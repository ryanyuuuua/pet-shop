const WINDOW_MS = 60_000;
const MAX_REQ_PER_WINDOW = 20;
const buckets = globalThis.__promptgptBuckets || (globalThis.__promptgptBuckets = new Map());

function ipOf(req) {
  return String(req.headers['x-forwarded-for'] || req.headers['x-real-ip'] || 'unknown').split(',')[0].trim();
}

function rateLimited(ip) {
  const now = Date.now();
  const rec = buckets.get(ip);
  if (!rec || now - rec.start >= WINDOW_MS) {
    buckets.set(ip, { start: now, count: 1 });
    return false;
  }
  rec.count += 1;
  return rec.count > MAX_REQ_PER_WINDOW;
}

function parseJSON(text) {
  const clean = String(text || '').trim().replace(/^```(?:json)?\s*/i, '').replace(/```$/i, '').trim();
  return JSON.parse(clean);
}

function sanitizeCandidates(value) {
  if (!Array.isArray(value)) return [];
  return value.slice(0, 60).map((p) => ({
    id: String(p?.id || '').slice(0, 12),
    categoryId: Number(p?.categoryId),
    category: String(p?.category || '').slice(0, 80),
    title: String(p?.title || '').slice(0, 160),
    usage: String(p?.usage || '').slice(0, 240),
  })).filter((p) => /^P\d{4}$/.test(p.id) && Number.isFinite(p.categoryId));
}

async function callGemini(model, instruction, key) {
  const ctl = new AbortController();
  const timer = setTimeout(() => ctl.abort(), 13_000);
  try {
    const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
      method: 'POST',
      signal: ctl.signal,
      headers: {
        'Content-Type': 'application/json',
        'x-goog-api-key': key,
      },
      body: JSON.stringify({
        contents: [{ role: 'user', parts: [{ text: instruction }] }],
        generationConfig: {
          temperature: 0.1,
          responseMimeType: 'application/json',
          maxOutputTokens: 650,
        },
      }),
    });
    if (!r.ok) throw new Error(`Gemini ${model}: ${r.status}`);
    const data = await r.json();
    const text = data?.candidates?.[0]?.content?.parts?.map((x) => x.text || '').join('') || '';
    return parseJSON(text);
  } finally {
    clearTimeout(timer);
  }
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const key = process.env.GEMINI_API_KEY;
  if (!key) return res.status(503).json({ error: 'AI search is not configured' });

  const ip = ipOf(req);
  if (rateLimited(ip)) return res.status(429).json({ error: 'Too many AI searches. Try again in a minute.' });

  const query = String(req.body?.query || '').trim().slice(0, 500);
  const candidates = sanitizeCandidates(req.body?.candidates);
  if (!query || candidates.length === 0) return res.status(400).json({ error: 'Invalid search request' });

  const list = candidates.map((p) => `${p.id} | category_id=${p.categoryId} | ${p.category} | ${p.title} | ${p.usage}`).join('\n');
  const instruction = `你是 PromptGPT 的搜尋排序引擎。使用者可能用繁體中文、粵語、英文或混合語言描述工作。\n\n你的唯一任務：從候選 Prompt 中挑出最適合使用者真正意圖的項目並排序。不要回答使用者的工作本身。\n\n使用者查詢：\n${query}\n\n候選 Prompt：\n${list}\n\n輸出嚴格 JSON：\n{\n  "rewritten_query": "一條更精準、簡短的搜尋語句",\n  "keywords": ["5-12個中英關鍵詞/同義詞"],\n  "category_ids": [最多4個最相關 category_id],\n  "top_prompt_ids": [按相關度排序、最多15個候選 Prompt ID],\n  "reason": "不超過25字的原因"\n}\n\n規則：top_prompt_ids 只能使用候選清單已有 ID；優先匹配任務意圖、交付物、語境、平台與品質要求，不要只做字面關鍵詞匹配；不要 Markdown。`;

  let lastError;
  for (const model of ['gemini-2.5-flash', 'gemini-2.5-flash-lite']) {
    try {
      const out = await callGemini(model, instruction, key);
      const ids = new Set(candidates.map((p) => p.id));
      const allowedCats = new Set(candidates.map((p) => p.categoryId));
      const result = {
        rewritten_query: typeof out.rewritten_query === 'string' ? out.rewritten_query.slice(0, 300) : '',
        keywords: Array.isArray(out.keywords) ? out.keywords.map(String).slice(0, 12) : [],
        category_ids: Array.isArray(out.category_ids) ? out.category_ids.map(Number).filter((n) => allowedCats.has(n)).slice(0, 4) : [],
        top_prompt_ids: Array.isArray(out.top_prompt_ids) ? out.top_prompt_ids.map(String).filter((id) => ids.has(id)).slice(0, 15) : [],
        reason: typeof out.reason === 'string' ? out.reason.slice(0, 120) : '',
        model,
      };
      res.setHeader('Cache-Control', 'no-store');
      return res.status(200).json(result);
    } catch (e) {
      lastError = e;
    }
  }

  console.error('PromptGPT Gemini search failed:', lastError?.message || lastError);
  return res.status(502).json({ error: 'AI search temporarily unavailable' });
}

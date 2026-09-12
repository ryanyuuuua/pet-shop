from pathlib import Path

p = Path('promptgpt/gemini.html')
s = p.read_text()

# 1) Friendly, human-readable titles for every generated prompt.
if 'function _friendlyTitle(' not in s:
    marker = 'function makePrompt('
    assert marker in s, 'makePrompt marker missing'
    helper = r'''function _friendlyTitle(category,focus,mode){const map={
'Master Build':`完整製作：${focus}`,
'Expert Audit':`專業檢查並改善：${focus}`,
'Strategy First':`${focus}：策略規劃版`,
'Production Ready':`${focus}：正式上線版`,
'Optimization':`全面優化：${focus}`,
'Research Backed':`${focus}：資料驗證版`,
'Rapid MVP':`${focus}：快速 MVP 版`,
'A/B Experiment':`${focus}：A/B 測試方案`,
'Reverse Engineer':`拆解參考並重建：${focus}`,
'Decision Framework':`${focus}：選擇與決策方案`,
'Troubleshoot':`排查並修復：${focus}`,
'SOP System':`${focus}：標準流程 SOP`
};return map[mode]||`${focus}｜${category}`}
'''
    s = s.replace(marker, helper + marker, 1)

old_title = 'title:`${c[0]} · ${focus} · ${m[0]}`'
new_title = 'title:_friendlyTitle(c[0],focus,m[0])'
if old_title in s:
    s = s.replace(old_title, new_title, 1)
assert new_title in s, 'friendly title replacement missing'

# 2) AI customizer UI inside each prompt drawer.
if 'id="customNeed"' not in s:
    needle = '<div class="tags" id="dtags"></div><div class="prompt" id="dprompt"></div><div class="actions">'
    assert needle in s, 'drawer insertion point missing'
    custom_ui = '''<div class="tags" id="dtags"></div><section class="customizer"><div class="customHead"><div><strong>✦ 幫我改成我需要嘅版本</strong><p>講你實際想做乜，Gemini 會保留原 Prompt 嘅專業結構，再改成你可以直接用嘅專屬版本。</p></div></div><textarea id="customNeed" rows="3" placeholder="例如：我要幫香港新開 cafe 整 Instagram 4:5 飲品宣傳圖，主角係士多啤梨梳打，要高級、真實、夏日感，唔好太 AI。"></textarea><div class="customBar"><button class="customBtn" id="customize">✦ AI 幫我改</button><span id="customStatus"></span></div><div class="customResultWrap" id="customResultWrap" hidden><div class="customResultHead"><strong>你的專屬 Prompt</strong><button class="secondary mini" id="copyCustom">複製專屬 Prompt</button></div><div class="prompt customResult" id="customResult"></div></div></section><div class="prompt" id="dprompt"></div><div class="actions">'''
    s = s.replace(needle, custom_ui, 1)

# 3) Styles for the customizer.
if '.customizer{' not in s:
    css = r'''
.customizer{margin:18px 0 14px;border:1px solid var(--border);border-radius:16px;background:var(--panel2);padding:16px}.customHead strong{font-size:15px}.customHead p{margin:5px 0 12px;color:var(--muted);font-size:12px;line-height:1.55}.customizer textarea{width:100%;min-height:84px;resize:vertical;border:1px solid var(--border);border-radius:12px;background:var(--bg);padding:12px;outline:0;line-height:1.5}.customizer textarea:focus{border-color:color-mix(in srgb,var(--text) 30%,var(--border))}.customBar{display:flex;align-items:center;gap:10px;margin-top:10px}.customBtn{border:0;background:var(--text);color:var(--bg);border-radius:10px;padding:9px 12px;cursor:pointer;font-weight:700}.customBtn:disabled{opacity:.45;cursor:default}#customStatus{font-size:11px;color:var(--muted);line-height:1.4}.customResultWrap{margin-top:14px}.customResultHead{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:8px}.customResult{margin:0;max-height:430px;overflow:auto;background:var(--bg)}.mini{padding:7px 9px;font-size:11px}@media(max-width:590px){.customizer{padding:13px}.customBar{align-items:flex-start;flex-direction:column}.customBtn{width:100%}.customResultHead{align-items:flex-start}}
'''
    s = s.replace('</style>', css + '</style>', 1)

# 4) Reset the AI-generated version when opening another prompt.
if 'function openPrompt(id){resetCustomizer();' not in s:
    assert 'function openPrompt(id){' in s, 'openPrompt marker missing'
    s = s.replace('function openPrompt(id){', 'function openPrompt(id){resetCustomizer();', 1)

# 5) Gemini prompt-customization logic. Uses the same locally stored Gemini key.
if 'async function customizeCurrentPrompt()' not in s:
    marker = 'async function runAI(){'
    assert marker in s, 'runAI marker missing'
    logic = r'''function resetCustomizer(){const n=$('#customNeed'),w=$('#customResultWrap'),r=$('#customResult'),st=$('#customStatus'),b=$('#customize');if(n)n.value='';if(w)w.hidden=true;if(r)r.textContent='';if(st)st.textContent='';if(b){b.disabled=false;b.textContent='✦ AI 幫我改'}}
function _customStatus(msg){const el=$('#customStatus');if(el)el.textContent=msg||''}
async function _callGeminiCustomizer(model,instruction,key){const ctl=new AbortController(),timer=setTimeout(()=>ctl.abort(),35000);try{const r=await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`,{method:'POST',signal:ctl.signal,headers:{'Content-Type':'application/json','x-goog-api-key':key},body:JSON.stringify({contents:[{role:'user',parts:[{text:instruction}]}],generationConfig:{maxOutputTokens:6000}})});if(!r.ok){const raw=await r.text();let info={};try{info=JSON.parse(raw)}catch{}const e=new Error(info?.error?.message||raw||`HTTP ${r.status}`);e.status=r.status;e.code=info?.error?.status||'';e.model=model;throw e}const d=await r.json(),text=d?.candidates?.[0]?.content?.parts?.map(x=>x.text||'').join('').trim()||'';if(!text){const e=new Error('EMPTY_RESPONSE');e.status=502;e.model=model;throw e}return text.replace(/^```(?:text|markdown|md)?\s*/i,'').replace(/```$/,'').trim()}finally{clearTimeout(timer)}}
async function customizeCurrentPrompt(){if(!current)return;const need=$('#customNeed').value.trim();if(!need){_customStatus('先寫低你實際想要咩，例如用途、對象、風格、平台、限制。');$('#customNeed').focus();return}let key=API_KEY||localStorage.getItem('pg-gemini-key')||'';if(!key){key=(prompt('貼上 Gemini API Key。只會儲存在你自己部機，用作 AI 搜尋同 Prompt 改寫。')||'').trim();if(!key){_customStatus('未設定 Gemini API Key。');return}API_KEY=key;localStorage.setItem('pg-gemini-key',key)}const btn=$('#customize');btn.disabled=true;btn.textContent='AI 改寫中…';_customStatus('Gemini 正在把原 Prompt 改成你嘅專屬版本…');const instruction=`你是一位世界級 Prompt Editor。你會收到「原始 Prompt」同「使用者真正需求」。你的任務不是回答原始 Prompt，而是重寫 Prompt 本身，讓使用者可以直接複製去 ChatGPT、Gemini、Claude、ImageGen 或其他相應模型使用。\n\n【使用者真正需求】\n${need}\n\n【原始 Prompt】\n${current.prompt}\n\n【改寫規則】\n1. 保留原 Prompt 最有價值的專業結構、品質門檻、QA、風險處理與輸出要求。\n2. 把使用者已提供的資料直接寫入 Prompt，不要再叫模型重問。\n3. 未提供但真正重要的資料才保留成清晰的 {{變數}}。\n4. 刪除同使用者需求無關的段落、重複內容和模板廢話。\n5. 根據實際任務加入必要的平台、受眾、格式、比例、語氣、技術或商業限制。\n6. 如果是圖片/影片 Prompt，要具體控制主體、構圖、鏡頭、光線、材質、色彩、動作、比例及要避免的問題。\n7. 如果是文字/編程/商業 Prompt，要具體定義輸入、步驟、交付物、驗收標準及錯誤處理。\n8. 不可捏造使用者沒有提供的品牌事實、數據或參考資料。\n9. 產出必須比原版更貼合、更短而不失專業，不要只是把使用者需求加在最前面。\n10. 只輸出「重寫後的完整 Prompt」，不要解釋、不要前言、不要 Markdown code fence。`;
let out='',err=null;for(const m of MODELS){try{out=await _callGeminiCustomizer(m,instruction,key);if(out)break}catch(e){err=e}}try{if(!out)throw err||new Error('Gemini unavailable');$('#customResult').textContent=out;$('#customResultWrap').hidden=false;_customStatus(`✓ 已用 Gemini 改成專屬版本`);$('#customResultWrap').scrollIntoView({behavior:'smooth',block:'nearest'})}catch(e){const code=e?.status?`HTTP ${e.status}`:'';if(e?.status===401){API_KEY='';localStorage.removeItem('pg-gemini-key');_customStatus(`Gemini Key 驗證失敗 ${code}。舊 Key 已清除，再撳一次重新輸入。`)}else if(e?.status===403)_customStatus(`Gemini 無權限 ${code}。請檢查 API Key 權限。`);else if(e?.status===429)_customStatus(`Gemini 配額暫時用盡 ${code}。稍後再試。`);else if(e?.name==='AbortError')_customStatus('Gemini 改寫逾時，請再試一次。');else _customStatus(`AI 改寫失敗${code?' · '+code:''}。`)}finally{btn.disabled=false;btn.textContent='✦ AI 幫我改'}}
'''
    s = s.replace(marker, logic + marker, 1)

# 6) Wire buttons.
if "$('#customize').onclick=customizeCurrentPrompt" not in s:
    marker = "$('#copy').onclick=async()=>{"
    assert marker in s, 'copy handler marker missing'
    handlers = r'''$('#customize').onclick=customizeCurrentPrompt;$('#customNeed').onkeydown=e=>{if((e.metaKey||e.ctrlKey)&&e.key==='Enter'){e.preventDefault();customizeCurrentPrompt()}};$('#copyCustom').onclick=async()=>{const text=$('#customResult').textContent.trim();if(!text)return;await navigator.clipboard.writeText(text);$('#copyCustom').textContent='✓ 已複製';setTimeout(()=>$('#copyCustom').textContent='複製專屬 Prompt',1200)};'''
    s = s.replace(marker, handlers + marker, 1)

# 7) Small copy polish so users understand what the feature is.
s = s.replace('PromptGPT · Curated Premium AI Prompts', 'PromptGPT · Curated Premium AI Prompts · AI 專屬改寫')

# Sanity checks.
assert '_friendlyTitle(c[0],focus,m[0])' in s
assert 'id="customNeed"' in s
assert 'async function customizeCurrentPrompt()' in s
assert "$('#customize').onclick=customizeCurrentPrompt" in s
assert 'gemini-3.8-flash' in s

p.write_text(s)
print('PROMPTGPT_V3_UPGRADE=PASS')
print('FRIENDLY_TITLES=PASS')
print('AI_CUSTOMIZER=PASS')
print('FILE_BYTES', len(s.encode()))

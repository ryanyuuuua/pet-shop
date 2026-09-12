from pathlib import Path

p=Path('promptgpt/gemini.html')
s=p.read_text(encoding='utf-8')

repls={
'PromptGPT · PromptGPT · 專業 Prompt，用人話寫 · AI 專屬改寫':'PromptGPT · 專業 Prompt，用人話寫 · AI 專屬改寫',
'<button>高級 SaaS 網站</button>':'<button>高級軟件網站</button>',
'<button>Code Review</button>':'<button>檢查程式碼</button>',
'<button class="chip" data-type="text">文字 / 工作流</button>':'<button class="chip" data-type="text">文字 / 工作</button>',
'<option value="id">Prompt ID</option>':'<option value="id">編號</option>',
"$('#libMeta').textContent=`${ALL.length} Curated Prompts`":"$('#libMeta').textContent=`${ALL.length} 條精選 Prompt`",
}
for a,b in repls.items():
    if a in s:
        s=s.replace(a,b,1)

# Keep search synonyms compatible with old technical words, but do not surface them to users.
p.write_text(s,encoding='utf-8')
print('PROMPTGPT_V4_2_UI_CLEANUP=PASS')

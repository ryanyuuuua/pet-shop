from pathlib import Path

p=Path('promptgpt/gemini.html')
s=p.read_text(encoding='utf-8')

# Replace jargon or noun duplication that survived the broad rules.
fixes={
"'Hero Character':'主角設計'":"'Hero Character':'遊戲主角'",
"'Villain':'反派設計'":"'Villain':'反派角色'",
"'iPhone App Mockup':'iPhone App 展示'":"'iPhone App Mockup':'iPhone App畫面'",
"'SaaS Dashboard Mockup':'軟件主頁展示'":"'SaaS Dashboard Mockup':'軟件數據畫面'",
"'Landing Page Mockup':'網頁設計展示'":"'Landing Page Mockup':'網頁設計圖'",
}
for a,b in fixes.items():
    if a in s:
        s=s.replace(a,b,1)

# Product 主視覺 is still design jargon for ordinary users.
needle="const TITLE_BASE={\n"
assert needle in s
s=s.replace(needle,needle+"'產品主視覺':'商品宣傳圖',\n",1)

# Hand-written titles for tasks where a generic action still sounded translated.
needle="const TITLE_SPECIAL={\n"
assert needle in s
extra="""const TITLE_SPECIAL={
'客服回覆模板':{'Master Build':'幫我寫客服回覆','SOP System':'整理客服回覆流程','Expert Audit':'檢查客服回覆','Optimization':'改善客服回覆'},
'Job Description':{'Master Build':'幫我寫招聘職位介紹','Strategy First':'規劃招聘職位','Expert Audit':'檢查招聘職位介紹','Optimization':'改善招聘職位介紹'},
"""
s=s.replace(needle,extra,1)

p.write_text(s,encoding='utf-8')
print('PROMPTGPT_V6_3_MANUAL_CLEANUP=PASS')

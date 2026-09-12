from pathlib import Path
import re

p=Path('promptgpt/gemini.html')
s=p.read_text(encoding='utf-8')

NEW_PICK = r'''function _pickModes(ci,fi){const cat=C[ci][0];const groups={
'網站策略':[0,2,1,4],'UI / UX':[0,2,1,4],
'Frontend':[0,3,1,10],'Backend':[0,3,1,10],'Mobile App':[0,3,1,10],'API / Integrations':[0,3,1,10],'Database / SQL':[0,3,1,10],'AI Agent':[0,3,1,10],
'Debugging':[10,1,4,11],'Code Review / Refactor':[1,4,10,3],'DevOps / Cloud':[0,3,10,11],
'Prompt Engineering':[0,1,4,7],'Automation / No-code':[0,11,10,4],
'Startup 驗證':[5,6,2,9],'產品管理':[2,9,6,1],'商業策略':[2,5,9,4],'市場研究':[5,1,9,2],'定價 / 變現':[2,5,7,4],
'Sales':[0,4,1,2],'Marketing':[0,4,7,1],'Copywriting':[0,4,1,2],'社交媒體':[0,4,7,1],'SEO / GEO':[0,4,1,5],'Email / Newsletter':[0,4,7,1],'E-commerce':[0,4,7,1],
'客戶服務':[0,11,1,4],'用戶研究':[5,0,1,9],'品牌策略':[2,0,5,1],'營運 / SOP':[11,0,1,4],'HR / 招聘':[0,11,1,4],'求職 / Portfolio':[0,1,4,2],
'數據分析':[5,0,1,9],'研究 / Fact-check':[5,1,9,0],'學術寫作':[0,1,4,2],'中文作文':[0,1,4,2],'英文寫作':[0,1,4,2],'學習 / 考試':[0,1,5,4],'STEM':[0,1,5,4],
'簡報 / Pitch':[0,1,4,2],'故事創作':[0,1,4,2],'YouTube / Video Script':[0,1,4,2],'Podcast / Audio':[0,1,4,2],'翻譯 / Localization':[0,1,4,2],'遊戲設計':[0,2,1,4]};
if(groups[cat])return groups[cat];if(C[ci][4]==='visual')return[0,1,4,8];return[0,1,2,4]}
function _friendlyTitle'''

s,n=re.subn(r"function _pickModes\(ci,fi\)\{.*?\}\nfunction _friendlyTitle",NEW_PICK,s,count=1,flags=re.S)
assert n==1,f'_pickModes patch failed: {n}'

# Make the choice label neutral and obvious.
s=s.replace("'Decision Framework':'幫你揀'","'Decision Framework':'比較選擇'")

p.write_text(s,encoding='utf-8')
print('PROMPTGPT_V5_1_MODE_MATCH=PASS')

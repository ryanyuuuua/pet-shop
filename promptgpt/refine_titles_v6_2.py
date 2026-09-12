from pathlib import Path

p=Path('promptgpt/gemini.html')
s=p.read_text(encoding='utf-8')

# Use mode sets that make sense for the whole category instead of forcing odd variants.
repls={
"'產品管理':[2,9,6,1]":"'產品管理':[0,2,1,4]",
"'市場研究':[5,1,9,2]":"'市場研究':[5,0,1,4]",
"'定價 / 變現':[2,5,7,4]":"'定價 / 變現':[2,5,1,4]",
"'用戶研究':[5,0,1,9]":"'用戶研究':[0,2,1,4]",
"'HR / 招聘':[0,11,1,4]":"'HR / 招聘':[0,2,1,4]",
"'學習 / 考試':[0,1,5,4]":"'學習 / 考試':[0,1,2,4]",
}
for a,b in repls.items():
    assert a in s, a
    s=s.replace(a,b,1)

# Visual design categories should say 設計, not 製作.
old="'Logo / Brand Identity':'visual','包裝設計':'visual','海報 / 平面設計':'visual','建築視覺':'visual','室內設計圖':'visual','角色設計':'visual','Game Art':'visual','3D / CGI':'visual','AI Video':'visual','Storyboard / Shot List':'visual','Infographic / Data Viz':'visual','UI Mockup / App Visual':'visual'"
new="'Logo / Brand Identity':'designvisual','包裝設計':'designvisual','海報 / 平面設計':'designvisual','建築視覺':'designvisual','室內設計圖':'designvisual','角色設計':'designvisual','Game Art':'designvisual','3D / CGI':'visual','AI Video':'visual','Storyboard / Shot List':'visual','Infographic / Data Viz':'designvisual','UI Mockup / App Visual':'designvisual'"
assert old in s
s=s.replace(old,new,1)
old_action="visual:{'Master Build':'幫我製作','Expert Audit':'幫我改善','Optimization':'幫我優化','Reverse Engineer':'參考重做'}};"
new_action="visual:{'Master Build':'幫我製作','Expert Audit':'幫我改善','Optimization':'幫我優化','Reverse Engineer':'參考重做'},designvisual:{'Master Build':'幫我設計','Expert Audit':'幫我改善','Optimization':'幫我優化','Reverse Engineer':'參考重做'}};"
assert old_action in s
s=s.replace(old_action,new_action,1)

# Natural short nouns for titles that still sounded like translated specifications.
insert="""'Stripe 整合':'網上付款','Google API 整合':'Google服務','多系統資料同步':'系統資料同步','第三方服務遷移':'外部服務搬遷','履歷重寫':'履歷','繁中香港化':'香港繁中','數學解題':'數學題','物理解題':'物理題','Hero Character':'遊戲主角','Villain':'反派角色','NPC':'遊戲配角','Boss Design':'Boss角色',"""
needle="const TITLE_BASE={\n'交易一致性'"
assert needle in s
s=s.replace(needle,"const TITLE_BASE={\n"+insert+"\n'交易一致性'",1)

# STEM wording should be what a student would actually say.
s=s.replace("stem:{'Master Build':'幫我解答','Expert Audit':'幫我檢查','Research Backed':'幫我解釋','Optimization':'幫我改善'}","stem:{'Master Build':'幫我解答','Expert Audit':'幫我檢查','Research Backed':'幫我講解','Optimization':'幫我改正'}",1)

# A few tasks need their own human title rather than a generic verb + noun formula.
old_special="const TITLE_SPECIAL={\n"
assert old_special in s
extra=r'''const TITLE_SPECIAL={
'繁中香港化':{'Master Build':'轉成香港繁中','Expert Audit':'校對香港繁中','Optimization':'潤色香港繁中','Strategy First':'調整香港用語'},
'Go to Market':{'Master Build':'制定產品推出計劃','Optimization':'改善產品推出計劃','A/B Experiment':'比較產品推出方案','Expert Audit':'檢查產品推出計劃'},
'Campaign Strategy':{'Master Build':'制定宣傳活動計劃','Optimization':'改善宣傳活動計劃','A/B Experiment':'比較宣傳活動方案','Expert Audit':'檢查宣傳活動計劃'},
'Audience Segmentation':{'Master Build':'整理目標客戶分類','Optimization':'改善目標客戶分類','A/B Experiment':'比較客戶分類方式','Expert Audit':'檢查目標客戶分類'},
'Channel Mix':{'Master Build':'規劃宣傳渠道','Optimization':'改善宣傳渠道','A/B Experiment':'比較宣傳渠道','Expert Audit':'檢查宣傳渠道'},
'Lead Magnet':{'Master Build':'製作吸客內容','Optimization':'改善吸客內容','A/B Experiment':'比較吸客內容','Expert Audit':'檢查吸客內容'},
'Referral Program':{'Master Build':'設計客戶轉介計劃','Optimization':'改善客戶轉介計劃','A/B Experiment':'比較客戶轉介方案','Expert Audit':'檢查客戶轉介計劃'},
'Launch Plan':{'Master Build':'制定新品推出計劃','Optimization':'改善新品推出計劃','A/B Experiment':'比較新品推出方案','Expert Audit':'檢查新品推出計劃'},
'Marketing Dashboard':{'Master Build':'製作宣傳數據表','Optimization':'改善宣傳數據表','A/B Experiment':'比較宣傳數據版面','Expert Audit':'檢查宣傳數據表'},
'''
s=s.replace(old_special,extra,1)

p.write_text(s,encoding='utf-8')
print('PROMPTGPT_V6_2_POLISH=PASS')

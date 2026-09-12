from pathlib import Path

p=Path('promptgpt/gemini.html')
s=p.read_text(encoding='utf-8')

# Shorten the few focus names that remained sentence-like after the first pass.
marker='const TITLE_BASE={'
assert marker in s
extras="""const TITLE_BASE={
'交易一致性':'資料交易','模組邊界重整':'程式模組','開場 Hook':'節目開場','深度研究':'研究資料','Fact Check':'資料查證','問題驗證':'創業想法','ICP 定義':'理想客戶','Cold Outreach':'開發客戶','Discovery Call':'客戶需要','Brand Positioning':'品牌定位',"""
s=s.replace(marker,extras,1)

# Normalise visible spacing around common English product names.
s=s.replace("function _titleBase(focus){let x=TITLE_BASE[focus]||_shortFocus(focus);x=String(x).replace(/\\s*／\\s*/g,'／')", "function _titleBase(focus){let x=TITLE_BASE[focus]||_shortFocus(focus);x=String(x).replace(/\\s*／\\s*/g,'／').replace(/AI \\s*/g,'AI').replace(/App \\s*/g,'App ')",1)

old="function _friendlyTitle(category,focus,mode){return `${_titleAction(category,mode)}${_titleBase(focus)}`}"
assert old in s
new=r'''const TITLE_SPECIAL={
'問題驗證':{'Research Backed':'研究創業需求','Rapid MVP':'測試創業想法','Strategy First':'規劃驗證方法','Decision Framework':'判斷創業需求'},
'ICP 定義':{'Research Backed':'研究理想客戶','Rapid MVP':'測試理想客群','Strategy First':'規劃目標客群','Decision Framework':'選出理想客群'},
'深度研究':{'Research Backed':'幫我做深度研究','Expert Audit':'檢查研究資料','Decision Framework':'比較研究結果','Master Build':'整理研究資料'},
'Fact Check':{'Research Backed':'幫我查證資料','Expert Audit':'檢查資料證據','Decision Framework':'比較資料來源','Master Build':'整理查證結果'},
'Cold Outreach':{'Master Build':'幫我寫開發訊息','Optimization':'改善開發訊息','Expert Audit':'檢查開發訊息','Strategy First':'規劃開發客戶'},
'Discovery Call':{'Master Build':'準備客戶訪談','Optimization':'改善銷售對話','Expert Audit':'檢查訪談問題','Strategy First':'規劃客戶訪談'},
'Brand Positioning':{'Strategy First':'規劃品牌定位','Master Build':'建立品牌定位','Research Backed':'研究品牌定位','Expert Audit':'檢查品牌定位'}};
function _friendlyTitle(category,focus,mode){const special=TITLE_SPECIAL[focus]&&TITLE_SPECIAL[focus][mode];if(special)return special;const base=_titleBase(focus),style=TITLE_STYLE[category]||'';if(style==='debug'){if(mode==='Troubleshoot')return `修好${base}`;if(mode==='Expert Audit')return `檢查${base}`;if(mode==='Optimization')return `改善${base}`;if(mode==='SOP System')return `${base}排查流程`;}return `${_titleAction(category,mode)}${base}`}'''
s=s.replace(old,new,1)

p.write_text(s,encoding='utf-8')
print('PROMPTGPT_V6_1_SEMANTIC_REFINE=PASS')

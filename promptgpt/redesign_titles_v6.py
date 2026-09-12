from pathlib import Path

p=Path('promptgpt/gemini.html')
s=p.read_text(encoding='utf-8')

old="function _friendlyTitle(category,focus,mode){return `${_shortFocus(focus)} · ${_simpleMode(mode)}`}"
assert old in s, 'old friendly title function not found'

new=r'''const TITLE_STYLE={
'網站策略':'website','UI / UX':'website',
'Frontend':'engineering','Backend':'engineering','Mobile App':'engineering','API / Integrations':'engineering','Database / SQL':'engineering','AI Agent':'engineering',
'Debugging':'debug','Code Review / Refactor':'review','DevOps / Cloud':'devops',
'Prompt Engineering':'prompt','Automation / No-code':'automation',
'Startup 驗證':'startup','產品管理':'product','商業策略':'strategy','市場研究':'research','定價 / 變現':'pricing',
'Sales':'sales','Marketing':'marketing','Copywriting':'writing','社交媒體':'social','SEO / GEO':'seo','Email / Newsletter':'email','E-commerce':'ecommerce',
'客戶服務':'service','用戶研究':'userresearch','品牌策略':'brand','營運 / SOP':'operations','HR / 招聘':'hr','求職 / Portfolio':'career',
'數據分析':'data','研究 / Fact-check':'research','學術寫作':'writing','中文作文':'writing','英文寫作':'writing','學習 / 考試':'study','STEM':'stem',
'簡報 / Pitch':'presentation','故事創作':'writing','YouTube / Video Script':'writing','Podcast / Audio':'media','翻譯 / Localization':'translation','遊戲設計':'game',
'產品攝影':'visual','飲品 / 食物攝影':'visual','Fashion Editorial':'visual','廣告創意圖':'visual','社交廣告視覺':'visual','電影感圖片':'visual','插畫':'visual','Anime / Manga':'visual','Logo / Brand Identity':'visual','包裝設計':'visual','海報 / 平面設計':'visual','建築視覺':'visual','室內設計圖':'visual','角色設計':'visual','Game Art':'visual','3D / CGI':'visual','AI Video':'visual','Storyboard / Shot List':'visual','Infographic / Data Viz':'visual','UI Mockup / App Visual':'visual'};
const TITLE_ACTION={
website:{'Master Build':'幫我設計','Strategy First':'幫我規劃','Expert Audit':'幫我檢查','Optimization':'幫我改善'},
engineering:{'Master Build':'幫我建立','Production Ready':'幫我完成','Expert Audit':'幫我檢查','Troubleshoot':'幫我修好'},
debug:{'Troubleshoot':'幫我修好','Expert Audit':'幫我檢查','Optimization':'幫我改善','SOP System':'整理好'},
review:{'Expert Audit':'幫我檢查','Optimization':'幫我整理','Troubleshoot':'幫我修好','Production Ready':'幫我完成'},
devops:{'Master Build':'幫我設定','Production Ready':'幫我完成','Troubleshoot':'幫我修好','SOP System':'整理好'},
prompt:{'Master Build':'幫我寫好','Expert Audit':'幫我檢查','Optimization':'幫我改善','A/B Experiment':'幫我比較'},
automation:{'Master Build':'幫我建立','SOP System':'整理好','Troubleshoot':'幫我修好','Optimization':'幫我改善'},
startup:{'Research Backed':'幫我研究','Rapid MVP':'幫我測試','Strategy First':'幫我規劃','Decision Framework':'幫我選擇'},
product:{'Strategy First':'幫我規劃','Decision Framework':'幫我選擇','Rapid MVP':'幫我測試','Expert Audit':'幫我檢查'},
strategy:{'Strategy First':'幫我規劃','Research Backed':'幫我分析','Decision Framework':'幫我選擇','Optimization':'幫我改善'},
research:{'Research Backed':'幫我研究','Expert Audit':'幫我查證','Decision Framework':'幫我比較','Strategy First':'幫我規劃','Master Build':'幫我整理'},
pricing:{'Strategy First':'幫我規劃','Research Backed':'幫我研究','A/B Experiment':'幫我比較','Optimization':'幫我改善'},
sales:{'Master Build':'幫我準備','Optimization':'幫我改善','Expert Audit':'幫我檢查','Strategy First':'幫我規劃'},
marketing:{'Master Build':'幫我規劃','Optimization':'幫我改善','A/B Experiment':'幫我比較','Expert Audit':'幫我檢查'},
writing:{'Master Build':'幫我寫好','Expert Audit':'幫我修改','Optimization':'幫我改善','Strategy First':'幫我規劃'},
social:{'Master Build':'幫我製作','Optimization':'幫我改善','A/B Experiment':'幫我比較','Expert Audit':'幫我檢查'},
seo:{'Master Build':'幫我處理','Optimization':'幫我改善','Expert Audit':'幫我檢查','Research Backed':'幫我研究'},
email:{'Master Build':'幫我寫好','Optimization':'幫我改善','A/B Experiment':'幫我比較','Expert Audit':'幫我檢查'},
ecommerce:{'Master Build':'幫我設計','Optimization':'幫我改善','A/B Experiment':'幫我比較','Expert Audit':'幫我檢查'},
service:{'Master Build':'幫我處理','SOP System':'整理好','Expert Audit':'幫我檢查','Optimization':'幫我改善'},
userresearch:{'Research Backed':'幫我研究','Master Build':'幫我準備','Expert Audit':'幫我檢查','Decision Framework':'幫我分析'},
brand:{'Strategy First':'幫我規劃','Master Build':'幫我設計','Research Backed':'幫我研究','Expert Audit':'幫我檢查'},
operations:{'SOP System':'整理好','Master Build':'幫我建立','Expert Audit':'幫我檢查','Optimization':'幫我改善'},
hr:{'Master Build':'幫我準備','SOP System':'整理好','Expert Audit':'幫我檢查','Optimization':'幫我改善'},
career:{'Master Build':'幫我準備','Expert Audit':'幫我修改','Optimization':'幫我改善','Strategy First':'幫我規劃'},
data:{'Research Backed':'幫我分析','Master Build':'幫我分析','Expert Audit':'幫我檢查','Decision Framework':'幫我比較'},
study:{'Master Build':'幫我整理','Expert Audit':'幫我檢查','Research Backed':'幫我解釋','Optimization':'幫我改善'},
stem:{'Master Build':'幫我解答','Expert Audit':'幫我檢查','Research Backed':'幫我解釋','Optimization':'幫我改善'},
presentation:{'Master Build':'幫我製作','Expert Audit':'幫我修改','Optimization':'幫我改善','Strategy First':'幫我規劃'},
media:{'Master Build':'幫我製作','Expert Audit':'幫我修改','Optimization':'幫我改善','Strategy First':'幫我規劃'},
translation:{'Master Build':'幫我翻譯','Expert Audit':'幫我校對','Optimization':'幫我潤色','Strategy First':'幫我調整'},
game:{'Master Build':'幫我設計','Strategy First':'幫我規劃','Expert Audit':'幫我檢查','Optimization':'幫我改善'},
visual:{'Master Build':'幫我製作','Expert Audit':'幫我改善','Optimization':'幫我優化','Reverse Engineer':'參考重做'}};
const TITLE_BASE={
'品牌官網資訊架構':'品牌網頁','高轉換 Landing Page':'宣傳單頁','SaaS 首頁策略':'軟件首頁','服務型企業網站':'公司網站','作品集網站':'作品集網站','活動及發布頁':'新品宣傳頁','多語網站規劃':'多語網站','網站重設與遷移':'網站改版',
'新手 onboarding':'新手教學','Dashboard 資訊架構':'數據主頁','Design System':'介面規則','Mobile Navigation':'手機選單','React 元件架構':'網頁程式','Next.js App Router':'網站結構','RWD 手機適配':'手機版網站','Accessibility 實作':'無障礙網站',
'REST API 設計':'資料接口','Authentication 系統':'登入功能','RBAC 權限':'用戶權限','Background Jobs':'背景任務','Webhook 系統':'自動通知','Caching 策略':'網站速度','Rate Limit':'使用次數限制',
'API 500 錯誤':'伺服器錯誤','記憶體洩漏':'記憶體問題','Race Condition':'同步錯誤','第三方 API 失效':'外部服務連接','間歇性 Bug':'間歇錯誤','Pull Request Review':'程式改動','Legacy Code 現代化':'舊程式','安全性 Code Review':'程式安全',
'CI Pipeline':'自動測試部署','Docker 化':'程式封裝','環境變數管理':'系統設定','Observability':'網站監察','Rollback 策略':'版本回復','Production Incident':'網站故障',
'OAuth Login':'帳戶登入','Webhook Consumer':'自動通知','API Client SDK':'連接工具','Retry 與 Idempotency':'安全重試','資料庫 Schema':'資料庫結構','SQL 查詢優化':'資料庫速度','Migration 計劃':'資料庫修改','RLS 政策':'資料權限',
'iOS App 架構':'iPhone App','Android App 架構':'Android App','跨平台 React Native':'跨平台 App','Push Notification':'手機通知','Mobile Performance':'App 速度',
'單一 Agent 工具鏈':'AI 助手工具','Multi Agent 團隊':'AI 助手團隊','Agent Memory':'AI 助手記憶','Tool Calling':'AI 自動工具','Human in the Loop':'真人確認流程','Agent 評估':'AI 助手測試','長任務編排':'AI 長任務',
'System Prompt':'AI 基本指令','Structured Output':'固定輸出格式','Few Shot Examples':'AI 示例指令','Prompt 壓縮':'精簡 AI 指令','Prompt 安全邊界':'AI 安全規則','多語 Prompt':'多語 AI 指令','Agent Prompt':'AI 助手指令','Prompt Evaluation':'AI 指令測試',
'Lead 自動化':'潛客自動流程','Email 工作流':'電郵自動流程','CRM 同步':'客戶資料同步','表單到資料庫':'表單自動入庫','審批流程':'審批流程','報表自動化':'自動報表','文件生成':'自動文件','失敗重試流程':'失敗重試流程',
'問題驗證':'創業問題驗證','ICP 定義':'理想客戶','假 Landing Page 測試':'介紹頁測試','Concierge MVP':'人工測試版本','Pivot 決策':'轉方向決定','PRD 撰寫':'功能說明','Roadmap 優先級':'功能優先次序','Feature Scoping':'功能範圍','North Star Metric':'主要成功指標','Release Planning':'推出時間','Backlog 整理':'待辦功能',
'Unit Economics':'每客戶盈利','Upsell 策略':'客戶升級','Freemium 策略':'免費收費方案','Cold Outreach':'陌生客戶開發','Discovery Call':'了解客戶需要','Demo Script':'產品示範','Proposal':'合作方案','Follow-up':'客戶跟進','成交後 Handoff':'成交後交接',
'Go to Market':'產品推出','Campaign Strategy':'宣傳活動','Audience Segmentation':'客戶分類','Channel Mix':'宣傳渠道','Lead Magnet':'吸客內容','Referral Program':'客戶轉介','Marketing Dashboard':'宣傳數據',
'Landing Page 文案':'宣傳頁文案','CTA 優化':'行動按鈕','品牌 About':'品牌介紹','FAQ 文案':'常見問題','Instagram Reels':'IG 短片','UGC Brief':'創作者要求','Keyword Cluster':'搜尋關鍵字','Search Intent':'搜尋目的','SEO Brief':'搜尋文章要求','Internal Linking':'網站內部連結','Technical SEO':'Google 收錄','Programmatic SEO':'大量搜尋頁','GEO 內容':'AI 搜尋曝光',
'Welcome Sequence':'新客歡迎電郵','Abandoned Cart':'追回棄單','Lead Nurture':'潛客培育','Reactivation':'喚醒舊客','Transactional Email':'系統通知電郵','Email A B Test':'電郵版本比較','Collection Page':'商品分類頁','Bundle 策略':'商品套裝','Cross-sell':'相關商品推薦','Review Strategy':'客戶評價',
'SLA 流程':'客服回覆時限','Usability Test':'產品易用測試','Survey':'問卷調查','JTBD Research':'用戶真正需要','Churn Interview':'流失客戶訪問','Concept Test':'概念測試','Persona Evidence':'客戶人物','Insight Synthesis':'研究重點',
'Brand Positioning':'品牌定位','Tone of Voice':'品牌語氣','Messaging House':'品牌核心訊息','Naming':'品牌改名','Rebrand Strategy':'品牌重塑','Brand Guidelines':'品牌規則','日常 SOP':'日常工作流程','Quality Checklist':'品質清單','營運 Dashboard':'營運數據',
'Job Description':'招聘職位介紹','Interview Scorecard':'面試評分表','Candidate Evaluation':'求職者評估','Onboarding':'新人入職','Performance Review':'員工評核','Team Handbook':'團隊手冊','Portfolio Case Study':'作品集個案','Cover Letter':'求職信','STAR 故事':'面試例子','LinkedIn Profile':'LinkedIn 個人頁',
'KPI 分析':'主要數據','Funnel 分析':'客戶流程','Cohort Analysis':'用戶批次','A B Test 分析':'版本測試數據','Dashboard 指標':'數據主頁指標','Forecast':'數據預測','Executive Insight':'管理層數據','Fact Check':'資料查證','Research Question':'研究問題','Essay Outline':'文章大綱','Literature Review':'文獻整理','Methodology':'研究方法','Argument Development':'論點證據','Critical Analysis':'批判分析','Citation Audit':'引用檢查','Abstract':'論文摘要',
'Argumentative Essay':'英文議論文','Narrative Writing':'英文記敘文','Formal Email':'正式英文電郵','Report Writing':'英文報告','Grammar Revision':'英文文法','Vocabulary Upgrade':'英文用字','IELTS Writing':'IELTS 寫作','Flashcards':'溫習卡','Study Schedule':'溫習時間表',
'Pitch Deck':'提案簡報','Sales Deck':'銷售簡報','Executive Update':'進度簡報','Case Study Deck':'個案簡報','Demo Presentation':'示範簡報','Investor Story':'投資者故事','Slide Audit':'簡報檢查','Plot Twist':'故事反轉','YouTube Long-form':'YouTube 長片','YouTube Shorts':'YouTube 短片','Explainer Video':'解說影片','Retention Rewrite':'影片留存','Podcast Episode':'Podcast 節目','Podcast Trailer':'Podcast 預告','Show Notes':'節目簡介','Sponsor Read':'贊助口播',
'Core Loop':'主要玩法','Economy Design':'遊戲經濟','Progression':'升級解鎖','Level Design':'關卡設計','Quest Design':'任務設計','Combat System':'戰鬥系統','Balance Pass':'遊戲平衡','Game Tutorial':'新手教學',
'Hero Product Shot':'商品宣傳圖','Luxury Editorial':'高級時尚照','Streetwear Campaign':'街頭服裝照','Beauty Portrait':'美容人像','Lookbook':'服裝展示照','Runway Backstage':'時裝後台照','Magazine Cover':'雜誌封面','Outdoor Billboard':'戶外廣告','Print Ad':'平面廣告','Brand Launch':'品牌宣傳圖','Instagram Feed Ad':'IG 貼文廣告','Story Ad':'限時動態廣告','Meta Carousel':'滑動式廣告','App Install Ad':'App 下載廣告','Lead Gen Ad':'客戶收集廣告','UGC Thumbnail':'用戶感封面','Retargeting Ad':'再營銷廣告',
'Neo Noir':'黑色電影畫面','Golden Hour':'黃昏電影畫面','Sci-fi Scene':'科幻場景','Hong Kong Night':'香港夜景','Period Drama':'年代劇畫面','Action Still':'動作電影畫面','Thriller Frame':'驚慄電影畫面','Editorial Illustration':'文章插畫','Children Book':'兒童繪本','Flat Vector':'扁平插畫','Watercolor':'水彩插畫','Ink Drawing':'水墨插畫','Isometric':'等距插畫','Conceptual Illustration':'概念插畫',
'Anime Portrait':'動漫人像','Manga Panel':'漫畫分鏡','Character Sheet':'角色設定','Slice of Life':'日常動漫場景','Anime Poster':'動漫海報','Wordmark':'文字 Logo','Symbol Mark':'圖形 Logo','Monogram':'字母 Logo','Mascot Logo':'吉祥物 Logo','Luxury Identity':'高級品牌形象','Tech Startup Logo':'科技品牌 Logo','Brand System':'品牌視覺系統','Typography Poster':'字體海報','Editorial Layout':'雜誌排版','Cafe Interior':'Cafe 室內設計','Hero Character':'主角設計','Villain':'反派設計','NPC':'遊戲角色','Fantasy Warrior':'奇幻戰士','Sci-fi Pilot':'科幻機師','Character Turnaround':'角色三視圖',
'Game Environment':'遊戲場景','Key Art':'遊戲宣傳圖','Weapon Concept':'武器設計','Prop Sheet':'道具設定','Level Mood':'關卡氣氛圖','Boss Design':'Boss 設計','Game UI Scene':'遊戲介面','Loading Screen':'載入畫面','3D Product Render':'3D 商品圖','Glass Material':'玻璃 3D 圖','Chrome CGI':'金屬 3D 圖','Abstract 3D':'抽象 3D 圖','Architectural CGI':'建築 3D 圖','Character Render':'角色 3D 圖','Motion Keyframe':'動畫關鍵畫面','Photoreal CGI':'寫實 3D 圖',
'Fashion Film':'時尚短片','Food Commercial':'食物廣告片','App Promo':'App 宣傳片','Cinematic Sequence':'電影感短片','30 秒廣告分鏡':'廣告分鏡','產品 Demo 分鏡':'產品示範分鏡','短片 Opening':'短片開場','Action Sequence':'動作分鏡','Tutorial Shots':'教學拍攝清單','Social Reel':'社交短片分鏡','統計 Infographic':'統計圖表','Timeline':'時間線圖','Dashboard Visual':'數據主頁圖','Annual Report Visual':'年報圖表','iPhone App Mockup':'iPhone App 展示','SaaS Dashboard Mockup':'軟件主頁展示','Landing Page Mockup':'網頁設計展示','Dark Mode UI':'深色介面','Fintech App':'金融 App 介面','Ecommerce App':'網店 App 介面','AI Product UI':'AI 產品介面','App Store Screenshots':'App 商店截圖'};
function _titleBase(focus){let x=TITLE_BASE[focus]||_shortFocus(focus);x=String(x).replace(/\s*／\s*/g,'／').replace(/網上訂閱軟件/g,'軟件').replace(/的內容/g,'').replace(/的流程/g,'流程').replace(/完整/g,'').trim();return x}
function _titleAction(category,mode){const style=TITLE_STYLE[category]||'website';const rules=TITLE_ACTION[style]||{};const fallback={'Master Build':'幫我製作','Expert Audit':'幫我檢查','Strategy First':'幫我規劃','Production Ready':'幫我完成','Optimization':'幫我改善','Research Backed':'幫我研究','Rapid MVP':'幫我測試','A/B Experiment':'幫我比較','Reverse Engineer':'參考重做','Decision Framework':'幫我選擇','Troubleshoot':'幫我修好','SOP System':'整理好'};return rules[mode]||fallback[mode]||'幫我處理'}
function _friendlyTitle(category,focus,mode){return `${_titleAction(category,mode)}${_titleBase(focus)}`}
function _cardDesc(mode){const x={'Master Build':'直接做出可以使用的版本，不只講概念。','Expert Audit':'找出最重要的問題，再逐項改善。','Strategy First':'先整理方向和需要，再決定怎樣做。','Production Ready':'以正式使用的標準完成並檢查。','Optimization':'保留做得好的部分，重點改善弱項。','Research Backed':'先查清楚資料，再給有根據的結果。','Rapid MVP':'先做最簡單可測試的版本。','A/B Experiment':'比較兩個版本，用結果決定哪個更好。','Reverse Engineer':'拆解好例子，再做成自己的版本。','Decision Framework':'比較不同選擇，再推薦最適合的一個。','Troubleshoot':'找出真正原因，再修好並確認。','SOP System':'整理成清楚、可以重複跟住做的步驟。'};return x[mode]||'直接給清楚、可以使用的結果。'}'''

s=s.replace(old,new,1)
old_desc="desc:`${task}｜${mode}`"
assert old_desc in s, 'old card desc not found'
s=s.replace(old_desc,"desc:_cardDesc(m[0])",1)

# Make the prompt opener sound natural while preserving the specialist standard.
old_open='請你以${role}的標準，幫我處理「${task}」。'
if old_open in s:
    s=s.replace(old_open,'請你當一位${role}，幫我完成「${task}」。',1)

p.write_text(s,encoding='utf-8')
print('PROMPTGPT_V6_TITLE_REDESIGN=PASS')

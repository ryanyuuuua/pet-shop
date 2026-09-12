from pathlib import Path
import re

p = Path('promptgpt/gemini.html')
s = p.read_text(encoding='utf-8')

HELPERS_AND_MAKE = r'''const CAT_PLAIN={
'網站策略':'網站規劃','UI / UX':'介面與使用體驗','Frontend':'網站畫面與互動','Backend':'網站後台與伺服器','Debugging':'找錯與修復','Code Review / Refactor':'程式檢查與整理','DevOps / Cloud':'部署與雲端','API / Integrations':'連接其他服務','Database / SQL':'資料庫','Mobile App':'手機 App','AI Agent':'AI 助手／Agent','Prompt Engineering':'AI 指令設計','Automation / No-code':'自動化流程','Startup 驗證':'創業點子驗證','產品管理':'產品規劃','商業策略':'商業策略','市場研究':'市場研究','定價 / 變現':'收費與賺錢方式','Sales':'銷售','Marketing':'市場推廣','Copywriting':'文案','社交媒體':'社交媒體','SEO / GEO':'Google／AI 搜尋曝光','Email / Newsletter':'Email／電子報','E-commerce':'網店','客戶服務':'客戶服務','用戶研究':'了解用戶','品牌策略':'品牌規劃','營運 / SOP':'營運流程','HR / 招聘':'招聘與員工','求職 / Portfolio':'求職與作品集','數據分析':'數據分析','研究 / Fact-check':'資料研究與查證','學術寫作':'學術寫作','中文作文':'中文作文','英文寫作':'英文寫作','學習 / 考試':'溫習與考試','STEM':'數理科','簡報 / Pitch':'簡報與提案','故事創作':'故事創作','YouTube / Video Script':'影片腳本','Podcast / Audio':'Podcast／音訊','翻譯 / Localization':'翻譯與本地化','遊戲設計':'遊戲設計','產品攝影':'產品攝影','飲品 / 食物攝影':'食物與飲品攝影','Fashion Editorial':'時尚攝影','廣告創意圖':'廣告圖片','社交廣告視覺':'社交媒體廣告圖','電影感圖片':'電影感圖片','插畫':'插畫','Anime / Manga':'動漫／漫畫','Logo / Brand Identity':'Logo／品牌識別','包裝設計':'包裝設計','海報 / 平面設計':'海報與平面設計','建築視覺':'建築效果圖','室內設計圖':'室內設計圖','角色設計':'角色設計','Game Art':'遊戲美術','3D / CGI':'3D 圖像','AI Video':'AI 影片','Storyboard / Shot List':'分鏡／拍攝清單','Infographic / Data Viz':'資訊圖表／數據圖','UI Mockup / App Visual':'App／網站介面展示圖'};
const MODE_PLAIN={'Master Build':'由零完整做好','Expert Audit':'檢查問題並改善','Strategy First':'先規劃清楚再開始','Production Ready':'做到可以正式使用','Optimization':'改善現有版本','Research Backed':'先查清楚資料再決定','Rapid MVP':'先做最簡單可測版本','A/B Experiment':'比較兩個版本邊個更好','Reverse Engineer':'拆解好例子再重新做','Decision Framework':'比較方案並幫你選擇','Troubleshoot':'找出問題再修好','SOP System':'整理成人人都跟到的固定步驟'};
const ROLE_PLAIN={'Staff 前端工程師':'資深前端工程師','Staff 後端工程師':'資深後端工程師','Staff Debug Engineer':'資深除錯工程師','Principal Engineer':'資深軟件工程師','Senior DevOps Engineer':'資深部署與雲端工程師','Integration Architect':'系統整合專家','Senior Database Engineer':'資深資料庫工程師','Senior Mobile Product Engineer':'資深手機 App 工程師','AI Agent Architect':'AI Agent 專家','Prompt Architect':'AI 指令設計專家','Automation Architect':'自動化流程專家','Startup Operator':'創業驗證顧問','Senior Product Manager':'資深產品經理','Strategy Consultant':'商業策略顧問','Market Intelligence Lead':'市場研究顧問','Pricing Strategist':'定價顧問','B2B Sales Coach':'B2B 銷售顧問','Growth Strategist':'市場推廣顧問','Conversion Copywriter':'轉換文案專家','Social Media Strategist':'社交媒體顧問','SEO Strategist':'搜尋曝光專家','Lifecycle Marketing Lead':'Email 與客戶留存顧問','Ecommerce Strategist':'網店顧問','CX Lead':'客戶體驗顧問','UX Research Lead':'用戶研究員','Brand Strategist':'品牌顧問','Operations Lead':'營運顧問','People Operations Lead':'招聘與人事顧問','Career Coach':'求職顧問','Senior Data Analyst':'資深數據分析師','Research Lead':'研究與查證專家','Academic Writing Coach':'學術寫作導師','Master Tutor':'學習導師','STEM Tutor':'數理科導師','Presentation Director':'簡報顧問','Story Editor':'故事編輯','Video Content Strategist':'影片內容顧問','Podcast Producer':'Podcast 製作人','Localization Lead':'翻譯與本地化專家','Lead Game Designer':'資深遊戲設計師','Product Photographer':'產品攝影師','Food Photographer':'食物攝影師','Fashion Art Director':'時尚美術指導','Creative Director':'廣告創意總監','Paid Social Art Director':'社交廣告美術指導','Cinematographer':'電影攝影師','Illustration Director':'插畫美術指導','Anime Art Director':'動漫美術指導','Brand Identity Director':'品牌識別設計師','Packaging Art Director':'包裝設計師','Graphic Design Director':'平面設計師','Architectural Visualizer':'建築效果圖設計師','Interior Art Director':'室內設計師','Character Art Director':'角色設計師','Game Art Director':'遊戲美術指導','CGI Director':'3D 圖像設計師','Film Director':'影片導演','Storyboard Director':'分鏡設計師','Information Designer':'資訊圖表設計師','Product Visual Designer':'產品介面視覺設計師'};
const FOCUS_PLAIN={
'品牌官網資訊架構':'品牌網站的頁面和內容安排','高轉換 Landing Page':'令更多人查詢或購買的單頁網站','SaaS 首頁策略':'SaaS 軟件首頁的內容和賣點','活動及發布頁':'活動／新產品發布頁','網站重設與遷移':'重新設計網站並安全搬資料','新手 onboarding':'新用戶第一次使用教學','Dashboard 資訊架構':'數據主頁要顯示甚麼和怎樣排列','Design System':'統一整個產品的介面設計規則','Mobile Navigation':'手機版選單和頁面導覽','React 元件架構':'整理 React 網站的程式結構','Next.js App Router':'用 Next.js App Router 安排頁面和功能','RWD 手機適配':'令網站在手機、平板和電腦都好用','Accessibility 實作':'令更多人包括殘障人士都能使用網站','REST API 設計':'設計系統之間交換資料的接口','Authentication 系統':'登入和身份驗證系統','RBAC 權限':'設定不同角色可以看甚麼、做甚麼','Background Jobs':'在背景自動執行耗時工作','Webhook 系統':'收到其他服務通知後自動處理','Caching 策略':'用快取加快網站和減少伺服器負擔','Rate Limit':'限制 API 使用次數，避免被濫用','API 500 錯誤':'找出伺服器 500 錯誤原因','記憶體洩漏':'找出程式愈用愈食記憶體的問題','Race Condition':'修正多個程序同時運行造成的錯誤','第三方 API 失效':'其他服務 API 壞咗時點處理','間歇性 Bug':'找出不是每次都出現的程式錯誤','Pull Request Review':'檢查準備合併的程式改動','Legacy Code 現代化':'整理舊程式，令它更安全易改','型別安全強化':'減少資料類型出錯','測試覆蓋改善':'增加自動測試，避免改壞功能','模組邊界重整':'重新整理不同程式部分的分工','安全性 Code Review':'檢查程式有沒有安全漏洞','CI Pipeline':'每次更新程式後自動測試和部署','Docker 化':'把程式包成容易在不同電腦運行的版本','環境變數管理':'安全管理 API Key 和不同環境設定','Observability':'監察網站狀態、錯誤和效能','Rollback 策略':'新版本出問題時快速退回舊版本','Production Incident':'正式網站出故障時的處理流程','OAuth Login':'用 Google／Apple 等帳號登入','Webhook Consumer':'接收並處理其他服務傳來的通知','API Client SDK':'做一套方便其他程式使用 API 的工具','Retry 與 Idempotency':'失敗後安全重試，而且不會重複做同一件事','資料庫 Schema':'設計資料庫要存甚麼和怎樣連結','SQL 查詢優化':'令資料庫查詢更快','Migration 計劃':'安全修改資料庫結構','RLS 政策':'限制每個用戶只可看到自己的資料','交易一致性':'確保一組資料操作要成功就全部成功','iOS App 架構':'規劃 iPhone App 的程式結構','Android App 架構':'規劃 Android App 的程式結構','跨平台 React Native':'用一套程式同時做 iPhone 和 Android App','Push Notification':'手機推送通知','Mobile Performance':'令手機 App 更快更順','單一 Agent 工具鏈':'讓一個 AI 助手懂得使用多種工具','Multi Agent 團隊':'讓多個 AI 助手分工合作','Agent Memory':'讓 AI 助手記住需要的資料','Tool Calling':'讓 AI 自動選擇和使用工具','Human in the Loop':'重要步驟由真人確認後 AI 才繼續','Agent 評估':'測試 AI 助手做得準不準','長任務編排':'安排 AI 完成多步驟長任務','System Prompt':'設定 AI 最基本的角色和規則','Structured Output':'要求 AI 用固定格式輸出','Few Shot Examples':'用幾個例子教 AI 跟你想要的方式做','Prompt 壓縮':'縮短 AI 指令但保留重要要求','Prompt 安全邊界':'限制 AI 不應做甚麼','多語 Prompt':'同一份 AI 指令支援多種語言','Agent Prompt':'給 AI Agent 使用的指令','Prompt Evaluation':'測試一份 AI 指令好不好用','Lead 自動化':'自動處理潛在客戶','Email 工作流':'自動發送和處理 Email','CRM 同步':'自動同步客戶資料','問題驗證':'先確認這個問題真的有人需要解決','ICP 定義':'找出最值得服務的理想客戶','假 Landing Page 測試':'先用簡單介紹頁測試有沒有人有興趣','Concierge MVP':'先用人工方式提供服務，驗證有人願意用','Pivot 決策':'判斷應否改變產品方向','PRD 撰寫':'寫清楚產品功能要做甚麼','Roadmap 優先級':'決定產品功能先做哪一些','Feature Scoping':'決定一個功能今次要做到甚麼程度','North Star Metric':'找出最重要的產品成功指標','Release Planning':'安排新功能幾時推出','Backlog 整理':'整理和排序待做功能','Unit Economics':'計清楚每個客戶實際賺不賺錢','Upsell 策略':'讓現有客戶願意升級或買更多','Freemium 策略':'免費版和付費版怎樣分','Cold Outreach':'主動聯絡未認識你的潛在客戶','Discovery Call':'第一次了解客戶需要的銷售對話','Demo Script':'產品示範時怎樣介紹','Proposal':'給客戶的正式合作方案','Follow-up':'客戶未回覆時怎樣跟進','成交後 Handoff':'成交後把客戶順利交給執行團隊','Go to Market':'產品推出市場的完整計劃','Campaign Strategy':'一次宣傳活動的整體計劃','Audience Segmentation':'把客戶分成不同類型','Channel Mix':'決定用哪些宣傳渠道','Lead Magnet':'用免費內容或工具吸引潛在客戶','Referral Program':'讓舊客戶介紹新客戶的計劃','Marketing Dashboard':'用數據主頁追蹤宣傳效果','Landing Page 文案':'單頁網站的銷售文案','CTA 優化':'改善按鈕和行動提示，令更多人願意下一步','品牌 About':'品牌「關於我們」內容','FAQ 文案':'常見問題頁內容','Instagram Reels':'Instagram Reels 短片內容','UGC Brief':'給用戶／創作者拍內容的清楚要求','Keyword Cluster':'整理一組相關搜尋關鍵字','Search Intent':'判斷搜尋者真正想找甚麼','SEO Brief':'給寫手的搜尋內容要求','Internal Linking':'安排網站內不同頁面互相連結','Technical SEO':'處理影響 Google 收錄的網站技術問題','Programmatic SEO':'用資料和模板大量建立搜尋頁面','GEO 內容':'讓內容更容易被 AI 搜尋答案引用','Welcome Sequence':'新訂閱者加入後的一連串 Email','Abandoned Cart':'追回放棄購物車的客人','Lead Nurture':'用一連串內容慢慢把潛在客戶變成客戶','Reactivation':'重新喚醒很久沒有互動的客戶','Transactional Email':'付款、註冊等系統通知 Email','Email A B Test':'比較兩個 Email 版本哪個效果更好','Collection Page':'網店商品分類頁','Bundle 策略':'把多件商品組合一起賣','Cross-sell':'推薦客戶順便買相關商品','Review Strategy':'增加和善用客戶評價','SLA 流程':'規定客服要在幾耐內回覆和解決','Usability Test':'測試真人用產品時哪裏卡住','Survey':'問卷調查','JTBD Research':'了解用戶真正想完成甚麼事情','Churn Interview':'訪問離開的客戶，找出為甚麼不用了','Concept Test':'在正式開發前測試一個概念是否吸引','Persona Evidence':'用真實證據建立客戶人物','Insight Synthesis':'把研究資料整理成真正有用的發現','Brand Positioning':'定清楚品牌在客戶心目中代表甚麼','Tone of Voice':'定義品牌平時怎樣說話','Messaging House':'整理品牌最重要的訊息和賣點','Naming':'幫品牌／產品改名','Rebrand Strategy':'重新定位和更新品牌','Brand Guidelines':'品牌設計和用字規則','日常 SOP':'日常工作固定步驟','Quality Checklist':'品質檢查清單','營運 Dashboard':'用數據主頁睇營運情況','Job Description':'招聘職位介紹','Interview Scorecard':'統一面試評分表','Candidate Evaluation':'比較和評估求職者','Onboarding':'新員工入職流程','Performance Review':'員工表現評核','Team Handbook':'團隊工作手冊','Portfolio Case Study':'作品集個案介紹','Cover Letter':'求職自薦信','STAR 故事':'用 STAR 方法整理面試例子','LinkedIn Profile':'LinkedIn 個人頁','KPI 分析':'看清楚主要業績數字','Funnel 分析':'找出客戶流程在哪一步流失','Cohort Analysis':'比較不同時間加入的用戶表現','A B Test 分析':'分析兩個版本哪個效果更好','Dashboard 指標':'決定數據主頁應看哪些數字','Forecast':'預測未來數字走勢','Executive Insight':'把複雜數據整理成管理層看得懂的重點','Fact Check':'查證一個說法是否可靠','Research Question':'定出清楚可研究的問題','Essay Outline':'文章／論文大綱','Literature Review':'整理和比較已有研究','Methodology':'說明研究會怎樣做','Argument Development':'把論點和證據一步步建立起來','Critical Analysis':'分析一個說法的優點、問題和證據','Citation Audit':'檢查引用是否正確','Abstract':'論文摘要','Argumentative Essay':'英文議論文','Narrative Writing':'英文記敘文','Formal Email':'正式英文 Email','Report Writing':'英文報告','Grammar Revision':'修改英文文法','Vocabulary Upgrade':'改善用字但保持自然','IELTS Writing':'IELTS 寫作','Flashcards':'溫習記憶卡','Study Schedule':'溫習時間表','Pitch Deck':'用來說服投資者／客戶的提案簡報','Executive Update':'給管理層看的簡短進度簡報','Case Study Deck':'用簡報展示一個成功個案','Demo Presentation':'產品示範簡報','Investor Story':'向投資者講清楚產品故事','Slide Audit':'檢查和改善整份簡報','Plot Twist':'故事反轉位','YouTube Long-form':'YouTube 長影片','YouTube Shorts':'YouTube Shorts 短片','Explainer Video':'解說影片','Retention Rewrite':'重寫影片令觀眾更願意看下去','Podcast Episode':'一集 Podcast 的完整內容','Podcast Trailer':'Podcast 預告','Show Notes':'Podcast 節目簡介和重點','Sponsor Read':'Podcast 中的贊助商口播','Brand Localization':'品牌內容本地化','Core Loop':'玩家不停重複的主要玩法','Economy Design':'遊戲內金錢和資源系統','Progression':'玩家升級和解鎖進度','Level Design':'關卡設計','Quest Design':'任務設計','Combat System':'戰鬥系統','Balance Pass':'調整遊戲數值令不同玩法更公平','Game Tutorial':'遊戲新手教學','Hero Product Shot':'最突出產品的主視覺照片','Luxury Editorial':'高級時尚雜誌風照片','Streetwear Campaign':'街頭服裝品牌宣傳照','Beauty Portrait':'美容／妝容人像','Lookbook':'服裝系列展示照','Runway Backstage':'時裝騷後台風格照片','Magazine Cover':'雜誌封面','Outdoor Billboard':'戶外大型廣告牌','Print Ad':'印刷廣告','Brand Launch':'品牌推出時的主宣傳圖','Instagram Feed Ad':'Instagram 貼文廣告','Story Ad':'直式限時動態廣告','Meta Carousel':'多張滑動式 Meta 廣告','App Install Ad':'吸引人下載 App 的廣告','Lead Gen Ad':'吸引潛在客戶留下資料的廣告','UGC Thumbnail':'用戶感內容風格封面','Retargeting Ad':'再次吸引看過產品的人回來的廣告','Neo Noir':'黑色電影感畫面','Golden Hour':'黃昏金色陽光畫面','Sci-fi Scene':'科幻場景','Hong Kong Night':'香港夜景電影感畫面','Period Drama':'年代劇畫面','Action Still':'動作電影定格畫面','Thriller Frame':'驚慄電影畫面','Editorial Illustration':'雜誌文章插畫','Children Book':'兒童繪本插畫','Flat Vector':'簡潔扁平向量插畫','Retro Poster':'復古海報插畫','Isometric':'等距視角插畫','Conceptual Illustration':'概念型插畫','Anime Portrait':'動漫人像','Manga Panel':'漫畫分鏡格','Character Sheet':'角色設定表','Slice of Life':'日常生活系動漫畫面','Anime Poster':'動漫海報','Wordmark':'純文字 Logo','Symbol Mark':'圖形 Logo','Monogram':'字母組合 Logo','Mascot Logo':'吉祥物 Logo','Luxury Identity':'高級品牌視覺識別','Tech Startup Logo':'科技初創 Logo','Brand System':'完整品牌視覺系統','Typography Poster':'以字體排版為主的海報','Editorial Layout':'雜誌／文章版面設計','Cafe Interior':'Cafe 室內設計','Hero Character':'主角角色設計','Villain':'反派角色設計','NPC':'非玩家角色設計','Fantasy Warrior':'奇幻戰士角色','Sci-fi Pilot':'科幻機師角色','Character Turnaround':'角色正面、側面、背面設定圖','Game Environment':'遊戲場景美術','Key Art':'遊戲主宣傳圖','Weapon Concept':'武器概念設計','Prop Sheet':'道具設定表','Level Mood':'關卡氣氛概念圖','Boss Design':'Boss 角色設計','Game UI Scene':'遊戲介面場景圖','Loading Screen':'遊戲載入畫面','3D Product Render':'3D 產品圖','Glass Material':'玻璃材質 3D 圖','Chrome CGI':'金屬鏡面 3D 圖','Abstract 3D':'抽象 3D 圖','Architectural CGI':'建築 3D 效果圖','Character Render':'角色 3D 效果圖','Motion Keyframe':'動畫關鍵畫面','Photoreal CGI':'像真照片的 3D 圖','Fashion Film':'時尚短片','Food Commercial':'食物廣告片','App Promo':'App 宣傳片','Cinematic Sequence':'連續電影感鏡頭','30 秒廣告分鏡':'30 秒廣告的逐鏡頭安排','產品 Demo 分鏡':'產品示範片的逐鏡頭安排','短片 Opening':'短片開場鏡頭','Action Sequence':'動作場面的逐鏡頭安排','Tutorial Shots':'教學影片拍攝清單','Social Reel':'社交平台短片分鏡','Dashboard Visual':'數據主頁視覺設計','Annual Report Visual':'年報資訊圖表','iPhone App Mockup':'iPhone App 展示圖','SaaS Dashboard Mockup':'SaaS 數據主頁展示圖','Landing Page Mockup':'網站單頁設計展示圖','Dark Mode UI':'深色模式介面','Fintech App':'金融科技 App 介面','Ecommerce App':'網店 App 介面','AI Product UI':'AI 產品介面','App Store Screenshots':'App Store 產品介紹截圖'};
function _catLabel(v){return CAT_PLAIN[v]||v}
function _modeLabel(v){return MODE_PLAIN[v]||v}
function _rolePlain(v){return ROLE_PLAIN[v]||String(v).replace(/^Senior /,'資深 ').replace(/^Lead /,'資深 ')}
function _plainFocus(v){return FOCUS_PLAIN[v]||v}
function _modeGoal(v){const x={
'Master Build':'由零開始，把需要的部分完整做好。','Expert Audit':'先找出真正影響結果的問題，再按重要程度逐一改善。','Strategy First':'先把目標、限制和方向想清楚，再開始做成品。','Production Ready':'用正式使用的標準完成，連同容易出錯的情況和之後維護都要考慮。','Optimization':'保留本身做得好的部分，只集中改善最影響結果的地方。','Research Backed':'先分清楚哪些是已知、哪些只是估計，再根據可靠資料做結論。','Rapid MVP':'先做最小但真的可以測試的版本，用最短時間驗證核心想法。','A/B Experiment':'把兩個不同版本放在同一標準下比較，用數據決定哪個更好。','Reverse Engineer':'先看懂高質參考為甚麼有效，只學原理，再重新做一個原創版本。','Decision Framework':'把幾個可行方案放在一起比較，清楚說明應選哪一個和原因。','Troubleshoot':'由表面問題一步步找出真正原因，只修需要修的地方，再確認真的解決。','SOP System':'把這件事整理成清楚、可重複、其他人也跟得到的固定流程。'};return x[v]||''}
function _friendlyTitle(category,focus,mode){const f=_plainFocus(focus),p={
'Master Build':'由零做好','Expert Audit':'檢查並改善','Strategy First':'先規劃清楚','Production Ready':'做到可以正式使用','Optimization':'改善效果','Research Backed':'先查清楚資料','Rapid MVP':'先做最簡單可測版本','A/B Experiment':'比較兩個版本','Reverse Engineer':'參考好例子再重新做','Decision Framework':'幫你揀最適合做法','Troubleshoot':'找出問題並修好','SOP System':'整理成清楚步驟'}[mode]||_modeLabel(mode);return `${p}：${f}`}
function makePrompt(ci,fi,mi,idNum){const c=C[ci],m=M[mi],focus=c[5][fi],plain=_plainFocus(focus),visual=c[4]==='visual',id='P'+String(idNum).padStart(4,'0'),mode=_modeLabel(m[0]),role=_rolePlain(c[3]);const vars=visual?'{你想呈現的主體／產品}、{會用在哪個平台或用途}、{畫面比例}、{品牌／想要的感覺}、{一定要出現的東西}、{一定不要出現的東西}、{光線／時間}、{可以參考但不能照抄的元素}':'{你最終想做到甚麼}、{給誰使用／目標客戶}、{現有資料或目前情況}、{不能違反的限制}、{怎樣才算成功}、{品牌／語氣}、{你想收到的格式}、{時間／人手／預算等資源}';const truth=visual?'不要自己作出不存在的品牌資料、產品細節或文字；不知道的地方請留成可以替換的欄位。':'不要把估計當成事實；資料不足時要清楚標示假設。如果答案依賴外部資料，要直接指出哪一部分需要再查證。';const special=visual?'把主體大小和位置、鏡頭角度、材質、光線、顏色、背景、留白和不同平台裁切方式說清楚。':'不要只講原則。能直接寫成文案、步驟、表格、規格、程式碼或明確決定的地方，就直接交出可用版本。';return{id,ci,mi,fi,type:visual?'visual':'text',quality:96,title:_friendlyTitle(c[0],focus,m[0]),desc:`適合想要「${plain}」的人。做法：${mode}。`,models:visual?'Gemini / ImageGen / Midjourney':'ChatGPT / Gemini / Claude',tags:[_catLabel(c[0]),plain,mode,visual?'圖片／影片':'文字／工作'],prompt:`請你當一位${role}，幫我完成「${plain}」。

這個任務的專業名稱是「${focus}」，今次會用「${mode}」的方式處理。請以專業標準做，但全程用一般人看得懂的說話。真的需要用專業詞時，第一次出現要順手解釋它是甚麼。

【你要完成的事】
${_modeGoal(m[0])}
最後要針對「${plain}」交出一份可以直接使用、交給別人執行、測試或正式使用的版本。原本要注意的重點仍然包括：${c[2]}。

【先看這些資料】
${vars}

如果有重要資料未提供：
1. 最多只問 3 個真的會影響結果的問題；
2. 如果不值得停下來等答案，就清楚寫明假設，再繼續完成；
3. 不要用空泛說話掩蓋不知道的地方。

【做法】
- 一開始先講清楚：做到怎樣才算成功，以及甚麼結果不能接受。
- 把事情分成「一定要做 / 最好做 / 暫時可以不做」。
- 每個重要建議都要講明它解決甚麼問題；如果只是推測，要標示清楚。
- ${special}
- 主動檢查少見但可能出錯的情況、手機或真實使用場景、之後是否容易修改，以及出錯時怎樣處理。
- 如果有合理的第二種做法，至少給 2 個真的不同的選擇，並用簡單說話講明哪種情況應選哪一個。
- ${truth}

【最後要交給我的內容】
A. 一句話結論：你建議我怎樣做，以及最重要的取捨。
B. 成功標準：列 3–7 個可以直接檢查是否做到的條件。
C. 主要成品：交出完整、可直接使用的版本，不要只給大綱。
D. 重要決定和原因：只保留真的會影響結果的理由。
E. ${m[3]}。
F. 可能出問題的地方：至少 5 項，並附上應對方法。
G. 完成前檢查：逐項檢查準確、完整、前後一致、真的做得到、適合使用平台，而且沒有把假設當成事實。
H. 下一步：列出現在最值得立即做的 3 件事。

【完成前檢查】
- 要具體：不要只寫「優化一下」「提升質感」，要講清楚實際怎樣做。
- 要可檢查：重要成果都要有驗收方法或成功指標。
- 不要重複：不同段落不要只是換句話重講同一件事。
- 要原創：可以學參考作品背後的原理，但不要逐字、逐圖或逐像素照抄。
- 不要為了看起來專業而堆砌術語；能用普通說話講清楚，就用普通說話。
- 如果真的要保留專業詞，第一次出現時用括號補一句簡單解釋。
- 自評低於 92/100，就先自行修正，再交出最後版本。
- 不要展示冗長的內部思考，只交結論、必要理由、成品和可以驗證的證據。`}}
function _quality'''

pattern = r"function _friendlyTitle\(category,focus,mode\)\{.*?\}\nfunction makePrompt\(ci,fi,mi,idNum\)\{.*?\}\nfunction _quality"
s, n = re.subn(pattern, HELPERS_AND_MAKE, s, count=1, flags=re.S)
assert n == 1, f'friendly/makePrompt replacement count={n}'

NEW_QUALITY = r'''function _quality(p){let q=84;if(p.prompt.length>1200)q+=4;if(p.prompt.includes('【最後要交給我的內容】'))q+=3;if(p.prompt.includes('可能出問題的地方'))q+=3;if(p.prompt.includes('完成前檢查'))q+=3;if(p.prompt.includes('不要把估計當成事實')||p.prompt.includes('不要自己作出不存在'))q+=2;if(p.prompt.includes('真的不同的選擇'))q+=1;return Math.min(q,100)}
function curateLibrary'''
s, n = re.subn(r"function _quality\(p\)\{.*?\}\nfunction curateLibrary", NEW_QUALITY, s, count=1, flags=re.S)
assert n == 1, f'quality replacement count={n}'

replacements = {
    "${p.id} · ${esc(C[p.ci][0])}": "${p.id} · ${esc(_catLabel(C[p.ci][0]))}",
    "`${current.id} · ${C[current.ci][0]} · ${M[current.mi][0]}`": "`${current.id} · ${_catLabel(C[current.ci][0])} · ${_modeLabel(M[current.mi][0])}`",
    "`<button class=\"cat\" data-cat=\"${i}\"><span>${c[0]}</span><em>${categoryCounts[i]}</em></button>`": "`<button class=\"cat\" data-cat=\"${i}\"><span>${_catLabel(c[0])}</span><em>${categoryCounts[i]}</em></button>`",
}
for old, new in replacements.items():
    assert old in s, f'missing replacement marker: {old[:80]}'
    s = s.replace(old, new, 1)

# Make the AI customizer keep the same plain-language standard too.
old = "9. 產出必須比原版更貼合、更短而不失專業，不要只是把使用者需求加在最前面。\\\n10. 只輸出「重寫後的完整 Prompt」，不要解釋、不要前言、不要 Markdown code fence。`"
new = "9. 產出必須比原版更貼合、更短而不失專業，不要只是把使用者需求加在最前面。\\\n10. 全文用一般人看得懂的說話；真的需要專業詞時，第一次出現要用括號簡單解釋。\\\n11. 簡化文字時不可刪走原本的重要限制、驗收標準、風險處理或輸出格式。\\\n12. 只輸出「重寫後的完整 Prompt」，不要解釋、不要前言、不要 Markdown code fence。`"
assert old in s, 'customizer instruction marker missing'
s = s.replace(old, new, 1)

# Small UI copy polish for non-technical users.
s = s.replace('Curated Prompt Library · Gemini Search','簡單易明 Prompt 庫 · AI 智能搜尋')
s = s.replace('Curated Premium AI Prompts · AI 專屬改寫','PromptGPT · 專業 Prompt，用人話寫 · AI 專屬改寫')
s = s.replace('即時本地索引 + Gemini 3.8 Flash 雲端語意重排。<br>不下載任何 AI 模型。','打字即時搜尋，再由 Gemini 幫你理解意思和排序。<br>手機不需要下載 AI 模型。')
s = s.replace('講你實際想做乜，Gemini 會保留原 Prompt 嘅專業結構，再改成你可以直接用嘅專屬版本。','講你實際想做乜，Gemini 會保留原本的重要要求，再用更貼合你情況的方式重寫。')

p.write_text(s, encoding='utf-8')
print('PROMPTGPT_V4_PLAIN_LANGUAGE_PATCH=PASS')

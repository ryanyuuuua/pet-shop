from pathlib import Path

p=Path('promptgpt/gemini.html')
s=p.read_text(encoding='utf-8')

assert 'const FOCUS_PLAIN={' in s

# Finish translating every remaining English-heavy focus label into outcome language.
extra={
'Vercel 部署':'將網站正式放上網','Stripe 整合':'在網站加入網上付款','Google API 整合':'讓網站連接 Google 服務','App Store 上架':'將 iPhone App 正式上架','SaaS 套餐設計':'網上訂閱軟件的收費方案','Launch Plan':'新產品推出計劃','銷售 Email':'用 Email 說服潛在客戶','App Store 文案':'App Store 產品介紹文字','Threads 貼文':'Threads 帖文','LinkedIn 內容':'LinkedIn 貼文內容','TikTok 腳本':'TikTok 短片腳本','Newsletter':'定期電子報','Product Launch Email':'新產品推出 Email','Article Writing':'英文文章','Sales Deck':'銷售簡報','Vlog Story':'日常影片的故事流程','開場 Hook':'一開始就吸引人繼續聽的開場','節目 Rundown':'節目每一段的流程安排','Audio Story':'用聲音講故事的節目','App Localization':'App 多語言和本地化','Marketing Localization':'宣傳內容本地化','翻譯 QA':'檢查翻譯是否自然準確','Jewelry Fashion':'珠寶時尚宣傳照','Sportswear':'運動服裝宣傳照','節日 Campaign':'節日宣傳主題','品牌 Launch':'品牌推出時的宣傳','TikTok Cover':'TikTok 短片封面','Romantic Scene':'浪漫電影場景','Watercolor':'水彩插畫','Ink Drawing':'水墨／墨線插畫','School Scene':'校園動漫場景','Action Scene':'動漫動作場景','Fantasy Anime':'奇幻動漫場景','Restaurant Brand':'餐廳 Logo 和品牌視覺','Menu Design':'餐牌／菜單設計','Flyer':'宣傳單張','Mascot':'吉祥物角色','Historical Character':'歷史人物角色設計','Travel Film':'旅遊短片','Music Video':'音樂影片','統計 Infographic':'統計數據資訊圖','Timeline':'時間線資訊圖'}
insert=''.join(repr(k)+':'+repr(v)+',' for k,v in extra.items())
s=s.replace('const FOCUS_PLAIN={\n','const FOCUS_PLAIN={\n'+insert+'\n',1)

# Remove unnecessary jargon even from focuses that were already translated.
repls={
"'SaaS 首頁策略':'SaaS 軟件首頁的內容和賣點'":"'SaaS 首頁策略':'網上訂閱軟件首頁的內容和賣點'",
"'React 元件架構':'整理 React 網站的程式結構'":"'React 元件架構':'整理網站畫面程式的結構'",
"'Next.js App Router':'用 Next.js App Router 安排頁面和功能'":"'Next.js App Router':'安排網站頁面和功能的程式結構'",
"'跨平台 React Native':'用一套程式同時做 iPhone 和 Android App'":"'跨平台 React Native':'用一套程式同時做 iPhone 和 Android App'",
"'第三方 API 失效':'其他服務 API 壞咗時點處理'":"'第三方 API 失效':'其他外部服務連接失效時怎樣處理'",
"'API Client SDK':'做一套方便其他程式使用 API 的工具'":"'API Client SDK':'做一套方便其他程式連接你服務的開發工具'",
"'SaaS Dashboard Mockup':'SaaS 數據主頁展示圖'":"'SaaS Dashboard Mockup':'網上訂閱軟件的數據主頁展示圖'",
"'AI Agent':'AI 助手／Agent'":"'AI Agent':'AI 助手'"
}
for a,b in repls.items():
    if a in s:s=s.replace(a,b,1)

SCOPE={
'網站策略':'網站要講甚麼、頁面怎樣安排、怎樣讓訪客更容易採取行動，以及如何配合商業目標。','UI / UX':'用戶由開始到完成任務是否順手、畫面是否容易理解、操作是否清楚，以及不同人士是否都能使用。','Frontend':'網站畫面和互動的程式如何安排、手機是否好用、速度、穩定性和可使用性。','Backend':'登入、權限、資料處理、伺服器速度、安全，以及日後是否容易維護。','Debugging':'先重現問題、找真正原因、只改需要改的地方，然後確認沒有引發新問題。','Code Review / Refactor':'程式是否易讀、結構是否清楚、有沒有重複或安全問題，以及怎樣逐步整理。','DevOps / Cloud':'自動測試和部署、不同環境設定、監察網站狀況、出事時怎樣恢復，以及怎樣控制雲端成本。','API / Integrations':'網站如何安全連接其他服務、交換資料、處理失敗，以及避免同一件事被重複執行。','Database / SQL':'資料要怎樣儲存和連結、查詢速度、資料正確性、安全權限，以及修改資料庫時的風險。','Mobile App':'iPhone／Android 的使用流程、觸控操作、沒有網絡時怎樣用、通知、速度和正式上架。','AI Agent':'AI 助手的角色、可以用甚麼工具、要記住甚麼、多個 AI 如何分工，以及失敗時怎樣處理。','Prompt Engineering':'怎樣把要求講清楚、提供例子、限制輸出格式、測試效果，以及讓 AI 自己檢查。','Automation / No-code':'甚麼情況自動開始、資料由哪裏去到哪裏、哪些步驟要人確認、出錯時怎樣重試和留下記錄。','Startup 驗證':'這個問題是否真的有人在意、最值得服務的是誰、用最小版本怎樣驗證，以及怎樣判斷繼續還是改方向。','產品管理':'用戶真正要解決甚麼、功能要做到甚麼、先做甚麼、怎樣量度成功，以及幾時推出。','商業策略':'市場機會、競爭對手、如何賺錢、成本、合作機會和長期優勢。','市場研究':'市場有多大、客戶可以分成哪些類型、競爭對手和替代方案是甚麼，以及證據是否可靠。','定價 / 變現':'客戶為甚麼願意付錢、不同收費方案怎樣分、價格對收入和成本有甚麼影響，以及怎樣測試。','Sales':'怎樣找到潛在客戶、了解需要、示範產品、寫方案、處理疑問、跟進和成交。','Marketing':'對誰講、講甚麼、在哪裏宣傳、怎樣設計宣傳活動，以及怎樣知道有沒有效果。','Copywriting':'讀者最在意甚麼、產品價值怎樣講、開頭如何吸引、用甚麼證據，以及最後叫人做甚麼。','社交媒體':'平時應發甚麼內容、開頭怎樣吸引人、不同平台怎樣寫、幾時發，以及怎樣增加互動。','SEO / GEO':'人們會搜尋甚麼、網站內容是否容易被 Google 和 AI 找到、頁面怎樣互相連結，以及技術問題是否影響收錄。','Email / Newsletter':'主旨怎樣吸引人、寄給哪類客戶、幾時寄、內容是否有價值，以及怎樣讓讀者採取下一步。','E-commerce':'商品資料是否清楚、客戶是否信任、購買流程是否順暢、怎樣提高每張訂單價值，以及怎樣令客戶再買。','客戶服務':'怎樣理解和分類問題、回覆是否有同理心、甚麼情況要升級處理、多久內要回覆，以及知識庫是否清楚。','用戶研究':'真正要研究甚麼、找哪些人、怎樣訪問或測試、哪些是真實行為證據，以及最後如何變成產品決定。','品牌策略':'品牌代表甚麼、想讓人記住甚麼、平時怎樣說話、視覺和訊息要如何保持一致。','營運 / SOP':'每件事由誰負責、先做甚麼後做甚麼、哪裏要檢查、出例外時怎樣處理，以及怎樣提升效率。','HR / 招聘':'職位需要甚麼人、怎樣招聘和面試、怎樣公平評估、新人如何入職，以及之後怎樣看表現。','求職 / Portfolio':'履歷和作品集怎樣突出能力、怎樣準備面試、如何證明經驗，以及薪酬和職涯方向怎樣談。','數據分析':'先清理資料、看哪些數字、找出變化和異常、用合適圖表說明，以及最後提出可行建議。','研究 / Fact-check':'研究問題是否清楚、來源是否可靠、不同證據是否一致、有沒有反面證據，以及結論有哪些限制。','學術寫作':'論題是否清楚、資料和研究是否足夠、論點怎樣一步步建立、引用是否正確，以及是否有批判分析。','中文作文':'中心思想、文章結構、描寫和論證、語氣修辭，以及是否符合學生年級。','英文寫作':'中心論點、文章結構、句子是否清楚、文法、語氣、證據和最後修改。','學習 / 考試':'先找出不懂哪裏、用簡單方法解釋、安排練習和重溫，以及確認是否真的學懂。','STEM':'概念是否明白、計算和推導步驟是否正確、單位和答案有沒有驗算，以及常見錯誤。','簡報 / Pitch':'故事線是否清楚、每頁應放甚麼、數據怎樣展示、版面是否易看，以及怎樣說服觀眾採取下一步。','故事創作':'角色想要甚麼、衝突是否足夠、節奏和場景是否吸引、伏筆和轉折是否合理，以及主題是否清楚。','YouTube / Video Script':'開頭能否吸引人、內容節奏、觀眾為甚麼會繼續看、畫面需要甚麼，以及最後怎樣引導下一步。','Podcast / Audio':'節目定位、每一段怎樣安排、主持節奏、訪問問題、聲音效果和剪輯提示。','翻譯 / Localization':'意思是否準確、是否符合當地文化、專有名詞是否一致、語氣是否自然，以及格式是否保留。','遊戲設計':'玩家主要會做甚麼、不同系統怎樣互相影響、難度和獎勵是否平衡、怎樣升級，以及玩家是否得到清楚回饋。','產品攝影':'產品大小和材質是否真實、光線和陰影、背景、反光，以及圖片是否適合廣告和網店使用。','飲品 / 食物攝影':'食物是否看起來新鮮好吃、飲品層次、冰霜或蒸氣、道具、光線，以及整體是否有食慾感。','Fashion Editorial':'服裝造型、模特姿勢、鏡頭、場景、光線和整體時尚質感。','廣告創意圖':'核心創意是否清楚、產品是否突出、構圖、品牌元素、文案留位、情緒和是否有助轉換。','社交廣告視覺':'貼文、限時動態和短片封面是否一眼吸引、文字安全區、平台比例，以及手機上是否清楚。','電影感圖片':'鏡頭、光線、人物和物件位置、色彩、氣氛、景深，以及畫面是否像在講故事。','插畫':'畫風、線條、色塊、構圖、想表達的意思、背景，以及一系列圖片是否一致。','Anime / Manga':'角色表情和動作、線稿、上色、構圖、背景、鏡頭，以及不同畫面是否保持同一角色。','Logo / Brand Identity':'品牌概念、圖形或文字標誌、是否夠簡潔、縮細後是否清楚、黑白時是否仍然好看，以及實際應用。','包裝設計':'包裝形狀、正背面資料、材質、放在貨架上是否容易認出、品牌感，以及能否真的印刷製作。','海報 / 平面設計':'版面次序、字體、圖形、留白、最重要資料是否突出，以及印刷後是否清楚。','建築視覺':'建築形狀、材料、大小比例、周圍環境、時間和天氣、鏡頭，以及自然光是否合理。','室內設計圖':'空間怎樣分配、材料、家具、燈光、鏡頭、生活感，以及設計是否看起來真的可以使用。','角色設計':'角色輪廓、衣服、表情、姿勢、材質、背景故事，以及不同角度是否保持一致。','Game Art':'整體美術方向、場景、角色、材質、介面和氣氛，以及玩家是否一眼看得懂重要物件。','3D / CGI':'物件形狀、材質、燈光、鏡頭、大小比例、物理感，以及最後畫面是否自然可信。','AI Video':'每個鏡頭要發生甚麼、角色或產品怎樣動、鏡頭怎樣移動、前後是否連貫、光線、轉場和聲音提示。','Storyboard / Shot List':'每個鏡頭為甚麼要拍、拍多近、相機放哪裏、人物怎樣動、鏡頭怎樣接，以及實際是否拍得到。','Infographic / Data Viz':'資料先後次序、應用哪種圖表、標示是否清楚、是否容易閱讀、故事線，以及有沒有誤導數據。','UI Mockup / App Visual':'裝置外框、介面層次、畫面是否像真產品、品牌感、背景，以及是否能清楚展示產品用途。'}

scope_js='const SCOPE_PLAIN='+repr(SCOPE).replace("'",'"')+';\n'
scope_js += "const MODE_DELIVERABLE={'Master Build':'完整成品、重要決定，以及最後檢查清單。','Expert Audit':'問題清單、每個問題的證據和嚴重程度，以及先修甚麼。','Strategy First':'選擇的方向、為甚麼這樣選，以及實際執行次序。','Production Ready':'正式可用版本、已知風險，以及最後測試清單。','Optimization':'改善前後比較、改了甚麼，以及應該先做哪幾項。','Research Backed':'可靠資料、最後結論、限制，以及仍然要查證的地方。','Rapid MVP':'最小版本要包含甚麼、3 步測試方法，以及成功／失敗標準。','A/B Experiment':'兩個版本、比較哪些數字，以及最後怎樣判定。','Reverse Engineer':'參考作品有效的原理、你的原創版本，以及兩者有甚麼不同。','Decision Framework':'方案比較表、最推薦哪個，以及甚麼情況不應選它。','Troubleshoot':'真正原因、最小修復方法，以及確認已經修好的步驟。','SOP System':'固定流程、檢查清單、例外情況，以及交接方法。'};\n"
scope_js += "function _plainScope(cat,raw){return SCOPE_PLAIN[cat]||raw}\nfunction _modeDeliverable(mode){return MODE_DELIVERABLE[mode]||'補充需要交付的內容。'}\n"
marker='function _catLabel(v){return CAT_PLAIN[v]||v}'
assert marker in s
s=s.replace(marker,scope_js+marker,1)

old='原本要注意的重點仍然包括：${c[2]}。'
assert old in s
s=s.replace(old,'要特別留意：${_plainScope(c[0],c[2])}',1)
old='E. ${m[3]}。'
assert old in s
s=s.replace(old,'E. ${_modeDeliverable(m[0])}',1)

p.write_text(s,encoding='utf-8')
print('PROMPTGPT_V4_1_POLISH=PASS')

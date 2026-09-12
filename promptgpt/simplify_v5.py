from pathlib import Path
import re

p=Path('promptgpt/gemini.html')
s=p.read_text(encoding='utf-8')

# Make mode labels short and obvious anywhere they are shown.
s, n = re.subn(
    r"const MODE_PLAIN=\{.*?\};\nconst ROLE_PLAIN=",
    "const MODE_PLAIN={'Master Build':'完整製作','Expert Audit':'檢查改善','Strategy First':'先規劃','Production Ready':'正式完成','Optimization':'優化','Research Backed':'查資料','Rapid MVP':'簡單測試版','A/B Experiment':'比較兩版','Reverse Engineer':'拆解參考','Decision Framework':'比較選擇','Troubleshoot':'修復問題','SOP System':'整理流程'};\nconst ROLE_PLAIN=",
    s, count=1, flags=re.S)
assert n == 1, f'MODE_PLAIN patch failed: {n}'

NEW_BLOCK = r'''function _shortFocus(v){let x=_plainFocus(v);const exact={
'品牌網站的頁面和內容安排':'品牌網站','令更多人查詢或購買的單頁網站':'單頁宣傳網站','網上訂閱軟件首頁的內容和賣點':'軟件首頁','活動／新產品發布頁':'活動／新品頁','重新設計網站並安全搬資料':'網站改版搬遷','新用戶第一次使用教學':'新手教學','數據主頁要顯示甚麼和怎樣排列':'數據主頁','統一整個產品的介面設計規則':'介面設計規則','手機版選單和頁面導覽':'手機選單','整理網站畫面程式的結構':'網站前端結構','安排網站頁面和功能的程式結構':'網站頁面程式','令網站在手機、平板和電腦都好用':'手機／電腦適配','令更多人包括殘障人士都能使用網站':'無障礙網站','設計系統之間交換資料的接口':'系統資料接口','登入和身份驗證系統':'登入系統','設定不同角色可以看甚麼、做甚麼':'用戶權限','在背景自動執行耗時工作':'背景自動任務','收到其他服務通知後自動處理':'外部服務通知','用快取加快網站和減少伺服器負擔':'網站快取','限制 API 使用次數，避免被濫用':'API 使用限制','找出伺服器 500 錯誤原因':'伺服器 500 錯誤','找出程式愈用愈食記憶體的問題':'記憶體問題','修正多個程序同時運行造成的錯誤':'同時運行錯誤','其他外部服務連接失效時怎樣處理':'外部服務連接','找出不是每次都出現的程式錯誤':'間歇性程式錯誤','檢查準備合併的程式改動':'程式改動檢查','整理舊程式，令它更安全易改':'舊程式整理','增加自動測試，避免改壞功能':'自動測試','每次更新程式後自動測試和部署':'自動測試部署','把程式包成容易在不同電腦運行的版本':'跨電腦運行版本','安全管理 API Key 和不同環境設定':'API Key／環境設定','監察網站狀態、錯誤和效能':'網站監察','新版本出問題時快速退回舊版本':'版本回復','正式網站出故障時的處理流程':'網站故障處理','用 Google／Apple 等帳號登入':'Google／Apple 登入','接收並處理其他服務傳來的通知':'外部服務通知','做一套方便其他程式連接你服務的開發工具':'API 連接工具','失敗後安全重試，而且不會重複做同一件事':'安全重試','設計資料庫要存甚麼和怎樣連結':'資料庫結構','令資料庫查詢更快':'資料庫速度','安全修改資料庫結構':'資料庫修改','限制每個用戶只可看到自己的資料':'資料權限','規劃 iPhone App 的程式結構':'iPhone App 結構','規劃 Android App 的程式結構':'Android App 結構','用一套程式同時做 iPhone 和 Android App':'跨平台 App','令手機 App 更快更順':'App 速度','讓一個 AI 助手懂得使用多種工具':'AI 助手工具','讓多個 AI 助手分工合作':'多個 AI 助手合作','讓 AI 助手記住需要的資料':'AI 助手記憶','讓 AI 自動選擇和使用工具':'AI 自動用工具','重要步驟由真人確認後 AI 才繼續':'真人確認 AI 步驟','測試 AI 助手做得準不準':'AI 助手測試','安排 AI 完成多步驟長任務':'AI 長任務','設定 AI 最基本的角色和規則':'AI 基本規則','要求 AI 用固定格式輸出':'固定格式輸出','用幾個例子教 AI 跟你想要的方式做':'用例子教 AI','縮短 AI 指令但保留重要要求':'縮短 AI 指令','限制 AI 不應做甚麼':'AI 安全限制','同一份 AI 指令支援多種語言':'多語言 AI 指令','給 AI Agent 使用的指令':'AI 助手指令','測試一份 AI 指令好不好用':'AI 指令測試','找出最值得服務的理想客戶':'理想客戶','先用簡單介紹頁測試有沒有人有興趣':'簡單介紹頁測試','先用人工方式提供服務，驗證有人願意用':'人工 MVP 測試','寫清楚產品功能要做甚麼':'產品功能說明','決定產品功能先做哪一些':'功能優先次序','找出最重要的產品成功指標':'主要成功指標','計清楚每個客戶實際賺不賺錢':'每客戶盈利','主動聯絡未認識你的潛在客戶':'陌生客戶開發','第一次了解客戶需要的銷售對話':'了解客戶需要','給客戶的正式合作方案':'客戶合作方案','產品推出市場的完整計劃':'產品推出計劃','一次宣傳活動的整體計劃':'宣傳活動計劃','把客戶分成不同類型':'客戶分類','決定用哪些宣傳渠道':'宣傳渠道','用免費內容或工具吸引潛在客戶':'吸客免費內容','讓舊客戶介紹新客戶的計劃':'客戶轉介計劃','用數據主頁追蹤宣傳效果':'宣傳數據','改善按鈕和行動提示，令更多人願意下一步':'按鈕／行動提示','給用戶／創作者拍內容的清楚要求':'創作者拍攝要求','整理一組相關搜尋關鍵字':'搜尋關鍵字','判斷搜尋者真正想找甚麼':'搜尋意圖','處理影響 Google 收錄的網站技術問題':'Google 收錄問題','讓內容更容易被 AI 搜尋答案引用':'AI 搜尋曝光','新訂閱者加入後的一連串 Email':'新客歡迎 Email','追回放棄購物車的客人':'追回棄單客戶','用一連串內容慢慢把潛在客戶變成客戶':'潛客培育','付款、註冊等系統通知 Email':'系統通知 Email','比較兩個 Email 版本哪個效果更好':'Email 版本比較','把多件商品組合一起賣':'商品套裝','推薦客戶順便買相關商品':'相關商品推薦','規定客服要在幾耐內回覆和解決':'客服回覆時限','測試真人用產品時哪裏卡住':'產品易用度測試','了解用戶真正想完成甚麼事情':'用戶真正需要','訪問離開的客戶，找出為甚麼不用了':'流失客戶訪問','在正式開發前測試一個概念是否吸引':'概念測試','定清楚品牌在客戶心目中代表甚麼':'品牌定位','整理品牌最重要的訊息和賣點':'品牌核心訊息','日常工作固定步驟':'日常工作流程','統一面試評分表':'面試評分表','比較和評估求職者':'求職者評估','用 STAR 方法整理面試例子':'STAR 面試例子','找出客戶流程在哪一步流失':'客戶流失步驟','比較不同時間加入的用戶表現':'不同批次用戶表現','把複雜數據整理成管理層看得懂的重點':'管理層數據重點','定出清楚可研究的問題':'研究問題','整理和比較已有研究':'文獻整理','把論點和證據一步步建立起來':'論點和證據','分析一個說法的優點、問題和證據':'批判分析','改善用字但保持自然':'自然改善用字','用來說服投資者／客戶的提案簡報':'提案簡報','給管理層看的簡短進度簡報':'管理層進度簡報','向投資者講清楚產品故事':'投資者故事','重寫影片令觀眾更願意看下去':'提升影片留存','玩家不停重複的主要玩法':'遊戲主要玩法','遊戲內金錢和資源系統':'遊戲經濟','玩家升級和解鎖進度':'升級解鎖','調整遊戲數值令不同玩法更公平':'遊戲平衡','最突出產品的主視覺照片':'產品主視覺','吸引人下載 App 的廣告':'App 下載廣告','吸引潛在客戶留下資料的廣告':'收集客戶資料廣告','再次吸引看過產品的人回來的廣告':'再營銷廣告','像真照片的 3D 圖':'寫實 3D 圖','30 秒廣告的逐鏡頭安排':'30 秒廣告分鏡','產品示範片的逐鏡頭安排':'產品示範分鏡','動作場面的逐鏡頭安排':'動作場面分鏡','App Store 產品介紹截圖':'App Store 截圖'};if(exact[x])return exact[x];x=x.replace(/^幫你/,'').replace(/^找出/,'').replace(/^檢查和改善/,'改善').replace(/^整理和比較/,'整理').replace(/^用數據主頁/,'數據主頁').replace(/的內容和賣點/g,'').replace(/的完整內容/g,'').replace(/的完整計劃/g,'計劃').replace(/怎樣處理/g,'處理').replace(/怎樣介紹/g,'介紹').replace(/是否自然準確/g,'').trim();return x}
function _simpleMode(v){const x={'Master Build':'完整製作','Expert Audit':'檢查改善','Strategy First':'先規劃','Production Ready':'正式版','Optimization':'優化','Research Backed':'查資料','Rapid MVP':'簡單版','A/B Experiment':'比較兩版','Reverse Engineer':'拆解參考','Decision Framework':'幫你揀','Troubleshoot':'修復問題','SOP System':'整理流程'};return x[v]||_modeLabel(v)}
function _friendlyTitle(category,focus,mode){return `${_shortFocus(focus)} · ${_simpleMode(mode)}`}
function makePrompt(ci,fi,mi,idNum){const c=C[ci],m=M[mi],focus=c[5][fi],plain=_plainFocus(focus),task=_shortFocus(focus),visual=c[4]==='visual',id='P'+String(idNum).padStart(4,'0'),mode=_simpleMode(m[0]),role=_rolePlain(c[3]);const vars=visual?'{主體／產品}、{用途／平台}、{畫面比例}、{想要的風格}、{一定要出現}、{一定不要出現}、{光線／時間}、{參考元素}':'{目標}、{給誰用／目標客戶}、{現有資料／目前情況}、{限制}、{成功標準}、{語氣／品牌}、{想收到的格式}、{時間／人手／預算}';const truth=visual?'不要捏造不存在的品牌資料、產品細節或文字；不知道的地方留成可替換欄位。':'不要把估計當成事實；資料不足要標示假設，依賴外部資料的部分要指出需要查證。';const special=visual?'把主體、構圖、鏡頭、材質、光線、顏色、背景、留白和平台比例講清楚。':'不要只講原則；能直接交文案、步驟、表格、規格、程式碼或決定，就直接給可用版本。';return{id,ci,mi,fi,type:visual?'visual':'text',quality:96,title:_friendlyTitle(c[0],focus,m[0]),desc:`${task}｜${mode}`,models:visual?'Gemini / ImageGen / Midjourney':'ChatGPT / Gemini / Claude',tags:[_catLabel(c[0]),task,mode,visual?'圖片／影片':'文字／工作'],prompt:`請你以${role}的標準，幫我處理「${task}」。

請用簡單、直接的中文。真的需要專業詞時，第一次出現用括號簡單解釋。

【我會提供】
${vars}

【你要做】
- ${_modeGoal(m[0])}
- 先確認我真正想要的結果，以及怎樣才算成功。
- 要特別留意：${_plainScope(c[0],c[2])}
- ${special}
- ${truth}

如果資料不足：最多只問 3 個真正重要的問題；不影響大方向的資料，可以寫明假設後繼續。

【請交給我】
1. 完整可直接使用的成品，不要只給大綱。
2. 最重要的做法和理由。
3. 主要風險／容易出錯的地方，以及怎樣避免。
4. 完成前自行檢查：準確、完整、前後一致、真的做得到，而且沒有把假設當事實。
5. 最值得立即做的下一步。

【要求】
- 具體，不要空泛或重複。
- 有明顯更好的第二種做法時才提供替代方案，並簡單說明何時選它。
- 不要捏造資料，不要照抄特定作品。
- 保留必要限制、輸出格式和驗收標準。
- 自評低於 92/100 時，先自行修正再交出最後版本。`}}
function _quality(p){let q=84;if(p.prompt.includes('【請交給我】'))q+=4;if(p.prompt.includes('主要風險'))q+=3;if(p.prompt.includes('完成前自行檢查'))q+=3;if(p.prompt.includes('不要把估計當成事實')||p.prompt.includes('不要捏造不存在'))q+=2;if(p.prompt.includes('替代方案'))q+=1;return Math.min(q,100)}
function curateLibrary'''

pattern=r"function _friendlyTitle\(category,focus,mode\)\{.*?\}\nfunction makePrompt\(ci,fi,mi,idNum\)\{.*?\}\nfunction _quality\(p\)\{.*?\}\nfunction curateLibrary"
s, n = re.subn(pattern, NEW_BLOCK, s, count=1, flags=re.S)
assert n == 1, f'title/makePrompt patch failed: {n}'

# Hide internal/technical category names from visible UI.
s=s.replace("${esc(C[p.ci][0])}</span>", "${esc(_catLabel(C[p.ci][0]))}</span>")
s=s.replace("${c[0]}</span><em>${categoryCounts[i]}", "${_catLabel(c[0])}</span><em>${categoryCounts[i]}")
s=re.sub(r"\$\('#dmeta'\)\.textContent=`\$\{current\.id\} · \$\{C\[current\.ci\]\[0\]\} · \$\{M\[current\.mi\]\[0\]\}`;", "$('#dmeta').textContent=`${current.id} · ${_catLabel(C[current.ci][0])}`;", s, count=1)

# Make the home copy shorter too.
s=s.replace('直接講你真正想完成嘅工作。打字時即時搜尋；撳 ↑ 後由 Gemini 理解意圖，再重新排序最適合嘅 Prompt。','講你想做咩，PromptGPT 會直接幫你搵最適合嘅 Prompt。')
s=s.replace('PromptGPT · 專業 Prompt，用人話寫 · AI 專屬改寫','PromptGPT · 簡單、直接、可即用')

p.write_text(s,encoding='utf-8')
print('PROMPTGPT_V5_SIMPLIFY=PASS')

# -*- coding: utf-8 -*-
"""
第二單元《千變萬化的植物》HTML 內容模組
"""

CONTENT_HTML = """
  <!-- 分頁 1: 單元導讀與核心概念總覽 -->
  <div id="tab-intro" class="tab-pane active">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">🌿 單元導讀：千變萬化的植物（翰林五上第二單元）</h2>
        <span class="tb-badge">108 課綱核心素養導向</span>
      </div>
      <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
        地球上生活著形形色色的植物，從海邊烈日泥灘、狂風冷冽的高山、平靜水域到校園林蔭，植物如何演化出驚人的形態與構造來適應不同的環境？
        本單元將帶領五年級學生走進植物的奇妙王國，深入探討<strong>植物適應環境的特化構造</strong>、<strong>水分在植物體內的運輸與蒸散調節</strong>、<strong>花朵授粉受精與種子傳播繁衍的絕技</strong>，以及運用<strong>科學二分法</strong>為千變萬化的植物進行精準分類！
      </p>

      <div class="grid-4" style="margin-top: 24px;">
        <div class="info-card" onclick="switchTab('tab-2-1')" style="cursor: pointer;">
          <div class="info-card-header">
            <div class="info-card-icon">🌊</div>
            <div class="info-card-title">2-1 不同環境的植物</div>
          </div>
          <p>探索海邊海茄苳呼吸根、高山玉山杜鵑厚蠟葉、水生布袋蓮膨大氣室葉柄與校園植物的生存智慧。</p>
          <div class="tag-list">
            <span class="tag-item">海邊植物</span>
            <span class="tag-item">高山植物</span>
            <span class="tag-item">水生植物</span>
          </div>
        </div>

        <div class="info-card" onclick="switchTab('tab-2-2')" style="cursor: pointer;">
          <div class="info-card-header">
            <div class="info-card-icon">💧</div>
            <div class="info-card-title">2-2 植物存活的本事</div>
          </div>
          <p>透視紅墨水芹菜水分運輸實驗！深入木質部導管、葉脈輸送、葉片氣孔開閉調節與蒸散作用拉力。</p>
          <div class="tag-list">
            <span class="tag-item">水分運輸</span>
            <span class="tag-item">木質部導管</span>
            <span class="tag-item">氣孔與蒸散</span>
          </div>
        </div>

        <div class="info-card" onclick="switchTab('tab-2-3')" style="cursor: pointer;">
          <div class="info-card-header">
            <div class="info-card-icon">🌸</div>
            <div class="info-card-title">2-3 植物繁衍大顯身手</div>
          </div>
          <p>花朵構造解剖（花萼、花瓣、雄蕊、雌蕊）、子房發育成果實與胚珠變種子；風彈水動四種子傳播與根莖葉營養繁殖。</p>
          <div class="tag-list">
            <span class="tag-item">花朵解剖</span>
            <span class="tag-item">種子傳播</span>
            <span class="tag-item">營養器官繁殖</span>
          </div>
        </div>

        <div class="info-card" onclick="switchTab('tab-2-4')" style="cursor: pointer;">
          <div class="info-card-header">
            <div class="info-card-icon">🔍</div>
            <div class="info-card-title">2-4 植物的特徵與分類</div>
          </div>
          <p>實戰演練二分法分類樹！比較開花植物與蕨類植物（孢子囊群、捲旋幼葉），認識臺灣蕨類王國與分類學。</p>
          <div class="tag-list">
            <span class="tag-item">二分法</span>
            <span class="tag-item">開花植物</span>
            <span class="tag-item">蕨類孢子</span>
          </div>
        </div>
      </div>

      <!-- 昨晚新發布微課焦點卡片 -->
      <div class="info-card" style="margin-top: 24px; border: 2px solid #fbbf24; background: rgba(30, 27, 7, 0.65);">
        <div class="info-card-header">
          <div class="info-card-icon">🌟</div>
          <div class="info-card-title" style="color: #fbbf24;">最新整合：2-3 金桔授粉結果微課 ＆ Google Flow AI 影片提示詞庫</div>
          <span class="tb-badge" style="background: #f59e0b; color: #000;">HOT 最新整合</span>
        </div>
        <p style="color: #fef3c7;">
          專為翰林版五上自然單元二研發之互動微課已全面整併！包含<strong>金桔花剖面蜜蜂傳粉動畫</strong>、<strong>子房膨大變成金桔生長縮時</strong>、<strong>種子四大傳播方式</strong>、<strong>Google Flow 3D 影片提示詞</strong>與<strong>NotebookLM 探究家教系統</strong>。
        </p>
        <div style="display: flex; gap: 12px; margin-top: 14px; flex-wrap: wrap;">
          <button class="btn-ctrl active" onclick="switchTab('tab-kumquat')">🍊 開啟金桔授粉結果微課</button>
          <button class="btn-ctrl" onclick="switchTab('tab-flow-prompt')">🎬 瀏覽 AI 影片提示詞庫</button>
          <a href="plant-learning-site.html" target="_blank" class="link-pill-btn">🌸 獨立微課全螢幕開啟 ↗</a>
          <a href="flower-fruit-animation.html" target="_blank" class="link-pill-btn" style="border-color:#38bdf8; color:#38bdf8;">🐝 授粉結果動畫 ↗</a>
        </div>
      </div>

      <div class="highlight-box" style="margin-top: 26px;">
        <h4>💡 108 課綱自然科學探究指引（學習表現與學習內容）</h4>
        <p>
          • <strong>INb-Ⅲ-1</strong>：動植物具有維持生命、生長、發育、生殖及適應環境的構造與功能。<br>
          • <strong>INb-Ⅲ-2</strong>：環境改變會影響動植物的生存，動植物發展出特殊構造以適應其生活環境。<br>
          • <strong>INe-Ⅲ-4</strong>：生物可以依外觀形態或生理特徵依據科學原則進行分類（如二分法）。
        </p>
      </div>
    </div>
  </div>

  <!-- 分頁 2: 2-1 不同環境的植物 -->
  <div id="tab-2-1" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">🌊 2-1 不同環境的植物（課本 p.42～49）</h2>
        <span class="tb-badge">形態與環境適應</span>
      </div>

      <!-- Canvas 模擬器 1 -->
      <div class="sim-container">
        <div class="sim-toolbar">
          <div class="sim-title">
            <span>🔬 極端環境植物特化構造微觀探索器</span>
          </div>
          <div class="sim-controls">
            <button class="btn-ctrl active" onclick="setAdaptPlant('mangrove')">🌴 海茄苳（海邊呼吸根）</button>
            <button class="btn-ctrl" onclick="setAdaptPlant('rhododendron')">🏔️ 玉山杜鵑（高山耐寒蠟葉）</button>
            <button class="btn-ctrl" onclick="setAdaptPlant('hyacinth')">💧 布袋蓮（水生氣室葉柄）</button>
            <button class="btn-ctrl" onclick="setAdaptPlant('casuarina')">🌲 木麻黃（退化齒葉板根）</button>
          </div>
        </div>

        <div class="sim-canvas-box">
          <canvas id="canvas-adapt" class="interactive-canvas"></canvas>
          <div id="adapt-info-overlay" class="sim-overlay-info">
            <h5 id="adapt-plant-title">海茄苳（Avicennia marina）</h5>
            <p id="adapt-plant-desc">生長在潮間帶泥灘，缺氧且高鹽分。土壤下的地下根會向上長出無數「棒狀呼吸根」，露出泥面進行氣體交換；葉背具有泌鹽腺體排出體內過多鹽分！</p>
          </div>
        </div>

        <div class="ctrl-panel">
          <div class="ctrl-item">
            <label id="adapt-slider-label">🌊 潮汐水位高度：</label>
            <input type="range" id="adapt-env-slider" min="10" max="90" value="50" oninput="updateAdaptEnv(this.value)">
            <span class="ctrl-val" id="adapt-env-val">50%</span>
          </div>
          <div style="font-size: 0.88rem; color: var(--text-dim);">
            👉 提示：拖曳滑桿改變環境因子，觀察植物特化構造如何保護自己生存！
          </div>
        </div>
      </div>

      <!-- 教材圖解解析卡片 -->
      <div class="grid-2">
        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🌊</div>
            <div class="info-card-title">海邊環境植物的生存絕技</div>
          </div>
          <p>• <strong>強光、強風、高鹽分、沙地缺水保水難</strong>是海邊植物面臨的嚴峻考驗。</p>
          <p>• <strong>海茄苳</strong>：生長在海邊潮間帶泥灘地，泥中缺氧，會長出向上直立的<strong>指狀呼吸根（氣生根）</strong>；葉片背面有排鹽孔，能分泌鹽分結晶。</p>
          <p>• <strong>濱水菜 / 馬鞍藤</strong>：具有肥厚肉質葉片，能大量儲存水分，表面有角質層減少水分蒸散。</p>
          <p>• <strong>木麻黃</strong>：具有深廣發達的根系與板根抓牢沙地；綠色小枝代替葉行光合作用，真正的葉退化成圍繞小枝節上的<strong>微小齒狀輪生葉</strong>，大幅減少水分散失抗乾旱！</p>
        </div>

        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🏔️</div>
            <div class="info-card-title">高山環境植物的生存智慧</div>
          </div>
          <p>• <strong>氣溫極低、強烈紫外線、狂風呼嘯、冬季積雪結凍</strong>是臺灣三千公尺以上高山的嚴苛條件。</p>
          <p>• <strong>玉山薄雪草</strong>：全株密被<strong>緊密的白色綿毛</strong>，宛如穿著保暖防寒大衣，能禦寒保溫並反射強烈紫外線，避免曬傷凍傷。</p>
          <p>• <strong>玉山杜鵑</strong>：植株低矮匍匐、木質莖堅韌彎曲緊貼岩石，可躲避強風吹襲；葉片呈厚革質，表面覆有厚厚蠟質，冬天還會向內捲縮以減少水分蒸發。</p>
          <p>• <strong>玉山圓柏</strong>：生長在高山風口處，受強勁山風長年雕琢，樹幹盤曲匍匐貼近地面，宛如天然高山盆景。</p>
        </div>
      </div>

      <div class="grid-2" style="margin-top: 20px;">
        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">💧</div>
            <div class="info-card-title">水生環境植物的浮力與換氣</div>
          </div>
          <p>• <strong>布袋蓮</strong>：葉柄呈現<strong>膨大海綿狀組織</strong>，切開內部有成千上萬個充滿空氣的<strong>氣室</strong>，能提供巨大的浮力使植株漂浮在水面上，並儲存氧氣供根部呼吸。</p>
          <p>• <strong>大萍（水芙蓉）</strong>：葉片表面密布<strong>細小防水纖毛</strong>，使水滴無法附著形成美麗的滾動水珠，同時能抓住空氣泡泡維持葉片漂浮與呼吸。</p>
          <p>• <strong>蓮（荷花）與睡蓮</strong>：地下莖（蓮藕）與長長的葉柄內部具有連通的大型通氣管道，直通水底泥中輸送新鮮空氣。</p>
        </div>

        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🏫</div>
            <div class="info-card-title">校園常見植物與爭取陽光</div>
          </div>
          <p>• <strong>榕樹</strong>：枝幹會垂下無數細長的<strong>氣生根</strong>，接觸地面深入泥土後會吸收水分養分並逐漸木質化加粗，形成支撐巨大樹冠的<strong>支持根</strong>！</p>
        </div>
      </div>

      <!-- YouTube 實境影音觀察教室（點了就看） -->
      <div style="margin-top: 26px;">
        <div class="tb-header" style="border-bottom: 2px solid rgba(56, 189, 248, 0.3); margin-bottom: 18px;">
          <h3 style="color: #38bdf8; font-size: 1.35rem; display: flex; align-items: center; gap: 10px;">
            <span>🎬 實境影音觀察教室：海邊與高山植物（已全面驗證・點了就看）</span>
          </h3>
          <span class="tb-badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; border-color: #38bdf8;">YouTube 實境生態教學</span>
        </div>

        <div class="grid-3">
          <!-- 海邊影片 1: 大蔚阿昌 海茄苳 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('Ct3AsJ20upY', '［認識植物好好玩］海茄苳（呼吸根與耐鹽構造）', '彰化芳苑海邊潮間帶海空步道實景觀察，棒狀指狀呼吸根向上伸出泥灘吸氧，葉背排鹽腺排出鹽分結晶')">
              <img class="video-thumb" src="https://img.youtube.com/vi/Ct3AsJ20upY/hqdefault.jpg" alt="海茄苳介紹" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag coastal">🌊 海邊植物 • 呼吸根與排鹽</span>
                <h4 class="video-title">［認識植物好好玩］海茄苳介紹</h4>
                <p class="video-desc">深入彰化芳苑潮間帶，特寫海茄苳密集的「棒狀呼吸根」如何露出缺氧泥灘進行氣體交換，以及葉片分泌白色鹽粒的耐鹽機制！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('Ct3AsJ20upY', '［認識植物好好玩］海茄苳介紹', '彰化芳苑海邊潮間帶海空步道實景觀察，棒狀指狀呼吸根向上伸出泥灘吸氧，葉背排鹽腺排出鹽分結晶')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=Ct3AsJ20upY" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 海邊影片 2: 臺南億載國小 行動學習海茄苳 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('OdL6idq8w9U', '億載國小 in 四草紅樹林行動學習：海茄苳實地探究', '國小學童實地走訪四草紅樹林，近距離觀察海茄苳呼吸根群與潮間帶生態')">
              <img class="video-thumb" src="https://img.youtube.com/vi/OdL6idq8w9U/hqdefault.jpg" alt="億載國小海茄苳" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag coastal">🌊 海邊植物 • 國小戶外教學</span>
                <h4 class="video-title">四草紅樹林行動學習：海茄苳</h4>
                <p class="video-desc">國小師生實地深入臺南四草濕地，以學童視角親自解說海茄苳如何在泥濘缺氧的環境長出呼吸根，非常貼合課本教材！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('OdL6idq8w9U', '四草紅樹林行動學習：海茄苳', '國小學童實地走訪四草紅樹林，近距離觀察海茄苳呼吸根群與潮間帶生態')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=OdL6idq8w9U" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 海邊影片 3: 自然教室 海茄苳地下氣根 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('-xALE2w9liU', '我的自然教室：海茄苳的地下氣根與呼吸根特寫', '特寫海茄苳地下根向上鑽出泥面的指狀呼吸根，觀察其海綿氣孔組織')">
              <img class="video-thumb" src="https://img.youtube.com/vi/-xALE2w9liU/hqdefault.jpg" alt="海茄苳地下氣根" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag coastal">🌊 海邊植物 • 微觀特寫</span>
                <h4 class="video-title">海茄苳地下氣根與呼吸根特寫</h4>
                <p class="video-desc">超清晰特寫鏡頭！清楚記錄海茄苳主幹周圍密密麻麻如手指般的呼吸根，說明其如何幫助植物在漲退潮泥灘中維持呼吸。</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('-xALE2w9liU', '海茄苳地下氣根與呼吸根特寫', '特寫海茄苳地下根向上鑽出泥面的指狀呼吸根，觀察其海綿氣孔組織')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=-xALE2w9liU" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 高山影片 1: 臺灣山林復育協會 玉山杜鵑 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('mNS4PZk24xk', '合歡山生態之旅：玉山杜鵑生存特化解析', '專業學者解說合歡山高山強風低溫環境下，玉山杜鵑如何匍匐低矮、厚革質葉與厚蠟質表面抗紫外線與禦寒')">
              <img class="video-thumb" src="https://img.youtube.com/vi/mNS4PZk24xk/hqdefault.jpg" alt="玉山杜鵑生態解說" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag alpine">🏔️ 高山植物 • 生態特化</span>
                <h4 class="video-title">合歡山生態之旅：玉山杜鵑</h4>
                <p class="video-desc">臺灣山林復育協會專業解說：合歡山海拔三千公尺強風帶，玉山杜鵑如何演化出矮小匍匐灌叢、厚革質葉片禦寒抗曬的生理特徵！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('mNS4PZk24xk', '合歡山生態之旅：玉山杜鵑', '專業學者解說合歡山高山強風低溫環境下，玉山杜鵑如何匍匐低矮、厚革質葉與厚蠟質表面抗紫外線與禦寒')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=mNS4PZk24xk" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 高山影片 2: 皮超丘 玉山頂開花的玉山薄雪草 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('YeL0KrYlnr8', '在零下十度的玉山頂，有東西正在開花：玉山薄雪草', '玉山主峰頂極端環境拍攝，特寫玉山薄雪草全身白絨毛禦寒大衣與冰河孑遺演化')">
              <img class="video-thumb" src="https://img.youtube.com/vi/YeL0KrYlnr8/hqdefault.jpg" alt="玉山薄雪草開花" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag alpine">🏔️ 高山植物 • 白絨毛禦寒</span>
                <h4 class="video-title">零下十度的玉山頂：玉山薄雪草</h4>
                <p class="video-desc">在臺灣最高峰玉山頂拍攝！直擊冰河時期孑遺至今的「玉山薄雪草」，全身覆蓋如羊毛般的緻密白綿毛，能保暖並反射強烈紫外線。</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('YeL0KrYlnr8', '零下十度的玉山頂：玉山薄雪草', '玉山主峰頂極端環境拍攝，特寫玉山薄雪草全身白絨毛禦寒大衣與冰河孑遺演化')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=YeL0KrYlnr8" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 高山影片 3: 太魯閣國家公園 合歡山高山生態精華 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('9adgWPxGpFw', '太魯閣國家公園官方：合歡山高山生態之旅精華', '國家公園官方高畫質生態紀錄，完整呈現高山寒原植物群落、玉山圓柏與玉山杜鵑適應環境')">
              <img class="video-thumb" src="https://img.youtube.com/vi/9adgWPxGpFw/hqdefault.jpg" alt="太魯閣高山生態" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag alpine">🏔️ 高山植物 • 國家公園官方</span>
                <h4 class="video-title">太魯閣官方：合歡高山植物生態</h4>
                <p class="video-desc">太魯閣國家公園官方製作！空拍與高畫質微觀合歡山高山寒原，展現玉山杜鵑、玉山圓柏等植物如何對抗狂風與酷寒，畫面極為震撼！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('9adgWPxGpFw', '太魯閣官方：合歡高山植物生態', '國家公園官方高畫質生態紀錄，完整呈現高山寒原植物群落、玉山圓柏與玉山杜鵑適應環境')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=9adgWPxGpFw" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 分頁 3: 2-2 植物存活的本事 -->
  <div id="tab-2-2" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">💧 2-2 植物存活的本事（課本 p.50～55）</h2>
        <span class="tb-badge">水分運輸與蒸散作用</span>
      </div>

      <!-- Canvas 模擬器 2 -->
      <div class="sim-container">
        <div class="sim-toolbar">
          <div class="sim-title">
            <span>🔬 植物體內水分運輸與氣孔蒸散動態實驗室</span>
          </div>
          <div class="sim-controls">
            <button class="btn-ctrl active" id="btn-view-stem" onclick="switchTransportView('stem')">🌱 芹菜紅墨水水分運輸動態</button>
            <button class="btn-ctrl" id="btn-view-cross" onclick="switchTransportView('cross')">🔬 莖的橫切面與縱切面剖視</button>
            <button class="btn-ctrl" id="btn-view-stoma" onclick="switchTransportView('stoma')">🍃 氣孔保衛細胞顯微開閉</button>
          </div>
        </div>

        <div class="sim-canvas-box">
          <canvas id="canvas-transport" class="interactive-canvas"></canvas>
          <div id="transport-info-overlay" class="sim-overlay-info">
            <h5 id="trans-title">紅墨水水分輸送進行中</h5>
            <p id="trans-desc">根與切口吸入紅墨水溶液，水分子沿著莖內的「木質部導管」一路向上輸送，經過葉柄直達葉片與葉脈！</p>
          </div>
        </div>

        <div class="ctrl-panel">
          <div class="ctrl-item" id="trans-ctrl-speed">
            <label>⚡ 水分輸送速率 / 日照強度：</label>
            <input type="range" id="trans-speed-slider" min="1" max="5" value="3" oninput="updateTransSpeed(this.value)">
            <span class="ctrl-val" id="trans-speed-val">3x</span>
          </div>
          <div class="ctrl-item" id="trans-ctrl-stoma" style="display:none;">
            <label>☀️ 環境光照與保衛細胞含水量：</label>
            <input type="range" id="stoma-slider" min="0" max="100" value="70" oninput="updateStomaState(this.value)">
            <span class="ctrl-val" id="stoma-slider-val">70% (開啟)</span>
          </div>
        </div>
      </div>

      <!-- 知識要點卡片 -->
      <div class="grid-3">
        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🧪</div>
            <div class="info-card-title">課本核心實驗：紅墨水染色探究</div>
          </div>
          <p>• <strong>實驗材料</strong>：帶有葉片的芹菜或白色花朵、透明量筒/燒杯、紅色食用色素水、油泥或保鮮膜。</p>
          <p>• <strong>對照操作</strong>：燒杯瓶口塞入<strong>油泥或滴一層食用油</strong>，目的是<strong>防止杯中水分直接蒸發到空氣中</strong>，確保量筒液面下降完全是由植物吸收所致！</p>
          <p>• <strong>實驗觀察</strong>：數小時後，白色花瓣邊緣變紅，芹菜葉脈明顯染紅，液面刻度下降。</p>
        </div>

        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🔍</div>
            <div class="info-card-title">莖的剖面微觀構造（導管分佈）</div>
          </div>
          <p>• <strong>橫切面</strong>：用美工刀將莖橫向切斷，在放大鏡下可看見許多<strong>紅色細小斑點</strong>，這些小紅點就是專門運送水分與無機鹽的<strong>木質部導管維管束</strong>。</p>
          <p>• <strong>縱切面</strong>：將莖縱向剖開，會看到一條條<strong>長長的紅色垂直細線條</strong>，證明導管是一根根連通上下、如吸管般的細微管路。</p>
          <p>• <strong>水分流向</strong>：土壤水分 ➔ 根毛 ➔ 根部導管 ➔ 莖部導管 ➔ 葉柄與葉脈 ➔ 葉肉細胞。</p>
        </div>

        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">💨</div>
            <div class="info-card-title">蒸散作用與氣孔開閉調節</div>
          </div>
          <p>• <strong>套袋實驗</strong>：將透明夾鏈袋套在長滿綠葉的枝條上並束緊，數小時後袋內出現<strong>細小水滴</strong>，證明葉片不斷釋放水蒸氣。</p>
          <p>• <strong>氣孔構造</strong>：氣孔主要分布在<strong>葉片背面表皮</strong>，由兩個半月形的<strong>保衛細胞</strong>圍成。</p>
          <p>• <strong>開閉機制</strong>：白天天氣溫和光照充足，保衛細胞吸水膨脹向外彎曲，<strong>氣孔張開</strong>；夜晚或嚴重缺水時，保衛細胞失水萎縮變直，<strong>氣孔閉合</strong>以防乾枯枯萎。</p>
          <p>• <strong>蒸散拉力</strong>：蒸散作用就像抽水機，產生強大的<strong>向上牽引拉力</strong>，帶動幾十公尺高大樹木的水分運輸！</p>
        </div>
      </div>

      <!-- YouTube 實境影音觀察教室：2-2 水分運輸與蒸散作用 -->
      <div style="margin-top: 26px;">
        <div class="tb-header" style="border-bottom: 2px solid rgba(56, 189, 248, 0.3); margin-bottom: 18px;">
          <h3 style="color: #38bdf8; font-size: 1.35rem; display: flex; align-items: center; gap: 10px;">
            <span>🎬 實境影音觀察教室：2-2 水分運輸與蒸散作用（已驗證教材・點了就看）</span>
          </h3>
          <span class="tb-badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; border-color: #38bdf8;">YouTube 實境實驗教學</span>
        </div>

        <div class="grid-3">
          <!-- 2-2 影片 1: 均一教育平台 植物體內水分運輸 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('nEo3ELKd21k', '均一教育平台：植物的水分運輸與實驗', '完整動畫與實物解析：根吸收水分經由木質部導管向上運送到莖與葉，並由氣孔蒸散出去')">
              <img class="video-thumb" src="https://img.youtube.com/vi/nEo3ELKd21k/hqdefault.jpg" alt="植物水分運輸" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag water">💧 2-2 核心觀念 • 均一教育平台</span>
                <h4 class="video-title">植物體內水分的運輸與實驗探究</h4>
                <p class="video-desc">均一專業教學動畫！系統性拆解根毛吸水、木質部導管單向向上輸送，以及葉片蒸散作用帶動水分子鏈的拉力機制。</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('nEo3ELKd21k', '均一教育平台：植物的水分運輸與實驗', '完整動畫與實物解析：根吸收水分經由木質部導管向上運送到莖與葉，並由氣孔蒸散出去')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=nEo3ELKd21k" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 2-2 影片 2: 酷課雲 x 均一 觀察植物的水分運輸構造 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('TSePPZHl1qk', '酷課雲 x 均一：植物體運輸構造的觀察（芹菜實驗）', '芹菜紅墨水染色實驗：瓶口滴油防水分蒸發對照組，切開芹菜莖觀察橫切面紅點與縱切面導管紅線')">
              <img class="video-thumb" src="https://img.youtube.com/vi/TSePPZHl1qk/hqdefault.jpg" alt="芹菜紅墨水實驗" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag water">🧪 課本標準實驗 • 酷課雲 x 均一</span>
                <h4 class="video-title">芹菜紅墨水染色與水分運輸構造觀察</h4>
                <p class="video-desc">完全配合國小五上課本！帶學生動手做芹菜紅墨水實驗，橫剖莖部觀察維管束紅斑點，縱剖觀察導管長紅線，對比鮮明易懂！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('TSePPZHl1qk', '酷課雲 x 均一：植物體運輸構造的觀察（芹菜實驗）', '芹菜紅墨水染色實驗：瓶口滴油防水分蒸發對照組，切開芹菜莖觀察橫切面紅點與縱切面導管紅線')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=TSePPZHl1qk" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 2-2 影片 3: 水怎樣進出植物的身體 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('qqY9YNP4fxI', '五上自然：水怎樣進出植物的身體與氣孔蒸散', '套袋實驗觀察葉片水珠形成，撕取葉背表皮用顯微鏡觀察保衛細胞與氣孔開合')">
              <img class="video-thumb" src="https://img.youtube.com/vi/qqY9YNP4fxI/hqdefault.jpg" alt="水怎樣進出植物" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag water">🍃 葉片蒸散作用 • 氣孔顯微</span>
                <h4 class="video-title">水怎樣進出植物的身體與氣孔觀察</h4>
                <p class="video-desc">透過透明夾鏈袋套袋實驗證實葉片蒸發水分，並利用顯微鏡特寫葉片背面半月形保衛細胞，直擊氣孔張開與閉合！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('qqY9YNP4fxI', '五上自然：水怎樣進出植物的身體與氣孔蒸散', '套袋實驗觀察葉片水珠形成，撕取葉背表皮用顯微鏡觀察保衛細胞與氣孔開合')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=qqY9YNP4fxI" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 分頁 4: 2-3 植物繁衍大顯身手 -->
  <div id="tab-2-3" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">🌸 2-3 植物繁衍大顯身手（課本 p.56～63）</h2>
        <span class="tb-badge">有性生殖與無性繁殖</span>
      </div>

      <!-- 金桔授粉微課快速入口橫幅 -->
      <div class="info-card" style="margin-bottom: 20px; border: 1.5px solid #fbbf24; background: rgba(25, 23, 7, 0.7); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
        <div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 1.4rem;">🍊</span>
            <h3 style="color: #fbbf24; margin: 0; font-size: 1.15rem;">2-3 金桔授粉結果專題微課 ＆ AI 影片提示詞已整合上線！</h3>
          </div>
          <p style="margin: 6px 0 0 0; color: #fde68a; font-size: 0.9rem;">
            支援金桔花剖面、蜜蜂授粉傳粉、子房膨大發育縮時、Google Flow (Veo) 提示詞庫與小學霸闖關測驗。
          </p>
        </div>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <button class="btn-ctrl active" onclick="switchTab('tab-kumquat')">👉 跳轉金桔微課專題</button>
          <button class="btn-ctrl" onclick="switchTab('tab-flow-prompt')">🎬 AI 影片提示詞</button>
          <a href="plant-learning-site.html" target="_blank" class="link-pill-btn">全螢幕開啟 ↗</a>
        </div>
      </div>

      <!-- Canvas 模擬器 3 -->
      <div class="sim-container">
        <div class="sim-toolbar">
          <div class="sim-title">
            <span>🔬 花朵構造解剖、果實發育與種子傳播模擬器</span>
          </div>
          <div class="sim-controls">
            <button class="btn-ctrl active" id="btn-flower-dissect" onclick="switchFlowerMode('dissect')">🌺 花朵解剖與結果演示</button>
            <button class="btn-ctrl" id="btn-seed-spread" onclick="switchFlowerMode('spread')">🚀 種子傳播四大絕招模擬</button>
          </div>
        </div>

        <div class="sim-canvas-box">
          <canvas id="canvas-flower" class="interactive-canvas"></canvas>
          <div id="flower-info-overlay" class="sim-overlay-info">
            <h5 id="fl-title">花朵解剖構造</h5>
            <p id="fl-desc">點擊下方按鈕或構造名稱，進行花朵器官拆解與授粉結果發育！</p>
          </div>
        </div>

        <div class="ctrl-panel">
          <div id="fl-controls-dissect" style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
            <button class="btn-ctrl" onclick="dissectPart('sepal')">1. 移除花萼 (萼片)</button>
            <button class="btn-ctrl" onclick="dissectPart('petal')">2. 移除花瓣 (花冠)</button>
            <button class="btn-ctrl" onclick="dissectPart('stamen')">3. 觀察雄蕊 (花藥/花粉)</button>
            <button class="btn-ctrl" onclick="dissectPart('pistil')">4. 觀察雌蕊 (柱頭/子房)</button>
            <button class="btn-ctrl active" onclick="animatePollination()">✨ 點擊進行【授粉受精發育成果實】！</button>
            <button class="btn-ctrl" onclick="resetFlower()">🔄 重置花朵</button>
          </div>
          <div id="fl-controls-spread" style="display:none; gap:10px; flex-wrap:wrap; align-items:center;">
            <button class="btn-ctrl active" onclick="setSpreadType('wind')">🍃 風力傳播（蒲公英/青楓）</button>
            <button class="btn-ctrl" onclick="setSpreadType('ballistic')">💥 彈力傳播（非洲鳳仙花爆裂）</button>
            <button class="btn-ctrl" onclick="setSpreadType('water')">🌊 水力傳播（椰子海漂）</button>
            <button class="btn-ctrl" onclick="setSpreadType('animal')">🐕 動物傳播（大花咸豐草倒鉤）</button>
            <button class="btn-ctrl active" id="btn-trigger-spread" onclick="triggerSpreadAction()">▶️ 觸發傳播動態！</button>
          </div>
        </div>
      </div>

      <!-- 繁衍知識全景圖 -->
      <div class="grid-2">
        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🌺</div>
            <div class="info-card-title">花朵的四大構造與受精發育</div>
          </div>
          <p>• <strong>花萼</strong>：位於花朵最外層，通常為綠色，在花苞時期緊緊包裹保護內部器官。</p>
          <p>• <strong>花瓣</strong>：通常色彩鮮豔繽紛並散發花香或蜜腺，吸引蜜蜂、蝴蝶等昆蟲前來傳粉。</p>
          <p>• <strong>雄蕊</strong>：由<strong>花絲</strong>支撐頂端的<strong>花藥</strong>，花藥成熟後會裂開釋放出無數金黃色微小<strong>花粉粒</strong>。</p>
          <p>• <strong>雌蕊</strong>：通常位在花朵正中央，包含頂端黏性接受花粉的<strong>柱頭</strong>、細長的<strong>花柱</strong>，以及膨大的<strong>子房</strong>（內含<strong>胚珠</strong>）。</p>
          <div class="highlight-box">
            <h4>💡 國小自然必考發育口訣！</h4>
            <p style="font-weight:700; font-size:1.05rem;">「子房發育成果實，胚珠發育成果實裡的種子！」</p>
          </div>
        </div>

        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🚀</div>
            <div class="info-card-title">種子與果實傳播四大途徑</div>
          </div>
          <p>• <strong>風力傳播</strong>：種子輕巧，具有利於隨風飄浮的附屬物。如<strong>蒲公英</strong>具降落傘狀冠毛；<strong>青楓 / 臺灣赤楊</strong>具雙翅翅果旋轉滑翔；<strong>木棉 / 臺灣欒樹</strong>具輕盈棉絮。</p>
          <p>• <strong>彈力傳播</strong>：成熟果莢乾燥時內外層組織張力不均，受碰觸時瞬間爆裂！如<strong>非洲鳳仙花</strong>、<strong>黃花酢漿草</strong>果實炸裂彈出種子。</p>
          <p>• <strong>水力傳播</strong>：果實具有防水且疏鬆富含氣室的纖維層，比水輕能浮在水面長期漂流不腐爛。如<strong>椰子</strong>、<strong>棋盤腳</strong>、<strong>蓮蓬</strong>。</p>
          <p>• <strong>動物傳播</strong>：<br>
            ① <strong>附著式</strong>：果實具倒鉤刺，掛在動物毛皮或人類衣物上帶走，如<strong>大花咸豐草（鬼針草）</strong>、<strong>蒺藜</strong>。<br>
            ② <strong>食用式</strong>：果實甜美多汁吸引鳥類取食，硬種子不易消化隨糞便排出，如<strong>雀榕</strong>、<strong>番茄</strong>、<strong>芭樂</strong>。
          </p>
        </div>
      </div>

      <!-- 營養器官繁殖卡片 -->
      <div class="info-card" style="margin-top: 20px;">
        <div class="info-card-header">
          <div class="info-card-icon">🌿</div>
          <div class="info-card-title">大顯身手：植物的營養器官繁殖（根、莖、葉）</div>
        </div>
        <div class="grid-3" style="margin-top: 10px;">
          <div>
            <h4 style="color: var(--primary-light); margin-bottom: 6px;">🍃 葉繁殖</h4>
            <p><strong>落地生根</strong>：肉質厚葉片邊緣的凹陷缺刻處，會長出帶有迷你小根的小芽（不定芽），掉落地面就能長成一棵全新植株！<strong>石蓮花</strong>、<strong>大岩桐</strong>也是著名的葉插高手。</p>
          </div>
          <div>
            <h4 style="color: var(--accent-cyan); margin-bottom: 6px;">🎋 莖繁殖</h4>
            <p><strong>甘藷（地瓜藤）</strong>：剪一段匍匐莖插入土壤中即可發根生長！<br><strong>萬年青、黃金葛</strong>：剪取帶節的莖段插入水中水耕即可長出新根。<br><strong>馬鈴薯</strong>：膨大的地下「塊莖」，其表面芽眼可發芽長成新株。</p>
          </div>
          <div>
            <h4 style="color: var(--accent-gold); margin-bottom: 6px;">🥕 根繁殖</h4>
            <p><strong>甘藷（塊根）</strong>：將甘藷塊根泡水或埋入土中，可長出無數新芽與新藤！<br><strong>胡蘿蔔</strong>：切下頂端帶根冠部分泡水，可長出綠葉新芽。<br><strong>大麗菊</strong>也是常見利用塊根繁殖的觀賞花卉。</p>
          </div>
        </div>
      </div>

      <!-- YouTube 實境影音觀察教室：2-3 植物花、果實、種子與繁衍 -->
      <div style="margin-top: 26px;">
        <div class="tb-header" style="border-bottom: 2px solid rgba(251, 191, 36, 0.3); margin-bottom: 18px;">
          <h3 style="color: #fbbf24; font-size: 1.35rem; display: flex; align-items: center; gap: 10px;">
            <span>🎬 實境影音觀察教室：2-3 花朵構造、授粉結果與種子繁衍（點了就看）</span>
          </h3>
          <span class="tb-badge" style="background: rgba(251, 191, 36, 0.2); color: #fbbf24; border-color: #fbbf24;">YouTube 實境生態教學</span>
        </div>

        <div class="grid-3">
          <!-- 2-3 影片 1: 植物花的構造與傳粉作用 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('19n2MAfNcwc', '臺北酷課雲：植物花的構造與傳粉作用', '花萼、花瓣、雄蕊（花藥花絲）與雌蕊（柱頭子房）四大構造解說與昆蟲授粉過程')">
              <img class="video-thumb" src="https://img.youtube.com/vi/19n2MAfNcwc/hqdefault.jpg" alt="花朵構造與授粉" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag flower">🌸 2-3 核心觀念 • 臺北酷課雲</span>
                <h4 class="video-title">植物花的構造與花粉傳粉觀察</h4>
                <p class="video-desc">由外而內清晰拆解花萼、花瓣、雄蕊（花藥花絲）與雌蕊（柱頭子房），解說昆蟲傳粉如何讓花粉落在柱頭完成受粉！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('19n2MAfNcwc', '臺北酷課雲：植物花的構造與傳粉作用', '花萼、花瓣、雄蕊（花藥花絲）與雌蕊（柱頭子房）四大構造解說與昆蟲授粉過程')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=19n2MAfNcwc" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 2-3 影片 2: 花、果實、種子的觀察與形成 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('sZ8h8qjyn_A', '臺北酷課雲：植物的果實與種子發育', '解說花朵授粉受精後子房膨大發育為果實、胚珠發育為種子的完整過程與實物觀察')">
              <img class="video-thumb" src="https://img.youtube.com/vi/sZ8h8qjyn_A/hqdefault.jpg" alt="花果實種子觀察" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag flower">🍊 授粉結果 • 臺北酷課雲</span>
                <h4 class="video-title">花、果實與種子的形成與觀察</h4>
                <p class="video-desc">考試必考核心口訣：「子房發育成果實，胚珠發育成種子」！剖開果實對照種子發育，直觀清晰易懂。</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('sZ8h8qjyn_A', '臺北酷課雲：植物的果實與種子發育', '解說花朵授粉受精後子房膨大發育為果實、胚珠發育為種子的完整過程與實物觀察')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=sZ8h8qjyn_A" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 2-3 影片 3: 植物莖的繁殖與營養器官繁衍 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('lgJLE8xIH80', '臺北酷課雲：植物莖的功能與扦插繁殖', '觀察植物利用營養器官（莖、葉、根）繁殖的奧秘，包含甘藷扦插與落地生根葉緣不定芽')">
              <img class="video-thumb" src="https://img.youtube.com/vi/lgJLE8xIH80/hqdefault.jpg" alt="植物特徵與繁衍" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag flower">🌿 營養器官繁殖 • 臺北酷課雲</span>
                <h4 class="video-title">植物莖的繁殖功能與營養器官繁衍</h4>
                <p class="video-desc">直擊植物營養器官繁衍的奧秘！包含甘藷匍匐莖扦插、落地生根厚葉片缺刻不定芽以及馬鈴薯地下塊莖發芽等無性生殖！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('lgJLE8xIH80', '臺北酷課雲：植物莖的功能與扦插繁殖', '觀察植物利用營養器官（莖、葉、根）繁殖的奧秘，包含甘藷扦插與落地生根葉緣不定芽')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=lgJLE8xIH80" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 分頁: 2-3 金桔開花、蜜蜂授粉與結果微課 -->
  <div id="tab-kumquat" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">🍊 2-3 金桔開花、授粉與果實發育微課（課本 p.54～57）</h2>
        <span class="tb-badge">高互動微課系統</span>
      </div>

      <!-- 操作頂部工具列與獨立開啟連結 -->
      <div class="info-card" style="margin-bottom: 18px; border: 1px solid var(--border-glow); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 1.5rem;">🌿</span>
          <div>
            <div style="font-weight: 700; color: var(--primary-light);">國小五上自然單元二：植物開花、授粉、結果與種子傳播全方位微課</div>
            <div style="font-size: 0.85rem; color: #a7f3d0;">支援教室大電視投影、iPad 學生平板操作、或新分頁獨立全螢幕運行</div>
          </div>
        </div>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <a href="plant-learning-site.html" target="_blank" class="link-pill-btn">🖥️ 全螢幕獨立開啟微課網站 ↗</a>
          <a href="flower-fruit-animation.html" target="_blank" class="link-pill-btn" style="border-color:#38bdf8; color:#38bdf8;">🐝 獨立開啟授粉結果動畫 ↗</a>
          <button class="btn-ctrl" onclick="switchTab('tab-flow-prompt')">🎬 查看 AI 影片提示詞庫</button>
        </div>
      </div>

      <!-- 站內無縫嵌入微課主體 -->
      <div style="width: 100%; border-radius: 16px; overflow: hidden; border: 2px solid var(--border-color); box-shadow: 0 10px 30px rgba(0,0,0,0.5); background: #ffffff;">
        <iframe src="plant-learning-site.html" style="width: 100%; height: 920px; border: none; display: block;" title="五上自然金桔授粉結果微課"></iframe>
      </div>

      <!-- 課堂投影重點總結卡片 -->
      <div class="grid-2" style="margin-top: 24px;">
        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🌸</div>
            <div class="info-card-title">金桔花授粉與結果核心公式</div>
          </div>
          <p>• <strong>授粉（Pollination）</strong>：雄蕊花藥產生之花粉粒，經由蜜蜂或風力傳遞至雌蕊柱頭之過程。</p>
          <p>• <strong>花落之後</strong>：花瓣與雄蕊逐漸枯萎脫落，營養集中運往中央子房。</p>
          <div class="highlight-box" style="margin-top: 10px;">
            <h4>🏆 國小自然段考必勝口訣：</h4>
            <p style="font-size: 1.05rem; font-weight: 800; color: #fbbf24;">雌蕊【子房】膨大 ➔ 發育為【果實（果肉）】！<br>子房內【胚珠】發育 ➔ 成為【種子】！</p>
          </div>
        </div>

        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🚀</div>
            <div class="info-card-title">種子四大傳播特徵速查表</div>
          </div>
          <p>• <strong>風力</strong>：蒲公英（冠毛降落傘）、青楓（薄翅竹蜻蜓）、木棉（棉絮）。</p>
          <p>• <strong>動物</strong>：榕樹（果肉吸引鳥吃排便）、大花咸豐草（倒鉤刺黏褲管與狗毛）。</p>
          <p>• <strong>自身彈力</strong>：非洲鳳仙花、黃花酢漿草（果莢乾燥成熟碰觸即爆裂彈出）。</p>
          <p>• <strong>水力</strong>：椰子、棋盤腳（果皮厚纖維與氣室，海漂數百公里發芽）。</p>
        </div>
      </div>
    </div>
  </div>

  <!-- 分頁: 種子四大傳播獨立實驗室 -->
  <div id="tab-seeds-detail" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">🚀 種子四大傳播獨立實驗室（課本 p.56～57）</h2>
        <span class="tb-badge">四大途徑獨立深度模擬</span>
      </div>

      <div class="info-card" style="margin-bottom: 20px; border: 1.5px solid var(--border-glow);">
        <p style="font-size: 1.05rem; line-height: 1.7;">
          依據國小自然 108 課綱與翰林版課本，植物果實成熟後為了避免與母株競爭陽光與土壤養分，發展出<strong>四大完全不同機制</strong>的傳播策略。下方為<strong>4大獨立實驗室</strong>，各具專屬物理模擬、構造解剖與即時小考：
        </p>
      </div>

      <!-- 四大獨立實驗室卡片導航格 -->
      <div class="grid-2">
        <!-- 實驗室 1: 風力傳播 -->
        <div class="info-card" style="border: 2px solid #38bdf8; background: rgba(8, 47, 73, 0.75);">
          <div class="info-card-header">
            <div class="info-card-icon">🌬️</div>
            <div class="info-card-title" style="color: #38bdf8;">1. 風力傳播獨立實驗室</div>
            <span class="tb-badge" style="background:#0284c7;">課本 p.56</span>
          </div>
          <p>• <strong>代表植物</strong>：蒲公英（冠毛降落傘）、青楓（旋轉薄翅竹蜻蜓）、木棉（輕巧棉絮）。</p>
          <p>• <strong>核心機制</strong>：構造微小輕巧、極致擴大迎風表面積，隨氣流遠飄數公里。</p>
          <p>• <strong>實驗功能</strong>：可切換微風/和風/強風，觀察不同風阻下的滑翔與自旋軌跡。</p>
          <div style="margin-top: 14px; display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="seed-wind.html" target="_blank" class="link-pill-btn" style="border-color:#38bdf8; color:#38bdf8;">🖥️ 開啟風力傳播獨立實驗室 ↗</a>
          </div>
        </div>

        <!-- 實驗室 2: 動物傳播 -->
        <div class="info-card" style="border: 2px solid #f97316; background: rgba(67, 20, 7, 0.75);">
          <div class="info-card-header">
            <div class="info-card-icon">🐦🐕</div>
            <div class="info-card-title" style="color: #f97316;">2. 動物傳播獨立實驗室</div>
            <span class="tb-badge" style="background:#ea580c;">課本 p.56~57</span>
          </div>
          <p>• <strong>代表植物</strong>：大花咸豐草（倒鉤刺附著）、榕樹/番茄（美味果肉吸引鳥吃排便）。</p>
          <p>• <strong>核心機制</strong>：【附著式】倒鉤刺卡毛皮；【食用式】耐胃酸硬種子糞便排播發芽。</p>
          <p>• <strong>實驗功能</strong>：模擬狗狗穿過草叢黏附倒鉤刺、麻雀啄食並飛至遠方排便長幼苗。</p>
          <div style="margin-top: 14px; display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="seed-animal.html" target="_blank" class="link-pill-btn" style="border-color:#f97316; color:#f97316;">🖥️ 開啟動物傳播獨立實驗室 ↗</a>
          </div>
        </div>

        <!-- 實驗室 3: 自身彈力 -->
        <div class="info-card" style="border: 2px solid #f43f5e; background: rgba(80, 7, 36, 0.75);">
          <div class="info-card-header">
            <div class="info-card-icon">💥</div>
            <div class="info-card-title" style="color: #f43f5e;">3. 自身彈力傳播獨立實驗室</div>
            <span class="tb-badge" style="background:#db2777;">課本 p.57</span>
          </div>
          <p>• <strong>代表植物</strong>：非洲鳳仙花（觸摸瞬間爆裂）、黃花酢漿草（果莢乾燥彈出）。</p>
          <p>• <strong>核心機制</strong>：果皮各層成熟張力極大，外力輕觸瞬間螺旋捲縮釋放位能，彈射種子。</p>
          <p>• <strong>實驗功能</strong>：包含 1x 與 0.25x 慢動作爆裂攝影、彈射距離標尺（0~5 公尺）測距。</p>
          <div style="margin-top: 14px; display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="seed-ballistic.html" target="_blank" class="link-pill-btn" style="border-color:#f43f5e; color:#f43f5e;">🖥️ 開啟自身彈力獨立實驗室 ↗</a>
          </div>
        </div>

        <!-- 實驗室 4: 水力傳播 -->
        <div class="info-card" style="border: 2px solid #38bdf8; background: rgba(8, 47, 73, 0.75);">
          <div class="info-card-header">
            <div class="info-card-icon">🌊</div>
            <div class="info-card-title" style="color: #38bdf8;">4. 水力傳播獨立實驗室</div>
            <span class="tb-badge" style="background:#0891b2;">課本 p.57</span>
          </div>
          <p>• <strong>代表植物</strong>：椰子（海漂之王）、棋盤腳（墾丁國寶樹）、蓮蓬（海綿狀氣室）。</p>
          <p>• <strong>核心機制</strong>：防水外果皮 ＋ 疏鬆粗纖維層與充足氣室，比重比水輕，海漂數百公里發芽。</p>
          <p>• <strong>實驗功能</strong>：切開果實縱剖面探索浮力氣室原理、洋流漂洋過海並沖上沙灘萌芽。</p>
          <div style="margin-top: 14px; display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="seed-water.html" target="_blank" class="link-pill-btn" style="border-color:#38bdf8; color:#38bdf8;">🖥️ 開啟水力傳播獨立實驗室 ↗</a>
          </div>
        </div>
      </div>

      <!-- 快速嵌入預覽區（預設顯示風力實驗室，可一鍵切換） -->
      <div style="margin-top: 24px; background: rgba(11, 36, 28, 0.9); border-radius: 16px; padding: 20px; border: 1px solid var(--border-color);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 10px;">
          <h3 style="color: var(--primary-light); font-size: 1.15rem; margin: 0;">🖥️ 站內直接操作獨立實驗室：</h3>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <button class="btn-ctrl active" id="btn-tab-seed-wind" onclick="switchEmbeddedSeed('seed-wind.html', this)">🌬️ 風力</button>
            <button class="btn-ctrl" id="btn-tab-seed-animal" onclick="switchEmbeddedSeed('seed-animal.html', this)">🐦 動物</button>
            <button class="btn-ctrl" id="btn-tab-seed-ballistic" onclick="switchEmbeddedSeed('seed-ballistic.html', this)">💥 彈力</button>
            <button class="btn-ctrl" id="btn-tab-seed-water" onclick="switchEmbeddedSeed('seed-water.html', this)">🌊 水力</button>
          </div>
        </div>
        <div style="width: 100%; border-radius: 12px; overflow: hidden; border: 2px solid var(--border-color); box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
          <iframe id="seedEmbeddedIframe" src="seed-wind.html" style="width: 100%; height: 860px; border: none; display: block;" title="種子傳播獨立實驗室"></iframe>
        </div>
      </div>
    </div>
  </div>

  <!-- 分頁: Google Flow AI 影片提示詞庫與 NotebookLM 系統 -->
  <div id="tab-flow-prompt" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">🎬 Google Flow (Veo) 3D AI 影片提示詞庫 ＆ NotebookLM 系統</h2>
        <span class="tb-badge">AI 教學應用</span>
      </div>

      <div class="info-card" style="margin-bottom: 20px;">
        <div class="info-card-header">
          <div class="info-card-icon">💡</div>
          <div class="info-card-title">使用說明：Google Flow (Veo) 影片生成</div>
        </div>
        <p>前往 <a href="https://flow.google.com" target="_blank" style="color: #38bdf8; font-weight: 700;">Google Flow (flow.google.com)</a>，點擊下方卡片的<strong>「📋 複製 Prompt」</strong>按鈕，直接貼入即可生成 3D 皮克斯風格、繁體中文標籤、台灣國語說中文語音的生動教學短片！</p>
      </div>

      <!-- 提示詞卡片 1: 金桔花授粉到結果全流程 -->
      <div class="prompt-card">
        <div class="prompt-card-header">
          <div class="prompt-card-title">
            <span>🍊 提示詞 1：金桔花授粉到結果全流程精華短片（皮克斯 3D）</span>
            <span class="tb-badge" style="background:#10b981; color:#031c12;">課本 p.54～55</span>
          </div>
          <button class="copy-prompt-btn" onclick="copyPromptText(this, 'prompt-text-kumquat')">📋 複製英文 Prompt</button>
        </div>
        <div class="prompt-box" id="prompt-text-kumquat">Cinematic 3D educational animation, Pixar style. Accompanied by gentle, clear Traditional Chinese (Taiwan Mandarin, 台灣國語) voiceover narration explaining plant reproduction to 5th-grade elementary students. All on-screen annotations, diagrams, and subtitles must strictly be in Traditional Chinese (繁體中文, 台灣用語). Macro cross-section of a blooming white kumquat flower (金桔花) under bright natural sunlight. A cute fuzzy honeybee covered in golden pollen lands on the flower, transferring glowing pollen grains from the anther to the sticky stigma of the pistil (授粉). Seamless magical time-lapse: the flower petals fall off, the green ovary at the center begins to swell and ripen, transforming into a plump, vibrant orange round kumquat fruit. The fruit splits open in a clean 3D cross-section, displaying clear Traditional Chinese annotations pointing to the juicy pulp originating from the ovary (子房 ➔ 果實) and seeds originating from the ovules (胚珠 ➔ 種子). Scientifically accurate for elementary school, vibrant colors, warm lighting, ultra-detailed 4K resolution.</div>
        <div class="prompt-desc">
          <strong>中文畫面細節：</strong>盛開白色金桔花微距剖面。可愛小蜜蜂沾滿金色花粉粒降落，將花粉傳至柱頭（授粉）。無縫縮時：白色花瓣隨後凋落，中心的綠色子房開始膨大成熟，逐漸轉變成一顆飽滿鮮豔的橙色圓形金桔果實。果實平滑切開呈現 3D 剖面，展示子房發育成的多汁果肉，以及胚珠發育成的種子。
        </div>
      </div>

      <!-- 提示詞卡片 2-A: 風力傳播獨立短片 -->
      <div class="prompt-card" style="border-color: #38bdf8;">
        <div class="prompt-card-header">
          <div class="prompt-card-title" style="color: #38bdf8;">
            <span>🌬️ 提示詞 2-A：【風力傳播獨立短片】（蒲公英冠毛 ＋ 青楓旋轉薄翅）</span>
            <span class="tb-badge" style="background:#0284c7; color:#fff;">課本 p.56 風力專屬</span>
          </div>
          <button class="copy-prompt-btn" onclick="copyPromptText(this, 'prompt-text-seed-wind')">📋 複製風力英文 Prompt</button>
        </div>
        <div class="prompt-box" id="prompt-text-seed-wind">Cinematic 3D Pixar animation style. Accompanied by cheerful, clear Traditional Chinese (Taiwan Mandarin, 台灣國語) voiceover narration explaining wind seed dispersal to 5th-grade elementary students. All on-screen captions, botanical labels, and title cards must strictly be displayed in Traditional Chinese (繁體中文, zh-TW).
Close-up shot of a fluffy white dandelion clock (蒲公英) in a sunny breeze on a lush green lawn. A gentle gust of wind blows, and parachute-like achenes with delicate white pappus hairs detach gracefully, floating across the blue sky like miniature parachutes. Smooth camera transition to a Taiwanese maple tree branch: ripe winged samara fruits (青楓薄翅翅果) drop and spin rapidly like tiny helicopters, generating aerodynamic lift and gliding over a sunlit mountain forest.
Top on-screen Traditional Chinese title card: "【風力傳播】靠風飛行大冒險". Clear annotations pointing to "冠毛（降落傘）" and "薄翅（旋轉竹蜻蜓）". Warm golden lighting, cheerful educational tone, ultra-detailed 4K resolution.</div>
        <div class="prompt-desc">
          <strong>中文畫面細節：</strong>皮克斯 3D 風格。台灣國語旁白。微距特寫蒲公英冠毛降落傘隨風飄浮；鏡頭切換至青楓樹枝，薄翅果實如竹蜻蜓高速自旋滑翔。頂端繁體中文標籤標註「冠毛（降落傘）」與「薄翅（旋轉竹蜻蜓）」。
        </div>
      </div>

      <!-- 提示詞卡片 2-B: 動物傳播獨立短片 -->
      <div class="prompt-card" style="border-color: #f97316;">
        <div class="prompt-card-header">
          <div class="prompt-card-title" style="color: #f97316;">
            <span>🐦🐕 提示詞 2-B：【動物傳播獨立短片】（咸豐草倒鉤刺 ＋ 鳥吃榕樹果）</span>
            <span class="tb-badge" style="background:#ea580c; color:#fff;">課本 p.56~57 動物專屬</span>
          </div>
          <button class="copy-prompt-btn" onclick="copyPromptText(this, 'prompt-text-seed-animal')" style="background:#ea580c; color:#fff;">📋 複製動物英文 Prompt</button>
        </div>
        <div class="prompt-box" id="prompt-text-seed-animal">Cinematic 3D Pixar animation style. Accompanied by lively, warm Traditional Chinese (Taiwan Mandarin, 台灣國語) voiceover narration explaining animal seed dispersal to 5th-grade elementary students. All on-screen captions, botanical labels, and title cards must strictly be displayed in Traditional Chinese (繁體中文, zh-TW).
Dual-scene botanical exploration:
First, macro slow-motion shot: a cute fluffy golden retriever puppy happily running through a wildflower meadow. As it brushes past Bidens pilosa (大花咸豐草), extreme macro close-up reveals tiny curved hooked spines (倒鉤刺) at the tip of slender black seeds firmly latching onto the puppy's fur and a student's denim jeans.
Then, transition to a sunny banyan tree branch: a cheerful tree sparrow (麻雀) eagerly pecks and swallows ripe red banyan figs (榕樹果實). The bird flies to a distant open field and excretes the acid-resistant hard seeds onto rich soil, where a fresh green seedling immediately sprouts.
Top on-screen Traditional Chinese title card: "【動物傳播】搭便車與美味旅行". Clear annotations pointing to "倒鉤刺（附著毛皮）" and "耐酸種子（排便發芽）". Warm natural sunlight, charming characters, 4K resolution.</div>
        <div class="prompt-desc">
          <strong>中文畫面細節：</strong>皮克斯 3D 風格。台灣國語旁白。雙場景呈現：① 大花咸豐草倒鉤刺微距卡住小狗毛皮與小學生牛仔褲搭便車；② 麻雀啄食紅熟榕樹果，飛到遠方排便，耐胃酸硬種子入土萌發新幼苗。
        </div>
      </div>

      <!-- 提示詞卡片 2-C: 自身彈力傳播獨立短片 -->
      <div class="prompt-card" style="border-color: #f43f5e;">
        <div class="prompt-card-header">
          <div class="prompt-card-title" style="color: #f43f5e;">
            <span>💥 提示詞 2-C：【自身彈力傳播獨立短片】（非洲鳳仙花 ＋ 酢漿草果莢爆裂）</span>
            <span class="tb-badge" style="background:#db2777; color:#fff;">課本 p.57 自彈專屬</span>
          </div>
          <button class="copy-prompt-btn" onclick="copyPromptText(this, 'prompt-text-seed-ballistic')" style="background:#db2777; color:#fff;">📋 複製彈力英文 Prompt</button>
        </div>
        <div class="prompt-box" id="prompt-text-seed-ballistic">Cinematic 3D educational animation, Pixar style. Accompanied by exciting, crystal-clear Traditional Chinese (Taiwan Mandarin, 台灣國語) voiceover narration explaining explosive self-dispersal of seeds to 5th-grade elementary students. All on-screen captions, botanical labels, and title cards must strictly be displayed in Traditional Chinese (繁體中文, zh-TW).
Extreme macro focus on a plump, ripe, translucent-green spindle-shaped seed pod of African touch-me-not (非洲鳳仙花果莢) on a dewy morning leaf. A curious child's fingertip gently touches the tip of the pod.
Ultra slow-motion (1000 fps high-speed camera effect): the pod valves violently split and coil backward like coiled steel springs in a split second, forcefully launching shiny dark brown seeds in an outward spiral trajectory like miniature fireworks across several meters.
Top on-screen Traditional Chinese title card: "【自身彈力】碰觸瞬間爆裂彈射！". Bold Traditional Chinese annotations: "成熟果皮張力釋放" and "種子彈射數公尺遠". Vibrant colors, dramatic high-speed action, sparkling particle trajectory, 4K resolution.</div>
        <div class="prompt-desc">
          <strong>中文畫面細節：</strong>超微距拍攝晨露中飽滿的非洲鳳仙花果莢。手指輕碰果莢，千分之一秒超高速攝影慢動作：果莢瓣瞬間螺旋捲縮釋放張力，「啪！」一聲將深褐色種子如煙火般強力彈射數公尺遠！
        </div>
      </div>

      <!-- 提示詞卡片 2-D: 水力傳播獨立短片 -->
      <div class="prompt-card" style="border-color: #38bdf8;">
        <div class="prompt-card-header">
          <div class="prompt-card-title" style="color: #38bdf8;">
            <span>🌊 提示詞 2-D：【水力傳播獨立短片】（椰子剖面 ＋ 海漂洋流沙灘發芽）</span>
            <span class="tb-badge" style="background:#0891b2; color:#fff;">課本 p.57 水力專屬</span>
          </div>
          <button class="copy-prompt-btn" onclick="copyPromptText(this, 'prompt-text-seed-water')" style="background:#0891b2; color:#fff;">📋 複製水力英文 Prompt</button>
        </div>
        <div class="prompt-box" id="prompt-text-seed-water">Cinematic 3D Pixar animation style. Accompanied by gentle, inspiring Traditional Chinese (Taiwan Mandarin, 台灣國語) voiceover narration explaining water seed dispersal to 5th-grade elementary students. All on-screen captions, botanical labels, and title cards must strictly be displayed in Traditional Chinese (繁體中文, zh-TW).
Bright tropical ocean adventure:
First, a clean 3D cross-section cut of a coconut (椰子剖面): glowing Traditional Chinese annotations highlight the smooth waterproof exocarp (防水外果皮), buoyant fibrous mesocarp packed with buoyant air pockets (疏鬆纖維氣室), and rock-hard inner endocarp protecting the seed.
The coconut and a fibrous Barringtonia fruit (棋盤腳) drop into crystal turquoise ocean waves, effortlessly bobbing on sparkling foam under sunny blue skies, drifting across deep blue ocean currents for hundreds of kilometers.
Gentle waves wash the buoyant fruits onto a pristine sandy tropical beach with gentle tide ripples. Inside the coconut, fresh green leaves and sturdy white roots break out, sprouting into a healthy young palm tree.
Top on-screen Traditional Chinese title card: "【水力傳播】漂洋過海大冒險". Clear annotations pointing to "疏鬆纖維氣室（提供浮力）" and "沙灘萌發新芽". Beautiful sun-drenched coastal lighting, refreshing ocean atmosphere, 4K resolution.</div>
        <div class="prompt-desc">
          <strong>中文畫面細節：</strong>3D 剖面展示椰子防水外果皮、疏鬆粗纖維氣室與堅硬骨質內殼；隨後椰子與棋盤腳果實落入湛藍波浪，隨洋流漂流數百公里沖上海灘，吸水萌芽長出翠綠幼苗。
        </div>
      </div>

      <!-- 提示詞卡片 3: 第一單元太陽的祕密 -->
      <div class="prompt-card">
        <div class="prompt-card-header">
          <div class="prompt-card-title">
            <span>☀️ 提示詞 3：第一單元《太陽的祕密》四季運行與彩虹折射</span>
            <span class="tb-badge" style="background:#fbbf24; color:#031c12;">單元一 太陽與影子</span>
          </div>
          <button class="copy-prompt-btn" onclick="copyPromptText(this, 'prompt-text-sun')">📋 複製英文 Prompt</button>
        </div>
        <div class="prompt-box" id="prompt-text-sun">3D educational visual infographic, Pixar animation style. Miniature Taiwanese elementary school ground with cardinal directions (E, W, S, N) clearly marked. A translucent celestial dome overhead shows three distinct glowing solar arcs: Summer Solstice at the highest noon altitude (89°), Spring/Autumn Equinox in the middle, and Winter Solstice at the lowest arc. A curious schoolboy observes the pole shadow shortening at noon during summer and stretching very long during winter. Followed by a sunny shot where the boy stands with back to the sun, spraying a gentle mist into the air to reveal a glowing 7-color rainbow arch refracting in the sunlight. Warm lighting, cheerful educational tone, 4K resolution.</div>
        <div class="prompt-desc">
          <strong>中文畫面細節：</strong>天球立體弧線展示春分秋分、夏至、冬至太陽高度角軌跡；正午竿影夏至極短 vs 冬至極長；背對太陽噴水製造色散彩虹。
        </div>
      </div>

      <!-- NotebookLM 家教系統卡片 -->
      <div class="prompt-card" style="border-color: #c084fc;">
        <div class="prompt-card-header">
          <div class="prompt-card-title" style="color: #c084fc;">
            <span>🤖 NotebookLM 自然科專屬探究家教自訂角色提示詞</span>
            <span class="tb-badge" style="background:#c084fc; color:#031c12;">AI 探究助教</span>
          </div>
          <button class="copy-prompt-btn" onclick="copyPromptText(this, 'prompt-text-notebooklm')" style="background:#c084fc;">📋 複製自訂角色指令</button>
        </div>
        <div class="prompt-box" id="prompt-text-notebooklm">你是一位專業、有耐心且幽默風趣的台灣國小五年級自然科學專屬探究學伴（自然小達人）。你的學生是國小五年級學生，來源檔案包含翰林版五上自然課本與習作。
請遵循以下最高準則：
1. 【嚴禁直接給予最終答案】：強制採用 POE 探究引導法（預測-觀察-解釋）與蘇格拉底提問法，一步步引導孩子自己從課本實驗或圖表中找出答案。
2. 【嚴格限制在國小 108 課綱範圍內】：絕對不使用超出國小程度之高中或大學專有名詞（嚴禁出現司乃耳定律、氧化還原電位、化學方程式等）。一律用五小學生能理解的生活比喻與課本實驗事實說明。
3. 【精準標註出處】：每個解說與引導均需標註課本出處（如：課本第 54 頁、習作第 28 頁）。
4. 【全程使用繁體中文（台灣）】：文字親切溫暖、多用條列式排版，結尾固定附上【想一想小提問】激發探究好奇心。</div>
        <div class="prompt-desc">
          <strong>使用方法：</strong>開啟 Google NotebookLM 筆記本，點擊右上角「設定對話」➔「自訂角色」，貼入上述指令，即可將課本 PDF 轉換為安全、防超綱、重探究的專屬自然科家教助教。
        </div>
      </div>
    </div>
  </div>

  <!-- 分頁 5: 2-4 植物的特徵與分類 -->
  <div id="tab-2-4" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">🔍 2-4 植物的特徵與分類（課本 p.64～69）</h2>
        <span class="tb-badge">二分法分類與蕨類特徵</span>
      </div>

      <!-- Canvas 模擬器 4 -->
      <div class="sim-container">
        <div class="sim-toolbar">
          <div class="sim-title">
            <span>🌲 互動式植物二分法檢索樹建構器</span>
          </div>
          <div class="sim-controls">
            <button class="btn-ctrl active" onclick="initDichotomyTree()">🔄 重置分類樹</button>
            <button class="btn-ctrl" onclick="autoSolveDichotomy()">✨ 課本標準六大植物二分法一鍵檢視</button>
          </div>
        </div>

        <div class="sim-canvas-box">
          <canvas id="canvas-tree" class="interactive-canvas"></canvas>
          <div id="tree-info-overlay" class="sim-overlay-info">
            <h5>林奈二分法（Dichotomous Key）</h5>
            <p id="tree-overlay-text">請點擊下方的分類特徵按鈕，一步步將植物族群精準二分拆解！</p>
          </div>
        </div>

        <div class="ctrl-panel" id="tree-interactive-btns">
          <div style="font-weight:700; color:var(--primary-light);">選擇第一層分類標準：</div>
          <button class="btn-ctrl active" onclick="applyTreeCriterion('habitat')">標準 A：生長環境（生長在水中 / 生長在陸地上）</button>
          <button class="btn-ctrl" onclick="applyTreeCriterion('flower')">標準 B：繁殖器官（會開花結果 / 不會開花【蕨類】）</button>
          <button class="btn-ctrl" onclick="applyTreeCriterion('stem')">標準 C：莖的質地（木本莖 / 草本莖）</button>
        </div>
      </div>

      <!-- 二分法與蕨類圖解 -->
      <div class="grid-2">
        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🌿</div>
            <div class="info-card-title">科學家的智慧：二分法分類準則</div>
          </div>
          <p>• <strong>什麼是二分法？</strong>：每次根據生物某個<strong>明確且互斥的特徵</strong>（是或否、有或沒有），將一群生物分成兩個子群體，直到分出每一種生物為止。</p>
          <p>• <strong>分類特徵選取原則</strong>：<br>
            ✅ <strong>好的標準（明確客觀）</strong>：會不會開花、生長在水生或陸生、木本莖或草本莖、單葉或複葉、葉脈是網狀脈或平行脈。<br>
            ❌ <strong>不宜的標準（主觀模糊）</strong>：漂不漂亮、長得高不高、味道香不香、對人有沒有用。
          </p>
          <p>• <strong>歷史上的大師</strong>：瑞典生物學家<strong>林奈</strong>創立二名法與現代生物分類學；明代醫學家<strong>李時珍</strong>在《本草綱目》中將草類植物按生長環境與特性分類。</p>
        </div>

        <div class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon">🍂</div>
            <div class="info-card-title">神秘的古代植物：蕨類植物大解析</div>
          </div>
          <p>• <strong>三大核心特徵</strong>：<br>
            ① <strong>不開花、不結果、沒有種子</strong>！<br>
            ② <strong>幼葉通常捲旋如問號「？」</strong>，成熟後展開呈羽狀複葉。<br>
            ③ 繁殖依靠成熟葉背上的<strong>孢子囊群</strong>，成熟時孢子囊會像彈簧彈射出微小的<strong>孢子</strong>，隨風飄散繁衍後代！
          </p>
          <p>• <strong>臺灣——世界蕨類王國</strong>：臺灣擁有超過 700 種蕨類植物，單位面積蕨類種密度世界第一！常見如<strong>腎蕨</strong>（圓球形儲水球莖）、<strong>山蘇花（臺灣巢蕨）</strong>、<strong>筆筒樹</strong>、<strong>過溝菜蕨（山蕨菜）</strong>。</p>
        </div>
      </div>

      <!-- YouTube 實境影音觀察教室：2-4 植物特徵、分類二分法與蕨類 -->
      <div style="margin-top: 26px;">
        <div class="tb-header" style="border-bottom: 2px solid rgba(192, 132, 252, 0.3); margin-bottom: 18px;">
          <h3 style="color: #c084fc; font-size: 1.35rem; display: flex; align-items: center; gap: 10px;">
            <span>🎬 實境影音觀察教室：2-4 二分法分類檢索與蕨類世界（點了就看）</span>
          </h3>
          <span class="tb-badge" style="background: rgba(192, 132, 252, 0.2); color: #c084fc; border-color: #c084fc;">YouTube 實境生態教學</span>
        </div>

        <div class="grid-3">
          <!-- 2-4 影片 1: 認識植物葉子與特徵二分法分類 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('W1JOQAvdcLw', '臺北酷課雲：認識植物葉子與特徵分類', '學習林奈二分法標準：單葉複葉、平行脈網狀脈、葉緣形狀等明確互斥特徵逐步分類')">
              <img class="video-thumb" src="https://img.youtube.com/vi/W1JOQAvdcLw/hqdefault.jpg" alt="二分法分類" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag fern">🔍 2-4 核心觀念 • 臺北酷課雲</span>
                <h4 class="video-title">科學家的思維：植物葉子特徵與二分法分類</h4>
                <p class="video-desc">每次依據一項明確且互斥的客觀特徵，將一群植物分成兩組。教導學生如何制定客觀分類標準，建立清晰檢索樹！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('W1JOQAvdcLw', '臺北酷課雲：認識植物葉子與特徵分類', '學習林奈二分法標準：單葉複葉、平行脈網狀脈、葉緣形狀等明確互斥特徵逐步分類')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=W1JOQAvdcLw" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 2-4 影片 2: 筆筒樹、蕨類與孢子囊群 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('UEbaCiihI5I', '強瘋來習自然生物：筆筒樹、蕨類特徵與孢子囊群', '特寫蕨類植物葉背孢子囊群、捲旋幼葉問號特徵，解說蕨類不開花無種子、靠孢子繁衍')">
              <img class="video-thumb" src="https://img.youtube.com/vi/UEbaCiihI5I/hqdefault.jpg" alt="蕨類孢子微距攝影" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag fern">🍂 微觀特寫 • 強瘋來習</span>
                <h4 class="video-title">蕨類王國：筆筒樹與葉背孢子囊群</h4>
                <p class="video-desc">翻開蕨類成熟葉片背面，直擊整齊排列的褐黃色孢子囊群！解說蕨類不開花、不結果、沒有種子，靠孢子囊彈射孢子繁衍！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('UEbaCiihI5I', '強瘋來習自然生物：筆筒樹、蕨類特徵與孢子囊群', '特寫蕨類植物葉背孢子囊群、捲旋幼葉問號特徵，解說蕨類不開花無種子、靠孢子繁衍')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=UEbaCiihI5I" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>

          <!-- 2-4 影片 3: 植物根的功能與校園植物觀察 -->
          <div class="video-card">
            <div class="video-thumb-wrap" onclick="playVideoModal('cAzCRSbycJA', '臺北酷課雲：植物根的功能與校園植物觀察', '實地走訪校園觀察軸根系、鬚根系、氣生根與支持根，探索植物適應環境的生存本領')">
              <img class="video-thumb" src="https://img.youtube.com/vi/cAzCRSbycJA/hqdefault.jpg" alt="校園植物探秘" loading="lazy">
              <div class="video-play-badge">▶</div>
            </div>
            <div class="video-info">
              <div>
                <span class="video-tag fern">🌿 校園實境 • 臺北酷課雲</span>
                <h4 class="video-title">校園植物探究：根部特徵與環境適應</h4>
                <p class="video-desc">實地帶學生在校園中觀察榕樹氣生根、各種植物的根系結構與特徵，連結課本知識與校園周遭環境，身歷其境！</p>
              </div>
              <div class="video-actions">
                <button class="video-btn video-btn-play" onclick="playVideoModal('cAzCRSbycJA', '臺北酷課雲：植物根的功能與校園植物觀察', '實地走訪校園觀察軸根系、鬚根系、氣生根與支持根，探索植物適應環境的生存本領')">▶ 站內播放</button>
                <a class="video-btn video-btn-link" href="https://www.youtube.com/watch?v=cAzCRSbycJA" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 分頁 6: 單元重點精華圖解整理 -->
  <div id="tab-summary" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">📚 第二單元《千變萬化的植物》重點精華整合筆記</h2>
        <span class="tb-badge">考前總複習必備</span>
      </div>

      <!-- 重點統整表格 -->
      <div style="overflow-x: auto; margin-bottom: 24px;">
        <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
          <thead>
            <tr style="background: rgba(16, 185, 129, 0.25); border-bottom: 2px solid var(--primary);">
              <th style="padding: 12px 14px;">主題小節</th>
              <th style="padding: 12px 14px;">核心植物與實例</th>
              <th style="padding: 12px 14px;">特化構造與生理機制</th>
              <th style="padding: 12px 14px;">適應目的 / 考試易錯關鍵</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.15);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--primary-light);">2-1 海邊植物</td>
              <td style="padding: 12px 14px;">海茄苳、木麻黃、濱水菜</td>
              <td style="padding: 12px 14px;">棒狀呼吸根、葉背排鹽腺、退化齒狀葉、肉質儲水葉</td>
              <td style="padding: 12px 14px;">泥灘缺氧呼吸、抗旱抗高鹽，木麻黃綠色的是「小枝」非葉！</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.15); background: rgba(255,255,255,0.02);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--primary-light);">2-1 高山植物</td>
              <td style="padding: 12px 14px;">玉山薄雪草、玉山杜鵑、玉山圓柏</td>
              <td style="padding: 12px 14px;">全株密生白絨毛、葉厚革質有蠟質、莖矮小貼地匍匐</td>
              <td style="padding: 12px 14px;">防寒禦寒、反射強烈紫外線，避免強風吹折與凍傷。</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.15);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--primary-light);">2-1 水生植物</td>
              <td style="padding: 12px 14px;">布袋蓮、大萍、睡蓮、蓮（荷花）</td>
              <td style="padding: 12px 14px;">葉柄海綿狀氣室、葉面防水細毛、長葉柄通氣管</td>
              <td style="padding: 12px 14px;">提供強大浮力漂浮於水面，並兼具通氣儲氧功能。</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.15); background: rgba(255,255,255,0.02);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--accent-cyan);">2-2 水分運輸</td>
              <td style="padding: 12px 14px;">芹菜、白花、大樹</td>
              <td style="padding: 12px 14px;">根毛吸水 ➔ 莖部木質部導管（橫切斑點、縱切管線）➔ 葉脈</td>
              <td style="padding: 12px 14px;">油泥防蒸發；水分在植物體內是「由下往上」單向運送！</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.15);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--accent-cyan);">2-2 蒸散作用</td>
              <td style="padding: 12px 14px;">葉片背面氣孔、保衛細胞</td>
              <td style="padding: 12px 14px;">保衛細胞吸水膨脹 ➔ 氣孔開；保衛細胞失水萎縮 ➔ 氣孔閉</td>
              <td style="padding: 12px 14px;">散熱降溫、提供水分向上抽吸之強大「蒸散拉力」。</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.15); background: rgba(255,255,255,0.02);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--accent-gold);">2-3 果實發育</td>
              <td style="padding: 12px 14px;">開花植物花朵（花萼、瓣、雄蕊、雌蕊）</td>
              <td style="padding: 12px 14px;">授粉後，<strong>子房 ➔ 果實</strong>；<strong>胚珠 ➔ 種子</strong></td>
              <td style="padding: 12px 14px;">切勿混淆：子房包在外面變果肉/果實，胚珠在內部變種子！</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.15);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--accent-gold);">2-3 種子傳播</td>
              <td style="padding: 12px 14px;">蒲公英、非洲鳳仙花、椰子、咸豐草</td>
              <td style="padding: 12px 14px;">風力（冠毛/翅果）、彈力（爆裂）、水力（浮力纖維）、動物（倒鉤/鳥糞）</td>
              <td style="padding: 12px 14px;">擴散族群，避免幼苗擠在親代樹蔭下爭奪陽光養分。</td>
            </tr>
            <tr style="background: rgba(255,255,255,0.02);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--accent-purple);">2-4 蕨類 vs 開花</td>
              <td style="padding: 12px 14px;">腎蕨、山蘇、筆筒樹</td>
              <td style="padding: 12px 14px;">不開花、不結果、無種子；幼葉捲旋；葉背孢子囊群</td>
              <td style="padding: 12px 14px;">蕨類是靠「孢子」繁殖，絕非種子繁殖！</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 易錯避坑指南 -->
      <div class="grid-2">
        <div class="highlight-box">
          <h4>⚠️ 考前避坑指南 1：木麻黃長得像針葉的是葉子嗎？</h4>
          <p>
            <strong>錯！</strong> 木麻黃那一節一節綠色細長的枝條是<strong>「小枝」</strong>，具有葉綠體負責光合作用；真正的葉子退化成環繞在小枝節上的<strong>微小齒狀輪生鱗片葉</strong>！這是為了極致減少海風吹拂下的水分蒸散。
          </p>
        </div>
        <div class="highlight-box">
          <h4>⚠️ 考前避坑指南 2：甘藷（地瓜）和馬鈴薯的食用部位一樣嗎？</h4>
          <p>
            <strong>不一樣！</strong> 甘藷吃的是膨大的<strong>「塊根」</strong>，能用根繁殖也能用莖繁殖；而馬鈴薯吃的是地下<strong>「塊莖」</strong>（上面具有會發芽的芽眼），屬於莖部繁殖！
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- 分頁 7: 課堂互動隨堂搶答評量（10題五上精選） -->
  <div id="tab-quiz" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">🎯 課堂互動隨堂挑戰：第二單元精選 10 題搶答測驗</h2>
        <div style="display:flex; align-items:center; gap:12px;">
          <span style="font-weight:700; color:var(--accent-gold); font-size:1.15rem;" id="quiz-score-board">目前得分：0 / 100 分</span>
          <button class="btn-ctrl" onclick="resetAllQuiz()">🔄 重新測驗</button>
        </div>
      </div>
      <p style="margin-bottom: 20px; color: var(--text-muted);">
        點擊選項立即揭曉正解與深度解析，並有音效與動畫回饋！適合課堂大螢幕投影全班搶答。
      </p>

      <div id="quiz-container">
        <!-- 題目由 JS 動態渲染或靜態結構初始化 -->
      </div>
    </div>
  </div>

  <!-- 分頁 8: 13節完整教學教案進度表與列印學習單 -->
  <div id="tab-lesson" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">📋 第二單元《千變萬化的植物》13節完整教案規劃</h2>
        <div class="no-print">
          <button class="btn-tool active" onclick="window.print()">🖨️ 列印本單元教案與學習單</button>
        </div>
      </div>

      <p style="line-height: 1.8; margin-bottom: 20px;">
        依據教育部 108 課綱與翰林版五年級上學期自然科學領域編撰，本單元共計 13 節課（每週 3 節，約 4.5 週教學進度）。
      </p>

      <div style="overflow-x: auto; margin-bottom: 30px;">
        <table style="width: 100%; border-collapse: collapse; font-size: 0.93rem;">
          <thead>
            <tr style="background: rgba(16, 185, 129, 0.2); border-bottom: 2px solid var(--primary); text-align: left;">
              <th style="padding: 10px 12px; width: 60px;">節次</th>
              <th style="padding: 10px 12px; width: 160px;">教學主題</th>
              <th style="padding: 10px 12px;">課堂核心學習活動與探究任務</th>
              <th style="padding: 10px 12px; width: 220px;">評量方式與素養指標</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12);">
              <td style="padding: 10px 12px; font-weight:700;">第 1 節</td>
              <td style="padding: 10px 12px; color:var(--primary-light);">2-1 海邊植物特化</td>
              <td style="padding: 10px 12px;">觀察海茄苳照片與標本，探究呼吸根、泌鹽孔功能；認識濱水菜肉質葉與木麻黃防風沙板根。</td>
              <td style="padding: 10px 12px;">口語評量、能說明呼吸根特化原因（自-E-A1）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12); background: rgba(255,255,255,0.02);">
              <td style="padding: 10px 12px; font-weight:700;">第 2 節</td>
              <td style="padding: 10px 12px; color:var(--primary-light);">2-1 高山植物挑戰</td>
              <td style="padding: 10px 12px;">探討高山強風、低溫、強紫外線環境；玉山薄雪草絨毛禦寒與玉山杜鵑厚蠟匍匐抗風策略。</td>
              <td style="padding: 10px 12px;">學習單紀錄、環境適應對照分析（自-E-B1）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12);">
              <td style="padding: 10px 12px; font-weight:700;">第 3 節</td>
              <td style="padding: 10px 12px; color:var(--primary-light);">2-1 水生與校園植物</td>
              <td style="padding: 10px 12px;">實體觀察布袋蓮膨大葉柄切面（氣室構造）與大萍防水纖毛；校園尋找榕樹氣生根與葉片鑲嵌。</td>
              <td style="padding: 10px 12px;">解剖顯微觀察記錄、校園實地查驗（自-E-A2）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12); background: rgba(255,255,255,0.02);">
              <td style="padding: 10px 12px; font-weight:700;">第 4 節</td>
              <td style="padding: 10px 12px; color:var(--accent-cyan);">2-2 芹菜水分吸取</td>
              <td style="padding: 10px 12px;">動手組裝芹菜紅墨水實驗裝置：設置油泥密閉瓶口作為對照組，記錄液面初值並觀察吸水速度。</td>
              <td style="padding: 10px 12px;">動手操作評量、變因控制概念（自-E-A3）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12);">
              <td style="padding: 10px 12px; font-weight:700;">第 5 節</td>
              <td style="padding: 10px 12px; color:var(--accent-cyan);">2-2 莖的橫縱剖面</td>
              <td style="padding: 10px 12px;">安全使用美工刀切片芹菜莖：觀察橫切面木質部維管束紅色小斑點、縱切面導管細長紅線條。</td>
              <td style="padding: 10px 12px;">顯微手繪圖、導管立體輸送概念（自-E-B2）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12); background: rgba(255,255,255,0.02);">
              <td style="padding: 10px 12px; font-weight:700;">第 6 節</td>
              <td style="padding: 10px 12px; color:var(--accent-cyan);">2-2 蒸散作用與氣孔</td>
              <td style="padding: 10px 12px;">觀察校園枝條套袋水珠；撕取下表皮製作玻片標本，顯微鏡下觀察保衛細胞形狀與氣孔開閉。</td>
              <td style="padding: 10px 12px;">顯微操作技術、蒸散拉力原理說明（自-E-C2）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12);">
              <td style="padding: 10px 12px; font-weight:700;">第 7 節</td>
              <td style="padding: 10px 12px; color:var(--accent-gold);">2-3 花朵解剖大拆解</td>
              <td style="padding: 10px 12px;">實物解剖朱槿或百合花：由外而內依序拆解花萼、花瓣、雄蕊（花藥花粉）、雌蕊（柱頭胚珠）。</td>
              <td style="padding: 10px 12px;">構造標本拼貼評量、花朵各部功能（自-E-A1）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12); background: rgba(255,255,255,0.02);">
              <td style="padding: 10px 12px; font-weight:700;">第 8 節</td>
              <td style="padding: 10px 12px; color:var(--accent-gold);">2-3 授粉受精與結果</td>
              <td style="padding: 10px 12px;">動畫演示花粉萌發花粉管受精；剖開番茄、青椒或四季豆，對照「子房變果實，胚珠變種子」。</td>
              <td style="padding: 10px 12px;">果實種子來源口試、概念圖繪製（自-E-B1）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12);">
              <td style="padding: 10px 12px; font-weight:700;">第 9 節</td>
              <td style="padding: 10px 12px; color:var(--accent-gold);">2-3 種子傳播四大招</td>
              <td style="padding: 10px 12px;">分組測試蒲公英與青楓飛行時間；觸摸鳳仙花彈裂；摸咸豐草倒鉤並在棉布上測試黏附力。</td>
              <td style="padding: 10px 12px;">動手探究記錄、傳播途徑分類表（自-E-C1）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12); background: rgba(255,255,255,0.02);">
              <td style="padding: 10px 12px; font-weight:700;">第 10 節</td>
              <td style="padding: 10px 12px; color:var(--accent-gold);">2-3 營養器官繁殖</td>
              <td style="padding: 10px 12px;">動手實作：落地生根葉片培植、甘藷莖段插枝水耕、胡蘿蔔根頂水培；記錄無性繁殖特點。</td>
              <td style="padding: 10px 12px;">長期觀察日記作業、實作評量（自-E-A2）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12);">
              <td style="padding: 10px 12px; font-weight:700;">第 11 節</td>
              <td style="padding: 10px 12px; color:var(--accent-purple);">2-4 二分法分類實戰</td>
              <td style="padding: 10px 12px;">以課本六種植物（大萍、布袋蓮、蓮、樟樹、甘藷、蛇莓）為例，小組討論並設計二分檢索表。</td>
              <td style="padding: 10px 12px;">二分分類樹海報展示與互評（自-E-B3）</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.12); background: rgba(255,255,255,0.02);">
              <td style="padding: 10px 12px; font-weight:700;">第 12 節</td>
              <td style="padding: 10px 12px; color:var(--accent-purple);">2-4 蕨類王國探秘</td>
              <td style="padding: 10px 12px;">觀察校園腎蕨：觀察幼葉問號捲旋、翻看成熟葉背孢子囊群、認識臺灣蕨類豐富生態與林奈分類學。</td>
              <td style="padding: 10px 12px;">蕨類與開花植物特徵比較評量（自-E-C2）</td>
            </tr>
            <tr>
              <td style="padding: 10px 12px; font-weight:700;">第 13 節</td>
              <td style="padding: 10px 12px; color:var(--accent-gold);">單元總結與評量</td>
              <td style="padding: 10px 12px;">全班使用本互動教學系統進行 10 題隨堂搶答測驗、重點精華回顧與學習成果展現。</td>
              <td style="padding: 10px 12px;">總結性評量測驗卷、自我檢核表（自-E-A1）</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 學生課堂學習單（可直接列印） -->
      <div style="border: 2px dashed rgba(52, 211, 153, 0.4); border-radius: 14px; padding: 22px; background: rgba(5,20,15,0.6);">
        <div style="text-align: center; margin-bottom: 16px;">
          <h3 style="color: var(--primary-light); font-size: 1.35rem;">📝 國小五年級自然領域 第二單元《千變萬化的植物》學生探究學習單</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-top: 4px;">五年 ____ 班  座號：____  姓名：____________  得分：________</p>
        </div>

        <div style="margin-bottom: 16px;">
          <h4 style="color: var(--accent-gold); margin-bottom: 8px;">一、植物環境特化連連看（請將植物與其適應構造及生存環境連起來）：</h4>
          <p style="font-size: 0.92rem; line-height: 1.8;">
            1. 海茄苳　　　　　　• 甲. 葉柄膨大有氣室，能提供浮力漂在水面　　　　• A. 狂風強寒高山環境<br>
            2. 玉山薄雪草　　　　• 乙. 指狀呼吸根向上伸出泥濘，葉背有泌鹽腺　　　• B. 平靜水塘漂浮環境<br>
            3. 布袋蓮　　　　　　• 丙. 全株密生白色綿毛禦寒，葉厚耐紫外線　　　　• C. 泥濘缺氧潮間帶沙灘<br>
            4. 木麻黃　　　　　　• 丁. 綠色小枝代行光合作用，葉退化為輪生細齒　　• D. 強風乾旱海濱防風林
          </p>
        </div>

        <div style="margin-bottom: 16px;">
          <h4 style="color: var(--accent-gold); margin-bottom: 8px;">二、水分運輸與蒸散作用實驗推理：</h4>
          <p style="font-size: 0.92rem; line-height: 1.8;">
            1. 在芹菜紅墨水吸水實驗中，為什麼要在量筒水面上塞入油泥或滴一層沙拉油？<br>
            　答：_____________________________________________________________________________________。<br>
            2. 將染紅的芹菜莖橫切一刀，看到的紅色斑點是什麼構造？（　　　　　　）；將莖縱切一刀，看到的紅色細線是什麼構造？（　　　　　　）。<br>
            3. 植物的氣孔通常分布在葉片的（　正面／背面　），由兩個（　　　　細胞　）圍成。當天氣涼爽含水量多時，氣孔會（　張開／閉合　）。
          </p>
        </div>

        <div style="margin-bottom: 16px;">
          <h4 style="color: var(--accent-gold); margin-bottom: 8px;">三、花朵解剖與生殖發育概念填空：</h4>
          <p style="font-size: 0.92rem; line-height: 1.8;">
            1. 一朵完整的花通常包含四個主要部分：（　　　　）、（　　　　）、（　　　　）、（　　　　）。<br>
            2. 花朵受精完成後，雌蕊基部膨大的【子房】會發育成（　　　　）；子房內部的【胚珠】會發育成（　　　　）。<br>
            3. 請寫出下列植物繁衍下一代的方式（填 風力傳播、彈力傳播、水力傳播、動物傳播、葉繁殖、莖繁殖）：<br>
            　• 蒲公英：（　　　　　　）　• 咸豐草：（　　　　　　）　• 非洲鳳仙花：（　　　　　　）<br>
            　• 落地生根：（　　　　　）　• 萬年青：（　　　　　　）　• 椰子：（　　　　　　）
          </p>
        </div>

        <div>
          <h4 style="color: var(--accent-gold); margin-bottom: 8px;">四、蕨類植物特徵觀察與二分法：</h4>
          <p style="font-size: 0.92rem; line-height: 1.8;">
            1. 蕨類植物會不會開花結果？（　會／不會　）；蕨類的幼葉通常呈現什麼形狀？（　　　　　　狀）。<br>
            2. 蕨類是靠葉片背面的（　　　　群　）散播微小的（　　　　）來繁殖下一代。<br>
            3. 如果要將「大萍」與「樟樹」用二分法分開，你會使用什麼客觀特徵作為分類標準？<br>
            　答：_____________________________________________________________________________________。
          </p>
        </div>
      </div>
    </div>
  </div>
"""

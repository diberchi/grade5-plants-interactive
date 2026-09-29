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
          <p>• <strong>水分流向</strong>：土壤水分 $\to$ 根毛 $\to$ 根部導管 $\to$ 莖部導管 $\to$ 葉柄與葉脈 $\to$ 葉肉細胞。</p>
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
    </div>
  </div>

  <!-- 分頁 4: 2-3 植物繁衍大顯身手 -->
  <div id="tab-2-3" class="tab-pane">
    <div class="textbook-section">
      <div class="tb-header">
        <h2 class="tb-title">🌸 2-3 植物繁衍大顯身手（課本 p.56～63）</h2>
        <span class="tb-badge">有性生殖與無性繁殖</span>
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
              <td style="padding: 12px 14px;">根毛吸水 $\to$ 莖部木質部導管（橫切斑點、縱切管線）$\to$ 葉脈</td>
              <td style="padding: 12px 14px;">油泥防蒸發；水分在植物體內是「由下往上」單向運送！</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.15);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--accent-cyan);">2-2 蒸散作用</td>
              <td style="padding: 12px 14px;">葉片背面氣孔、保衛細胞</td>
              <td style="padding: 12px 14px;">保衛細胞吸水膨脹 $\to$ 氣孔開；保衛細胞失水萎縮 $\to$ 氣孔閉</td>
              <td style="padding: 12px 14px;">散熱降溫、提供水分向上抽吸之強大「蒸散拉力」。</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(52, 211, 153, 0.15); background: rgba(255,255,255,0.02);">
              <td style="padding: 12px 14px; font-weight:700; color:var(--accent-gold);">2-3 果實發育</td>
              <td style="padding: 12px 14px;">開花植物花朵（花萼、瓣、雄蕊、雌蕊）</td>
              <td style="padding: 12px 14px;">授粉後，<strong>子房 $\to$ 果實</strong>；<strong>胚珠 $\to$ 種子</strong></td>
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

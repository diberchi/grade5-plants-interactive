# -*- coding: utf-8 -*-
"""
第二單元《千變萬化的植物》JavaScript 互動與模擬器模組
"""

JS_CONTENT = """
// 全域狀態
let currentTab = 'tab-intro';
let isTvMode = false;
let audioCtx = null;

// 音效引擎 (Web Audio API)
function playSound(type) {
  try {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    const now = audioCtx.currentTime;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);

    if (type === 'correct') {
      // 歡樂三和弦
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(523.25, now); // C5
      osc.frequency.setValueAtTime(659.25, now + 0.1); // E5
      osc.frequency.setValueAtTime(783.99, now + 0.2); // G5
      gain.gain.setValueAtTime(0.2, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
      osc.start(now);
      osc.stop(now + 0.45);
    } else if (type === 'wrong') {
      // 警示低音
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(220, now);
      osc.frequency.setValueAtTime(170, now + 0.15);
      gain.gain.setValueAtTime(0.25, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
      osc.start(now);
      osc.stop(now + 0.35);
    } else if (type === 'pop') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(440, now);
      osc.frequency.exponentialRampToValueAtTime(880, now + 0.1);
      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
      osc.start(now);
      osc.stop(now + 0.15);
    }
  } catch (e) {
    console.log("Audio not supported or restricted:", e);
  }
}

// 碎紙花效果 (Canvas Confetti)
function triggerConfetti() {
  const c = document.createElement('canvas');
  c.style.position = 'fixed';
  c.style.top = '0';
  c.style.left = '0';
  c.style.width = '100vw';
  c.style.height = '100vh';
  c.style.pointerEvents = 'none';
  c.style.zIndex = '99999';
  document.body.appendChild(c);

  const ctx = c.getContext('2d');
  c.width = window.innerWidth;
  c.height = window.innerHeight;

  const particles = [];
  const colors = ['#10b981', '#34d399', '#fbbf24', '#f87171', '#38bdf8', '#c084fc', '#f43f5e'];

  for (let i = 0; i < 90; i++) {
    particles.push({
      x: c.width / 2 + (Math.random() - 0.5) * 200,
      y: c.height / 2 - 50,
      vx: (Math.random() - 0.5) * 16,
      vy: (Math.random() - 0.8) * 18,
      size: Math.random() * 8 + 5,
      color: colors[Math.floor(Math.random() * colors.length)],
      rotation: Math.random() * 360,
      vRot: (Math.random() - 0.5) * 12,
      opacity: 1
    });
  }

  let frame = 0;
  function animate() {
    ctx.clearRect(0, 0, c.width, c.height);
    let alive = false;
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.45; // 重力
      p.rotation += p.vRot;
      p.opacity -= 0.012;

      if (p.opacity > 0) {
        alive = true;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.globalAlpha = Math.max(0, p.opacity);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
        ctx.restore();
      }
    });

    frame++;
    if (alive && frame < 120) {
      requestAnimationFrame(animate);
    } else {
      c.remove();
    }
  }
  animate();
}

// 頁籤切換
function switchTab(tabId) {
  currentTab = tabId;
  document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(el => el.classList.remove('active'));

  const targetPane = document.getElementById(tabId);
  if (targetPane) targetPane.classList.add('active');

  const targetBtn = document.querySelector(`.nav-tab[data-tab="${tabId}"]`);
  if (targetBtn) {
    targetBtn.classList.add('active');
    targetBtn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
  }

  playSound('pop');
  window.scrollTo({ top: 0, behavior: 'smooth' });

  // 延遲重設 Canvas 尺寸，確保繪製尺寸精準
  setTimeout(() => {
    resizeAllCanvases();
  }, 100);
}

// TV Mode 切換
function toggleTvMode() {
  isTvMode = !isTvMode;
  document.body.classList.toggle('tv-mode', isTvMode);
  const btn = document.getElementById('btn-tv-mode');
  if (btn) {
    btn.classList.toggle('active', isTvMode);
    btn.innerHTML = isTvMode ? '📺 大字投影模式：開' : '📺 大電視投影模式';
  }
  playSound('pop');
}

// QR Code 彈窗與網址複製
function openQrModal() {
  const m = document.getElementById('qrModal');
  if (m) m.style.display = 'flex';
  playSound('pop');
}

function closeQrModal() {
  const m = document.getElementById('qrModal');
  if (m) m.style.display = 'none';
}

function copyUrl() {
  const url = 'https://diberchi.github.io/grade5-plants-interactive/';
  navigator.clipboard.writeText(url).then(() => {
    const btn = document.getElementById('copyBtn');
    if (btn) {
      btn.innerText = '✅ 複製成功！';
      setTimeout(() => { btn.innerText = '📋 複製網址'; }, 2000);
    }
  }).catch(() => {
    alert('網站網址：' + url);
  });
}

// ==========================================
// 模擬器 1：極端環境植物微觀適應展示器
// ==========================================
let adaptPlant = 'mangrove'; // mangrove, rhododendron, hyacinth, casuarina
let adaptEnvVal = 50;
let adaptCanvas, adaptCtx;
let adaptAnimId;

function initAdaptSim() {
  adaptCanvas = document.getElementById('canvas-adapt');
  if (!adaptCanvas) return;
  adaptCtx = adaptCanvas.getContext('2d');
  resizeCanvas(adaptCanvas);
  renderAdaptLoop();
}

function setAdaptPlant(plant) {
  adaptPlant = plant;
  document.querySelectorAll('.sim-toolbar .btn-ctrl').forEach(b => {
    if (b.getAttribute('onclick') && b.getAttribute('onclick').includes(plant)) {
      b.classList.add('active');
    } else {
      b.classList.remove('active');
    }
  });

  const titleEl = document.getElementById('adapt-plant-title');
  const descEl = document.getElementById('adapt-plant-desc');
  const sliderLabel = document.getElementById('adapt-slider-label');

  if (plant === 'mangrove') {
    titleEl.innerText = '🌴 海茄苳（海邊紅樹林）';
    descEl.innerText = '生活於潮間帶泥灘地。地下根長出無數直立向上伸出泥面的「指狀呼吸根」，進行氣體交換；葉背密布泌鹽腺，將多餘鹽分排出形成白色結晶！';
    sliderLabel.innerText = '🌊 潮汐水位高度：';
  } else if (plant === 'rhododendron') {
    titleEl.innerText = '🏔️ 玉山杜鵑（高山嚴寒耐風）';
    descEl.innerText = '生長在海拔三千公尺以上岩壁。植株矮小匍匐貼地生長以躲避強風；葉片厚革質且表面具厚臘質，葉背具綿毛，冬天向內捲曲禦寒防水分流失！';
    sliderLabel.innerText = '💨 高山強風吹拂強度：';
  } else if (plant === 'hyacinth') {
    titleEl.innerText = '💧 布袋蓮（水生漂浮植物）';
    descEl.innerText = '葉柄呈紡錘狀膨大，內部切開具有無數蜂窩狀海綿氣室，充滿空氣產生巨大浮力漂浮於水面；水下鬚根能吸收水中養分並維持平衡。';
    sliderLabel.innerText = '🌊 水位與波浪晃動：';
  } else if (plant === 'casuarina') {
    titleEl.innerText = '🌲 木麻黃（海濱防風抗沙）';
    descEl.innerText = '深根性並具發達板根抓住沙土。綠色細長的「小枝」代替葉進行光合作用，真正的葉退化為圍繞小枝節上的「輪生微小齒葉」，極致減少水分散失抗風旱！';
    sliderLabel.innerText = '🌪️ 海濱海風乾燥程度：';
  }

  playSound('pop');
}

function updateAdaptEnv(val) {
  adaptEnvVal = parseInt(val);
  document.getElementById('adapt-env-val').innerText = val + '%';
}

let adaptTime = 0;
function renderAdaptLoop() {
  adaptTime += 0.03;
  if (currentTab === 'tab-2-1' && adaptCanvas && adaptCtx) {
    drawAdaptScene(adaptCtx, adaptCanvas.width, adaptCanvas.height, adaptTime);
  }
  adaptAnimId = requestAnimationFrame(renderAdaptLoop);
}

function drawAdaptScene(ctx, w, h, t) {
  ctx.clearRect(0, 0, w, h);

  if (adaptPlant === 'mangrove') {
    // 海茄苳：天空、泥灘、潮水、呼吸根、樹幹與葉片
    const waterY = h * 0.75 - (adaptEnvVal - 50) * 1.5;
    
    // 天空
    const skyGrad = ctx.createLinearGradient(0, 0, 0, h * 0.7);
    skyGrad.addColorStop(0, '#0a2e23');
    skyGrad.addColorStop(1, '#134e3a');
    ctx.fillStyle = skyGrad;
    ctx.fillRect(0, 0, w, h * 0.7);

    // 泥灘地
    ctx.fillStyle = '#2d2218';
    ctx.fillRect(0, h * 0.65, w, h * 0.35);

    // 主樹幹
    ctx.fillStyle = '#4a3728';
    ctx.beginPath();
    ctx.moveTo(w * 0.28, h * 0.75);
    ctx.quadraticCurveTo(w * 0.32, h * 0.45, w * 0.35, h * 0.3);
    ctx.lineTo(w * 0.38, h * 0.3);
    ctx.quadraticCurveTo(w * 0.36, h * 0.45, w * 0.42, h * 0.75);
    ctx.fill();

    // 樹冠葉片
    ctx.fillStyle = '#10b981';
    ctx.beginPath();
    ctx.arc(w * 0.36, h * 0.24, 75, 0, Math.PI * 2);
    ctx.arc(w * 0.28, h * 0.28, 55, 0, Math.PI * 2);
    ctx.arc(w * 0.44, h * 0.27, 60, 0, Math.PI * 2);
    ctx.fill();

    // 指狀呼吸根（地上氣生根）
    const numRoots = 14;
    for (let i = 0; i < numRoots; i++) {
      const rx = w * 0.15 + i * (w * 0.55 / numRoots);
      const rootH = 55 + Math.sin(i * 1.3) * 15;
      const ry = h * 0.68;

      ctx.fillStyle = '#634832';
      ctx.beginPath();
      ctx.roundRect(rx - 6, ry - rootH, 12, rootH + 30, [6, 6, 0, 0]);
      ctx.fill();

      // 呼吸孔小白點
      ctx.fillStyle = '#a7f3d0';
      ctx.fillRect(rx - 2, ry - rootH + 8, 4, 4);
      ctx.fillRect(rx - 2, ry - rootH + 20, 4, 4);
    }

    // 呼吸根文字標籤
    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 15px sans-serif';
    ctx.fillText('⬆️ 指狀呼吸根（向上伸出泥面呼吸）', w * 0.2, h * 0.56);

    // 水位
    ctx.fillStyle = 'rgba(56, 189, 248, 0.5)';
    ctx.beginPath();
    ctx.moveTo(0, waterY);
    for (let x = 0; x <= w; x += 20) {
      const wave = Math.sin(x * 0.02 + t * 3) * 4;
      ctx.lineTo(x, waterY + wave);
    }
    ctx.lineTo(w, h);
    ctx.lineTo(0, h);
    ctx.fill();

    // 水面文字
    ctx.fillStyle = '#ffffff';
    ctx.font = '13px sans-serif';
    ctx.fillText('潮水水面（隨潮汐漲退）', 20, waterY - 8);

  } else if (adaptPlant === 'rhododendron') {
    // 玉山杜鵑：高山岩石、強風吹拂彎曲枝條、厚革質葉
    const windForce = adaptEnvVal / 50;

    // 高山灰藍天空
    ctx.fillStyle = '#0f2735';
    ctx.fillRect(0, 0, w, h);

    // 遠方山巒
    ctx.fillStyle = '#1e3a4c';
    ctx.beginPath();
    ctx.moveTo(0, h * 0.5);
    ctx.lineTo(w * 0.35, h * 0.28);
    ctx.lineTo(w * 0.7, h * 0.45);
    ctx.lineTo(w, h * 0.32);
    ctx.lineTo(w, h);
    ctx.lineTo(0, h);
    ctx.fill();

    // 崎嶇岩石坡
    ctx.fillStyle = '#374151';
    ctx.beginPath();
    ctx.moveTo(0, h * 0.6);
    ctx.lineTo(w * 0.4, h * 0.55);
    ctx.lineTo(w, h * 0.7);
    ctx.lineTo(w, h);
    ctx.lineTo(0, h);
    ctx.fill();

    // 匍匐低矮樹幹（隨風微動）
    const sway = Math.sin(t * 4) * windForce * 6;
    ctx.strokeStyle = '#4b382a';
    ctx.lineWidth = 14;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(w * 0.2, h * 0.68);
    ctx.quadraticCurveTo(w * 0.4 + sway, h * 0.65, w * 0.6 + sway * 1.5, h * 0.62);
    ctx.stroke();

    // 叢聚厚革質杜鵑葉群
    for (let i = 0; i < 9; i++) {
      const lx = w * 0.35 + i * 28 + sway * (1 + i * 0.1);
      const ly = h * 0.58 + Math.sin(i * 1.5) * 12;

      ctx.save();
      ctx.translate(lx, ly);
      ctx.rotate(0.3 + windForce * 0.15 + Math.sin(t * 3 + i) * 0.08);

      // 厚蠟質革葉
      ctx.fillStyle = '#047857';
      ctx.beginPath();
      ctx.ellipse(0, 0, 26, 11, 0, 0, Math.PI * 2);
      ctx.fill();

      // 葉面光澤亮點 (反光蠟質)
      ctx.fillStyle = 'rgba(255, 255, 255, 0.45)';
      ctx.beginPath();
      ctx.ellipse(-5, -3, 14, 4, -0.2, 0, Math.PI * 2);
      ctx.fill();

      ctx.restore();
    }

    // 風向線條
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
    ctx.lineWidth = 2;
    for (let j = 0; j < 6; j++) {
      const fx = ((t * 220 + j * 160) % (w + 100)) - 50;
      const fy = h * 0.3 + j * 30;
      ctx.beginPath();
      ctx.moveTo(fx, fy);
      ctx.lineTo(fx + 50 * windForce, fy + 5);
      ctx.stroke();
    }

    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 15px sans-serif';
    ctx.fillText('🛡️ 植株矮小匍匐貼地，葉具厚厚蠟質反射紫外線並禦寒抗風', w * 0.18, h * 0.85);

  } else if (adaptPlant === 'hyacinth') {
    // 布袋蓮：水面浮力、膨大葉柄切面（蜂窩海綿氣室）
    ctx.fillStyle = '#07241d';
    ctx.fillRect(0, 0, w, h);

    const waterSurface = h * 0.5;
    const wave = Math.sin(t * 2) * (adaptEnvVal / 25);

    // 水域背景
    const waterGrad = ctx.createLinearGradient(0, waterSurface, 0, h);
    waterGrad.addColorStop(0, '#0284c7');
    waterGrad.addColorStop(1, '#082f49');
    ctx.fillStyle = waterGrad;
    ctx.fillRect(0, waterSurface + wave, w, h - waterSurface);

    // 水中鬚根
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 2.5;
    for (let r = 0; r < 16; r++) {
      ctx.beginPath();
      const rx = w * 0.38 + (r - 8) * 6;
      ctx.moveTo(rx, waterSurface + 35 + wave);
      ctx.quadraticCurveTo(rx + Math.sin(t * 2 + r) * 12, waterSurface + 90, rx + (r - 8) * 3, waterSurface + 150);
      ctx.stroke();
    }

    // 膨大葉柄外觀（左側）
    ctx.fillStyle = '#10b981';
    ctx.beginPath();
    ctx.ellipse(w * 0.38, waterSurface + 10 + wave, 40, 28, 0, 0, Math.PI * 2);
    ctx.fill();

    // 上方綠葉
    ctx.fillStyle = '#34d399';
    ctx.beginPath();
    ctx.ellipse(w * 0.34, waterSurface - 35 + wave, 30, 42, -0.2, 0, Math.PI * 2);
    ctx.fill();

    // 右側：放大切片「海綿狀氣室組織」
    ctx.save();
    ctx.translate(w * 0.68, h * 0.45);
    
    // 切面外圈
    ctx.fillStyle = '#065f46';
    ctx.beginPath();
    ctx.arc(0, 0, 85, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#34d399';
    ctx.lineWidth = 4;
    ctx.stroke();

    // 氣室微觀蜂窩孔
    ctx.fillStyle = '#a7f3d0';
    for (let row = -3; row <= 3; row++) {
      for (let col = -3; col <= 3; col++) {
        if (row * row + col * col <= 9) {
          const cx = col * 22 + (row % 2) * 11;
          const cy = row * 19;
          ctx.beginPath();
          ctx.arc(cx, cy, 7.5, 0, Math.PI * 2);
          ctx.fill();
        }
      }
    }
    ctx.restore();

    // 連接指引虛線
    ctx.strokeStyle = '#fbbf24';
    ctx.setLineDash([5, 5]);
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(w * 0.42, waterSurface + 10 + wave);
    ctx.lineTo(w * 0.58, h * 0.45);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 15px sans-serif';
    ctx.fillText('🔍 葉柄膨大放大切面：無數充滿空氣的海綿狀氣室（提供巨大浮力）', w * 0.22, h * 0.88);

  } else if (adaptPlant === 'casuarina') {
    // 木麻黃：綠色小枝、退化輪生齒狀葉、板根
    ctx.fillStyle = '#0b241c';
    ctx.fillRect(0, 0, w, h);

    // 沙丘地面
    ctx.fillStyle = '#785635';
    ctx.beginPath();
    ctx.moveTo(0, h * 0.72);
    ctx.quadraticCurveTo(w * 0.5, h * 0.68, w, h * 0.75);
    ctx.lineTo(w, h);
    ctx.lineTo(0, h);
    ctx.fill();

    // 發達板根
    ctx.fillStyle = '#45301e';
    ctx.beginPath();
    ctx.moveTo(w * 0.25, h * 0.72);
    ctx.lineTo(w * 0.35, h * 0.52);
    ctx.lineTo(w * 0.42, h * 0.71);
    ctx.fill();

    // 主樹幹
    ctx.fillRect(w * 0.32, h * 0.25, 28, h * 0.35);

    // 右側放大：細微小枝與輪生退化齒葉
    ctx.save();
    ctx.translate(w * 0.66, h * 0.42);

    // 綠色小枝
    ctx.fillStyle = '#059669';
    ctx.fillRect(-22, -90, 44, 180);

    // 小枝節環
    for (let k = -2; k <= 2; k++) {
      const jy = k * 45;
      ctx.strokeStyle = '#022c22';
      ctx.lineWidth = 3;
      ctx.strokeRect(-22, jy - 4, 44, 8);

      // 退化輪生齒狀鱗葉
      ctx.fillStyle = '#d97706';
      for (let t = -16; t <= 16; t += 8) {
        ctx.beginPath();
        ctx.moveTo(t, jy + 4);
        ctx.lineTo(t + 4, jy - 6);
        ctx.lineTo(t + 8, jy + 4);
        ctx.fill();
      }
    }
    ctx.restore();

    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 15px sans-serif';
    ctx.fillText('🌿 綠色長條是「小枝」行光合作用；真正的葉退化為圍繞節上的「微小齒葉」！', w * 0.18, h * 0.88);
  }
}

// ==========================================
// 模擬器 2：植物水分運輸與氣孔蒸散實驗室
// ==========================================
let transView = 'stem'; // stem, cross, stoma
let transSpeed = 3;
let stomaOpenRatio = 0.7; // 0~1
let transCanvas, transCtx;
let transAnimId;

function initTransportSim() {
  transCanvas = document.getElementById('canvas-transport');
  if (!transCanvas) return;
  transCtx = transCanvas.getContext('2d');
  resizeCanvas(transCanvas);
  renderTransportLoop();
}

function switchTransportView(view) {
  transView = view;
  document.getElementById('btn-view-stem').classList.toggle('active', view === 'stem');
  document.getElementById('btn-view-cross').classList.toggle('active', view === 'cross');
  document.getElementById('btn-view-stoma').classList.toggle('active', view === 'stoma');

  const speedCtrl = document.getElementById('trans-ctrl-speed');
  const stomaCtrl = document.getElementById('trans-ctrl-stoma');
  const titleEl = document.getElementById('trans-title');
  const descEl = document.getElementById('trans-desc');

  if (view === 'stem') {
    speedCtrl.style.display = 'flex';
    stomaCtrl.style.display = 'none';
    titleEl.innerText = '🌱 芹菜紅墨水吸水動態模擬';
    descEl.innerText = '紅色食用色素水由下而上輸送，油泥封住瓶口防止水面自然蒸發，水分經由莖部木質部直達葉柄與葉脈！';
  } else if (view === 'cross') {
    speedCtrl.style.display = 'flex';
    stomaCtrl.style.display = 'none';
    titleEl.innerText = '🔬 芹菜莖部橫切面與縱切面剖視';
    descEl.innerText = '橫切面可見一圈或散生的「紅色斑點」，縱切面可見一條條「垂直長紅線」，均為木質部導管輸送管路！';
  } else if (view === 'stoma') {
    speedCtrl.style.display = 'none';
    stomaCtrl.style.display = 'flex';
    titleEl.innerText = '🍃 氣孔與保衛細胞顯微開閉調節';
    descEl.innerText = '保衛細胞吸水膨脹時向外彎曲使氣孔張開，釋放水蒸氣產生「蒸散拉力」；失水時萎縮閉合以防乾枯！';
  }
  playSound('pop');
}

function updateTransSpeed(val) {
  transSpeed = parseInt(val);
  document.getElementById('trans-speed-val').innerText = val + 'x';
}

function updateStomaState(val) {
  stomaOpenRatio = parseInt(val) / 100;
  const text = stomaOpenRatio > 0.4 ? `${val}% (張開)` : `${val}% (閉合/微開)`;
  document.getElementById('stoma-slider-val').innerText = text;
}

let transTime = 0;
function renderTransportLoop() {
  transTime += 0.02 * transSpeed;
  if (currentTab === 'tab-2-2' && transCanvas && transCtx) {
    drawTransportScene(transCtx, transCanvas.width, transCanvas.height, transTime);
  }
  transAnimId = requestAnimationFrame(renderTransportLoop);
}

function drawTransportScene(ctx, w, h, t) {
  ctx.clearRect(0, 0, w, h);

  if (transView === 'stem') {
    // 燒杯 + 紅墨水 + 油泥 + 芹菜植株 + 上升紅微粒
    const beakerX = w * 0.35;
    const beakerY = h * 0.45;
    const beakerW = 160;
    const beakerH = 200;

    // 燒杯玻璃
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
    ctx.lineWidth = 4;
    ctx.strokeRect(beakerX, beakerY, beakerW, beakerH);

    // 燒杯刻度線
    ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
    for (let k = 1; k <= 5; k++) {
      ctx.fillRect(beakerX + beakerW - 25, beakerY + k * 30, 20, 2);
    }

    // 紅墨水液面
    const liquidY = beakerY + 60;
    ctx.fillStyle = 'rgba(225, 29, 72, 0.75)';
    ctx.fillRect(beakerX + 2, liquidY, beakerW - 4, beakerH - 62);

    // 油泥密封層（封口）
    ctx.fillStyle = '#d97706';
    ctx.fillRect(beakerX - 8, beakerY - 12, beakerW + 16, 20);
    ctx.fillStyle = '#fef3c7';
    ctx.font = 'bold 13px sans-serif';
    ctx.fillText('封口油泥（防蒸發）', beakerX + beakerW + 12, beakerY);

    // 芹菜莖幹（直立插入燒杯）
    ctx.fillStyle = '#059669';
    ctx.fillRect(beakerX + 55, h * 0.12, 50, beakerY + 120);

    // 導管內部上升的紅色小水滴
    ctx.fillStyle = '#ff0055';
    for (let i = 0; i < 15; i++) {
      const dropY = ((beakerY + 120 - (t * 60 + i * 26)) % (beakerY + 120 - h * 0.12)) + h * 0.12;
      const dropX = beakerX + 68 + (i % 3) * 12;
      ctx.beginPath();
      ctx.arc(dropX, dropY, 4, 0, Math.PI * 2);
      ctx.fill();
    }

    // 上方芹菜分枝與葉片（被染成微紅）
    ctx.fillStyle = '#10b981';
    ctx.beginPath();
    ctx.arc(beakerX + 50, h * 0.1, 35, 0, Math.PI * 2);
    ctx.arc(beakerX + 110, h * 0.08, 40, 0, Math.PI * 2);
    ctx.arc(beakerX + 80, h * 0.04, 30, 0, Math.PI * 2);
    ctx.fill();

    // 葉脈染紅細紋
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(beakerX + 80, h * 0.12);
    ctx.lineTo(beakerX + 50, h * 0.09);
    ctx.moveTo(beakerX + 80, h * 0.12);
    ctx.lineTo(beakerX + 110, h * 0.07);
    ctx.stroke();

    // 標籤指引
    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 15px sans-serif';
    ctx.fillText('⬆️ 水分與紅色色素沿著導管向上輸送至葉脈', beakerX - 60, h * 0.92);

  } else if (transView === 'cross') {
    // 橫切面（左）與縱切面（右）
    const cx1 = w * 0.3;
    const cy1 = h * 0.45;
    const r1 = 90;

    // 橫切面圓盤
    ctx.fillStyle = '#065f46';
    ctx.beginPath();
    ctx.arc(cx1, cy1, r1, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#34d399';
    ctx.lineWidth = 3;
    ctx.stroke();

    // 橫切面的紅色斑點（木質部維管束）
    ctx.fillStyle = '#ef4444';
    const numSpots = 12;
    for (let k = 0; k < numSpots; k++) {
      const angle = (k / numSpots) * Math.PI * 2;
      const sx = cx1 + Math.cos(angle) * (r1 * 0.65);
      const sy = cy1 + Math.sin(angle) * (r1 * 0.65);
      ctx.beginPath();
      ctx.arc(sx, sy, 7, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.fillStyle = '#f1fdf6';
    ctx.font = 'bold 16px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('【橫切面】呈現紅色小圓斑點', cx1, cy1 + r1 + 35);

    // 縱切面長條（右側）
    const lx = w * 0.65;
    const ly = h * 0.22;
    const lw = 90;
    const lh = 200;

    ctx.fillStyle = '#065f46';
    ctx.fillRect(lx, ly, lw, lh);
    ctx.strokeStyle = '#34d399';
    ctx.lineWidth = 3;
    ctx.strokeRect(lx, ly, lw, lh);

    // 縱切面的垂直紅色導管線條
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 5;
    for (let col = 1; col <= 3; col++) {
      const lineX = lx + col * 22;
      ctx.beginPath();
      ctx.moveTo(lineX, ly);
      ctx.lineTo(lineX, ly + lh);
      ctx.stroke();
    }

    ctx.fillStyle = '#f1fdf6';
    ctx.fillText('【縱切面】呈現垂直紅色細管線條', lx + lw / 2, ly + lh + 35);
    ctx.textAlign = 'left';

  } else if (transView === 'stoma') {
    // 氣孔顯微：兩顆半月形保衛細胞 + 氣孔縫隙 + 蒸散水蒸氣泡泡
    const cx = w * 0.5;
    const cy = h * 0.48;
    const gap = 4 + stomaOpenRatio * 32;

    // 表皮細胞背景
    ctx.fillStyle = '#064e3b';
    ctx.fillRect(0, 0, w, h);

    // 左側保衛細胞
    ctx.fillStyle = '#10b981';
    ctx.strokeStyle = '#34d399';
    ctx.lineWidth = 4;

    ctx.beginPath();
    ctx.ellipse(cx - gap / 2 - 25, cy, 32, 90, -0.15 * stomaOpenRatio, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // 右側保衛細胞
    ctx.beginPath();
    ctx.ellipse(cx + gap / 2 + 25, cy, 32, 90, 0.15 * stomaOpenRatio, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // 葉綠體顆粒（保衛細胞內特有）
    ctx.fillStyle = '#047857';
    for (let c = -2; c <= 2; c++) {
      ctx.beginPath();
      ctx.arc(cx - gap / 2 - 25, cy + c * 26, 6, 0, Math.PI * 2);
      ctx.arc(cx + gap / 2 + 25, cy + c * 26, 6, 0, Math.PI * 2);
      ctx.fill();
    }

    // 氣孔孔隙（深色中央孔洞）
    ctx.fillStyle = '#021c13';
    ctx.beginPath();
    ctx.ellipse(cx, cy, gap * 0.65, 75, 0, 0, Math.PI * 2);
    ctx.fill();

    // 若氣孔張開，散發藍色水蒸氣分子
    if (stomaOpenRatio > 0.2) {
      ctx.fillStyle = 'rgba(56, 189, 248, 0.7)';
      for (let s = 0; s < 10; s++) {
        const steamY = cy - ((t * 80 + s * 22) % 150);
        const steamX = cx + Math.sin(steamY * 0.05 + s) * 16;
        ctx.beginPath();
        ctx.arc(steamX, steamY, 5, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    // 文字標籤
    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 15px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('半月形保衛細胞（含葉綠體）圍成氣孔', cx, cy + 130);
    if (stomaOpenRatio > 0.4) {
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('💨 氣孔張開中：水蒸氣分子不斷蒸散，產生強大向上拉力！', cx, h * 0.12);
    } else {
      ctx.fillStyle = '#f87171';
      ctx.fillText('🔒 氣孔閉合中：減少水分散失，保護植物不致枯萎！', cx, h * 0.12);
    }
    ctx.textAlign = 'left';
  }
}

// ==========================================
// 模擬器 3：花朵解剖受精與種子傳播大冒險
// ==========================================
let flowerMode = 'dissect'; // dissect, spread
let flowerStage = 0; // 0: full, 1: remove sepal, 2: remove petal, 3: stamen, 4: pistil, 5: pollinated fruit
let spreadType = 'wind'; // wind, ballistic, water, animal
let spreadActive = false;
let flowerCanvas, flowerCtx;
let flowerAnimId;

function initFlowerSim() {
  flowerCanvas = document.getElementById('canvas-flower');
  if (!flowerCanvas) return;
  flowerCtx = flowerCanvas.getContext('2d');
  resizeCanvas(flowerCanvas);
  renderFlowerLoop();
}

function switchFlowerMode(mode) {
  flowerMode = mode;
  document.getElementById('btn-flower-dissect').classList.toggle('active', mode === 'dissect');
  document.getElementById('btn-seed-spread').classList.toggle('active', mode === 'spread');

  document.getElementById('fl-controls-dissect').style.display = mode === 'dissect' ? 'flex' : 'none';
  document.getElementById('fl-controls-spread').style.display = mode === 'spread' ? 'flex' : 'none';

  const titleEl = document.getElementById('fl-title');
  const descEl = document.getElementById('fl-desc');

  if (mode === 'dissect') {
    titleEl.innerText = '🌺 花朵構造解剖與發育結果';
    descEl.innerText = '點擊按鈕逐步拆解花萼、花瓣、雄蕊、雌蕊，並可一鍵觸發【授粉受精發育成果實】！';
  } else {
    titleEl.innerText = '🚀 種子傳播四大絕招模擬';
    descEl.innerText = '選擇不同傳播類型並點擊「觸發傳播」，觀看風力、彈力爆裂、水力漂流與動物毛皮攜帶！';
  }
  playSound('pop');
}

function dissectPart(part) {
  if (part === 'sepal') flowerStage = 1;
  else if (part === 'petal') flowerStage = 2;
  else if (part === 'stamen') flowerStage = 3;
  else if (part === 'pistil') flowerStage = 4;
  playSound('pop');
}

function resetFlower() {
  flowerStage = 0;
  pollinateAnim = 0;
  playSound('pop');
}

let pollinateAnim = 0;
function animatePollination() {
  flowerStage = 5;
  pollinateAnim = 0;
  playSound('correct');
  triggerConfetti();
}

function setSpreadType(type) {
  spreadType = type;
  document.querySelectorAll('#fl-controls-spread .btn-ctrl').forEach(b => {
    if (b.getAttribute('onclick') && b.getAttribute('onclick').includes(type)) {
      b.classList.add('active');
    } else if (b.id !== 'btn-trigger-spread') {
      b.classList.remove('active');
    }
  });
  playSound('pop');
}

function triggerSpreadAction() {
  spreadActive = true;
  spreadTimer = 0;
  playSound('correct');
  if (spreadType === 'ballistic') {
    playSound('wrong'); // 爆裂擬音
  }
}

let flowerTime = 0;
let spreadTimer = 0;
function renderFlowerLoop() {
  flowerTime += 0.03;
  if (spreadActive) spreadTimer += 0.04;
  if (currentTab === 'tab-2-3' && flowerCanvas && flowerCtx) {
    drawFlowerScene(flowerCtx, flowerCanvas.width, flowerCanvas.height, flowerTime);
  }
  flowerAnimId = requestAnimationFrame(renderFlowerLoop);
}

function drawFlowerScene(ctx, w, h, t) {
  ctx.clearRect(0, 0, w, h);

  if (flowerMode === 'dissect') {
    // 繪製花朵四大輪構造或果實
    const cx = w * 0.5;
    const cy = h * 0.52;

    // 花托花梗
    ctx.fillStyle = '#065f46';
    ctx.fillRect(cx - 10, cy + 50, 20, 140);

    if (flowerStage < 5) {
      // 1. 花萼 (sepal) - 若 stage >= 1 則隱藏或分離
      if (flowerStage < 1) {
        ctx.fillStyle = '#047857';
        ctx.beginPath();
        ctx.ellipse(cx - 50, cy + 45, 30, 15, -0.4, 0, Math.PI * 2);
        ctx.ellipse(cx + 50, cy + 45, 30, 15, 0.4, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#34d399';
        ctx.fillText('綠色花萼（保護花苞）', cx - 180, cy + 60);
      }

      // 2. 花瓣 (petal) - 若 stage >= 2 則移除
      if (flowerStage < 2) {
        ctx.fillStyle = '#f43f5e';
        const numPetals = 5;
        for (let p = 0; p < numPetals; p++) {
          const angle = (p / numPetals) * Math.PI * 2 - Math.PI / 2;
          const px = cx + Math.cos(angle) * 75;
          const py = cy + Math.sin(angle) * 75;
          ctx.beginPath();
          ctx.arc(px, py, 48, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.fillStyle = '#ffffff';
        ctx.fillText('鮮豔花瓣（吸引昆蟲）', cx + 110, cy - 60);
      }

      // 3. 雄蕊 (stamen) - 花絲 + 花藥花粉
      if (flowerStage < 4) {
        for (let s = -2; s <= 2; s++) {
          if (s === 0) continue;
          const sx = cx + s * 30;
          ctx.strokeStyle = '#fef08a';
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.moveTo(cx, cy + 40);
          ctx.quadraticCurveTo(sx, cy, sx, cy - 50);
          ctx.stroke();

          // 花藥
          ctx.fillStyle = '#eab308';
          ctx.beginPath();
          ctx.ellipse(sx, cy - 50, 9, 6, 0.2, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.fillStyle = '#fef08a';
        ctx.fillText('雄蕊（花藥與金黃花粉）', cx + 90, cy - 20);
      }

      // 4. 雌蕊 (pistil) - 正中央：柱頭 + 花柱 + 子房 + 胚珠
      // 子房 (膨大底部)
      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.ellipse(cx, cy + 25, 30, 40, 0, 0, Math.PI * 2);
      ctx.fill();

      // 子房內部胚珠
      ctx.fillStyle = '#fbbf24';
      ctx.beginPath();
      ctx.arc(cx, cy + 25, 12, 0, Math.PI * 2);
      ctx.fill();

      // 細長花柱與黏性柱頭
      ctx.strokeStyle = '#34d399';
      ctx.lineWidth = 7;
      ctx.beginPath();
      ctx.moveTo(cx, cy + 10);
      ctx.lineTo(cx, cy - 80);
      ctx.stroke();

      // 柱頭 (三叉或黏性盤)
      ctx.fillStyle = '#059669';
      ctx.beginPath();
      ctx.arc(cx, cy - 85, 14, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 15px sans-serif';
      ctx.fillText('雌蕊：頂端黏性【柱頭】', cx - 180, cy - 80);
      ctx.fillText('雌蕊：膨大【子房】內含【胚珠】', cx - 210, cy + 25);

    } else {
      // 5. 授粉受精成果實動畫
      pollinateAnim = Math.min(1, pollinateAnim + 0.02);

      // 發育膨大的果實（例如大番茄）
      const fruitR = 40 + pollinateAnim * 65;
      ctx.fillStyle = `rgb(${Math.floor(16 + pollinateAnim * 220)}, ${Math.floor(185 - pollinateAnim * 150)}, 50)`;
      ctx.beginPath();
      ctx.arc(cx, cy, fruitR, 0, Math.PI * 2);
      ctx.fill();

      // 果實內部種子（由胚珠發育）
      ctx.fillStyle = '#fef08a';
      for (let z = 0; z < 6; z++) {
        const zAngle = (z / 6) * Math.PI * 2;
        const zx = cx + Math.cos(zAngle) * (fruitR * 0.55);
        const zy = cy + Math.sin(zAngle) * (fruitR * 0.55);
        ctx.beginPath();
        ctx.arc(zx, zy, 7, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 18px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('✨ 子房發育成【果實】！胚珠發育成【種子】！', cx, cy - fruitR - 20);
      ctx.textAlign = 'left';
    }

  } else {
    // 種子傳播四大絕招模擬
    const cx = w * 0.5;
    const cy = h * 0.5;

    if (spreadType === 'wind') {
      // 蒲公英冠毛 / 青楓雙翅果隨風飄
      ctx.fillStyle = '#06281e';
      ctx.fillRect(0, 0, w, h);

      // 風速粒子
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      for (let i = 0; i < 8; i++) {
        const wx = ((t * 180 + i * 150) % w);
        ctx.strokeRect(wx, 50 + i * 45, 60, 1);
      }

      // 飄散的蒲公英降落傘種子
      const seedsCount = 12;
      for (let s = 0; s < seedsCount; s++) {
        const sx = ((t * 120 + s * 95) % (w + 100)) - 50;
        const sy = h * 0.2 + s * 25 + Math.sin(t * 3 + s) * 20;

        // 黑色小種子
        ctx.fillStyle = '#451a03';
        ctx.beginPath();
        ctx.ellipse(sx, sy + 25, 4, 8, 0.2, 0, Math.PI * 2);
        ctx.fill();

        // 傘柄
        ctx.strokeStyle = '#fef3c7';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(sx, sy + 25);
        ctx.lineTo(sx, sy);
        ctx.stroke();

        // 白色羽狀冠毛
        ctx.strokeStyle = '#ffffff';
        for (let a = -4; a <= 4; a++) {
          ctx.beginPath();
          ctx.moveTo(sx, sy);
          ctx.lineTo(sx + a * 5, sy - 15);
          ctx.stroke();
        }
      }

      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 16px sans-serif';
      ctx.fillText('🍃 風力傳播：蒲公英冠毛如降落傘隨風飄浮數公里；青楓翅果旋轉滑翔！', 30, h * 0.9);

    } else if (spreadType === 'ballistic') {
      // 非洲鳳仙花成熟果莢碰觸瞬間爆開
      ctx.fillStyle = '#0f241a';
      ctx.fillRect(0, 0, w, h);

      if (!spreadActive || spreadTimer < 0.1) {
        // 飽滿緊繃的綠色果莢
        ctx.fillStyle = '#10b981';
        ctx.beginPath();
        ctx.ellipse(cx, cy, 65, 30, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fbbf24';
        ctx.font = 'bold 16px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('💥 成熟果莢組織張力極大！請點擊【觸發傳播動態】引爆！', cx, cy + 100);
        ctx.textAlign = 'left';
      } else {
        // 炸開：果皮螺旋捲曲 + 種子四向高速飛射
        ctx.strokeStyle = '#059669';
        ctx.lineWidth = 7;
        for (let k = 0; k < 5; k++) {
          const a = (k / 5) * Math.PI * 2;
          ctx.beginPath();
          ctx.arc(cx + Math.cos(a) * 45, cy + Math.sin(a) * 45, 25, a, a + Math.PI);
          ctx.stroke();
        }

        // 飛散的種子
        ctx.fillStyle = '#78350f';
        for (let s = 0; s < 16; s++) {
          const angle = (s / 16) * Math.PI * 2;
          const dist = 50 + spreadTimer * 260;
          const zx = cx + Math.cos(angle) * dist;
          const zy = cy + Math.sin(angle) * dist;
          ctx.beginPath();
          ctx.arc(zx, zy, 6, 0, Math.PI * 2);
          ctx.fill();
        }

        ctx.fillStyle = '#fbbf24';
        ctx.font = 'bold 16px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('💥 砰！果皮受碰觸瞬間反捲，產生強大彈力將種子彈射至遠處！', cx, h * 0.9);
        ctx.textAlign = 'left';
      }

    } else if (spreadType === 'water') {
      // 椰子 / 棋盤腳在海浪中隨波漂流
      ctx.fillStyle = '#0369a1';
      ctx.fillRect(0, h * 0.45, w, h * 0.55);
      ctx.fillStyle = '#0c4a6e';
      ctx.fillRect(0, 0, w, h * 0.45);

      const cocoX = ((t * 80) % (w + 100)) - 50;
      const cocoY = h * 0.46 + Math.sin(t * 3) * 15;

      // 椰子果實（木質纖維保護層）
      ctx.fillStyle = '#78350f';
      ctx.beginPath();
      ctx.ellipse(cocoX, cocoY, 38, 30, 0.2, 0, Math.PI * 2);
      ctx.fill();

      // 浮力波浪線
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let x = 0; x <= w; x += 30) {
        ctx.lineTo(x, h * 0.46 + Math.sin(x * 0.03 + t * 4) * 8);
      }
      ctx.stroke();

      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 16px sans-serif';
      ctx.fillText('🌊 水力傳播：椰子具有疏鬆富含氣室的纖維外殼，耐鹽水且長年漂浮不爛！', 30, h * 0.9);

    } else if (spreadType === 'animal') {
      // 大花咸豐草倒鉤附著在毛皮上
      ctx.fillStyle = '#062e20';
      ctx.fillRect(0, 0, w, h);

      // 動物毛皮背景
      ctx.fillStyle = '#d97706';
      ctx.fillRect(0, h * 0.5, w, h * 0.5);

      // 毛皮細毛
      ctx.strokeStyle = '#b45309';
      ctx.lineWidth = 2;
      for (let m = 0; m < w; m += 15) {
        ctx.beginPath();
        ctx.moveTo(m, h * 0.5);
        ctx.lineTo(m + 8, h * 0.5 - 18);
        ctx.stroke();
      }

      // 咸豐草種子（前端具倒鉤刺，牢牢黏附）
      const numHooks = 5;
      for (let hIndex = 0; hIndex < numHooks; hIndex++) {
        const hx = w * 0.25 + hIndex * 90;
        const hy = h * 0.5 - 20;

        // 黑色長條種子
        ctx.fillStyle = '#1e1b4b';
        ctx.fillRect(hx, hy, 10, 45);

        // 前端兩根倒鉤刺
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(hx + 2, hy);
        ctx.lineTo(hx - 8, hy - 16);
        ctx.lineTo(hx - 4, hy - 12); // 倒刺
        ctx.moveTo(hx + 8, hy);
        ctx.lineTo(hx + 18, hy - 16);
        ctx.lineTo(hx + 14, hy - 12);
        ctx.stroke();
      }

      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 16px sans-serif';
      ctx.fillText('🐕 動物傳播：大花咸豐草前端具逆向倒鉤刺，隨路過動物毛皮搭便車旅行！', 30, h * 0.9);
    }
  }
}

// ==========================================
// 模擬器 4：植物特徵二分法檢索樹互動器
// ==========================================
let treeCanvas, treeCtx;
let treeStep = 0; // 0: initial, 1: habitat split, 2: flower split, 3: full solved
const plantData = [
  { name: '大萍', habitat: 'water', flower: true, stem: 'herb' },
  { name: '布袋蓮', habitat: 'water', flower: true, stem: 'herb' },
  { name: '蓮(荷花)', habitat: 'water', flower: true, stem: 'herb' },
  { name: '樟樹', habitat: 'land', flower: true, stem: 'wood' },
  { name: '甘藷', habitat: 'land', flower: true, stem: 'herb' },
  { name: '腎蕨', habitat: 'land', flower: false, stem: 'herb' }
];

function initDichotomyTree() {
  treeStep = 0;
  treeCanvas = document.getElementById('canvas-tree');
  if (!treeCanvas) return;
  treeCtx = treeCanvas.getContext('2d');
  resizeCanvas(treeCanvas);
  document.getElementById('tree-overlay-text').innerText = '請點選下方標準按鈕，建構植物二分檢索樹！';
  drawTree();
}

function applyTreeCriterion(type) {
  if (type === 'habitat') treeStep = 1;
  else if (type === 'flower') treeStep = 2;
  else if (type === 'stem') treeStep = 3;
  playSound('pop');
  drawTree();
}

function autoSolveDichotomy() {
  treeStep = 3;
  playSound('correct');
  triggerConfetti();
  document.getElementById('tree-overlay-text').innerText = '🎉 課本六大植物標準二分檢索樹建構完成！';
  drawTree();
}

function drawTree() {
  if (!treeCanvas || !treeCtx) return;
  const ctx = treeCtx;
  const w = treeCanvas.width;
  const h = treeCanvas.height;
  ctx.clearRect(0, 0, w, h);

  ctx.fillStyle = '#f1fdf6';
  ctx.font = 'bold 16px sans-serif';
  ctx.textAlign = 'center';

  // 頂層：全體 6 大植物
  drawNode(ctx, w * 0.5, 45, '全體 6 種植物：大萍、布袋蓮、蓮、樟樹、甘藷、腎蕨', '#065f46', '#34d399');

  if (treeStep === 0) {
    ctx.fillStyle = '#a7f3d0';
    ctx.font = '15px sans-serif';
    ctx.fillText('👉 請在下方點選分類標準（例如：生長環境是否在水中？）', w * 0.5, h * 0.5);
    ctx.textAlign = 'left';
    return;
  }

  // 第一層分支：水生 vs 陸生
  drawBranch(ctx, w * 0.5, 75, w * 0.28, 140, '生長在水中');
  drawBranch(ctx, w * 0.5, 75, w * 0.72, 140, '生長在陸地');

  drawNode(ctx, w * 0.28, 160, '水生植物 (大萍、布袋蓮、蓮)', '#0284c7', '#38bdf8');
  drawNode(ctx, w * 0.72, 160, '陸生植物 (樟樹、甘藷、腎蕨)', '#059669', '#34d399');

  if (treeStep >= 2) {
    // 陸生植物再分：會開花 vs 不會開花(蕨類)
    drawBranch(ctx, w * 0.72, 190, w * 0.6, 260, '會開花結果');
    drawBranch(ctx, w * 0.72, 190, w * 0.86, 260, '不開花(孢子)');

    drawNode(ctx, w * 0.6, 280, '開花植物 (樟樹、甘藷)', '#065f46', '#34d399');
    drawNode(ctx, w * 0.86, 280, '蕨類：腎蕨 🏆', '#7c3aed', '#c084fc');
  }

  if (treeStep >= 3) {
    // 樟樹 vs 甘藷：木本莖 vs 草本莖
    drawBranch(ctx, w * 0.6, 310, w * 0.5, 380, '木本莖');
    drawBranch(ctx, w * 0.6, 310, w * 0.7, 380, '草本蔓生莖');

    drawNode(ctx, w * 0.5, 400, '樟樹 🌲', '#d97706', '#fbbf24');
    drawNode(ctx, w * 0.7, 400, '甘藷 🍠', '#10b981', '#6ee7b7');

    // 水生植物細分：漂浮水面 vs 沉水/挺水
    drawBranch(ctx, w * 0.28, 190, w * 0.16, 260, '全株漂浮水面');
    drawBranch(ctx, w * 0.28, 190, w * 0.38, 260, '根生於泥挺水');

    drawNode(ctx, w * 0.16, 280, '大萍、布袋蓮', '#0284c7', '#38bdf8');
    drawNode(ctx, w * 0.38, 280, '蓮 (荷花) 🪷', '#ec4899', '#f472b6');
  }

  ctx.textAlign = 'left';
}

function drawNode(ctx, x, y, text, bg, border) {
  ctx.save();
  ctx.font = 'bold 13px sans-serif';
  const tw = ctx.measureText(text).width + 24;
  ctx.fillStyle = bg;
  ctx.strokeStyle = border;
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.roundRect(x - tw / 2, y - 16, tw, 32, 8);
  ctx.fill();
  ctx.stroke();
  ctx.fillStyle = '#ffffff';
  ctx.fillText(text, x, y + 5);
  ctx.restore();
}

function drawBranch(ctx, x1, y1, x2, y2, label) {
  ctx.strokeStyle = '#34d399';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();

  // 標籤
  ctx.fillStyle = '#fbbf24';
  ctx.font = '12px sans-serif';
  const mx = (x1 + x2) / 2;
  const my = (y1 + y2) / 2;
  ctx.fillText(label, mx, my - 6);
}

// ==========================================
// 課堂互動隨堂搶答測驗（10 題精華題）
// ==========================================
const quizQuestions = [
  {
    q: '1. 海茄苳生長在潮間帶泥灘地，泥中缺乏氧氣，它演化出哪種特殊構造露出泥面呼吸？',
    options: ['肥厚肉質葉', '棒狀指狀呼吸根', '發達板根', '卷鬚攀緣莖'],
    ans: 1,
    exp: '正解：棒狀指狀呼吸根。海茄苳由地下根向上垂直生長出許多呼吸根，露出泥灘表面直接進行氣體交換。'
  },
  {
    q: '2. 木麻黃生長在海邊防風沙，看起來一節一節綠色細長的構造，在植物學上實際上是什麼？',
    options: ['針狀葉', '綠色小枝（代行光合作用）', '氣生根', '假葉'],
    ans: 1,
    exp: '正解：綠色小枝。木麻黃真正葉子已退化為圍繞小枝節上的微小齒狀葉，由綠色小枝負責光合作用以極致減少水分散失。'
  },
  {
    q: '3. 玉山薄雪草能生長在嚴寒、強紫外線的高山上，主要是因為全身具有哪種特化構造？',
    options: ['刺針與毒素', '密生白色綿毛', '巨大肥厚球莖', '氣室組織'],
    ans: 1,
    exp: '正解：密生白色綿毛。白色綿毛就像保暖大衣，能禦寒保溫並反射強烈紫外線。'
  },
  {
    q: '4. 布袋蓮之所以能平穩漂浮在水面上，是因為葉柄具有什麼獨特組織？',
    options: ['充滿空氣的海綿狀氣室', '堅硬木質纖維', '大量儲水細胞', '厚厚蠟質層'],
    ans: 0,
    exp: '正解：充滿空氣的海綿狀氣室。布袋蓮葉柄膨大，切面有無數微小氣孔氣室，能儲存空氣產生強大浮力。'
  },
  {
    q: '5. 在芹菜紅墨水水分吸收實驗中，燒杯口塞入油泥的主要科學目的是什麼？',
    options: ['防止芹菜倒塌', '防止杯內水分直接蒸發到空氣中', '加快紅墨水染色', '隔絕光線'],
    ans: 1,
    exp: '正解：防止杯內水分直接蒸發。塞油泥是變因控制，確保液面下降純粹是由芹菜吸收所致。'
  },
  {
    q: '6. 將染過紅墨水的芹菜莖「橫切」一刀，在放大鏡下看見許多「紅色細小斑點」，這些斑點是？',
    options: ['葉綠體', '氣孔', '木質部導管（維管束）', '保衛細胞'],
    ans: 2,
    exp: '正解：木質部導管（維管束）。導管如同水管直通上下，橫切看是小斑點，縱切看則是垂直管線。'
  },
  {
    q: '7. 植物花朵受精完成後，雌蕊基部膨大的【子房】與內部的【胚珠】分別會發育為什麼？',
    options: ['花瓣與雄蕊', '果實與種子', '種子與果實', '根與莖'],
    ans: 1,
    exp: '正解：果實與種子！牢記口訣：「子房變果實，胚珠變種子」。'
  },
  {
    q: '8. 非洲鳳仙花與黃花酢漿草繁衍後代時，主要是靠哪種方式將種子傳播到遠處？',
    options: ['水力漂流', '動物取食排便', '果莢爆裂的彈力', '風力吹拂'],
    ans: 2,
    exp: '正解：果莢爆裂的彈力。果莢成熟乾燥張力極高，輕輕一碰即螺旋捲曲炸開彈飛種子。'
  },
  {
    q: '9. 落地生根這類植物，主要是利用哪一個營養器官長出不定芽來繁殖下一代？',
    options: ['花瓣', '葉片邊緣缺刻', '主根', '種子'],
    ans: 1,
    exp: '正解：葉片邊緣缺刻。落地生根的厚肉質葉缺刻處會長出帶小根的小芽，掉落即可獨立成株。'
  },
  {
    q: '10. 關於蕨類植物（如腎蕨、山蘇）的特徵，下列哪一項敘述是【錯誤】的？',
    options: ['幼葉通常呈問號捲旋狀', '葉背成熟時具有孢子囊群', '靠開花結出果實與種子繁殖', '臺灣單位面積蕨類密度世界第一'],
    ans: 2,
    exp: '正解：選項【靠開花結出果實與種子繁殖】是錯誤的！蕨類不開花、不結果、沒有種子，是依靠微小的「孢子」繁殖！'
  }
];

let userScores = {};

function initQuiz() {
  const container = document.getElementById('quiz-container');
  if (!container) return;
  container.innerHTML = '';

  quizQuestions.forEach((item, qIdx) => {
    const card = document.createElement('div');
    card.className = 'quiz-card';
    card.id = `qcard-${qIdx}`;

    const optsHtml = item.options.map((opt, oIdx) => `
      <button class="quiz-opt" id="opt-${qIdx}-${oIdx}" onclick="selectQuizOpt(${qIdx}, ${oIdx})">
        <span style="font-weight:700; color:var(--primary-light); min-width:20px;">(${['A','B','C','D'][oIdx]})</span>
        <span>${opt}</span>
      </button>
    `).join('');

    card.innerHTML = `
      <div class="quiz-header">
        <span class="quiz-badge">第 ${qIdx + 1} 題 / 共 10 題</span>
        <span style="font-size:0.85rem; color:var(--accent-gold);">分值：10 分</span>
      </div>
      <div class="quiz-title">${item.q}</div>
      <div class="quiz-options">${optsHtml}</div>
      <div class="quiz-feedback" id="feedback-${qIdx}">
        <div id="fb-text-${qIdx}"></div>
      </div>
    `;
    container.appendChild(card);
  });
}

function selectQuizOpt(qIdx, optIdx) {
  const qData = quizQuestions[qIdx];
  const card = document.getElementById(`qcard-${qIdx}`);
  const fb = document.getElementById(`feedback-${qIdx}`);
  const fbText = document.getElementById(`fb-text-${qIdx}`);

  // 禁用該題按鈕
  for (let i = 0; i < 4; i++) {
    const btn = document.getElementById(`opt-${qIdx}-${i}`);
    if (btn) btn.disabled = true;
  }

  const selectedBtn = document.getElementById(`opt-${qIdx}-${optIdx}`);
  const correctBtn = document.getElementById(`opt-${qIdx}-${qData.ans}`);

  if (optIdx === qData.ans) {
    userScores[qIdx] = 10;
    card.classList.add('correct');
    if (selectedBtn) selectedBtn.classList.add('selected-correct');
    fb.className = 'quiz-feedback show feedback-correct';
    fbText.innerHTML = `🎉 <strong>答對了！</strong> ${qData.exp}`;
    playSound('correct');
    triggerConfetti();
  } else {
    userScores[qIdx] = 0;
    card.classList.add('wrong');
    if (selectedBtn) selectedBtn.classList.add('selected-wrong');
    if (correctBtn) correctBtn.classList.add('show-correct');
    fb.className = 'quiz-feedback show feedback-wrong';
    fbText.innerHTML = `❌ <strong>答錯囉！</strong> ${qData.exp}`;
    playSound('wrong');
  }

  updateTotalScore();
}

function updateTotalScore() {
  let total = 0;
  Object.values(userScores).forEach(s => total += s);
  const board = document.getElementById('quiz-score-board');
  if (board) {
    board.innerText = `目前得分：${total} / 100 分`;
    if (total === 100) {
      board.innerText = `🏆 滿分 100 分！太神了！植物大師！`;
    }
  }
}

function resetAllQuiz() {
  userScores = {};
  updateTotalScore();
  initQuiz();
  playSound('pop');
}

// 響應式調整所有 Canvas 大小
function resizeCanvas(c) {
  if (!c) return;
  const rect = c.parentElement.getBoundingClientRect();
  if (rect.width > 0 && rect.height > 0) {
    c.width = rect.width;
    c.height = rect.height;
  }
}

function resizeAllCanvases() {
  resizeCanvas(document.getElementById('canvas-adapt'));
  resizeCanvas(document.getElementById('canvas-transport'));
  resizeCanvas(document.getElementById('canvas-flower'));
  resizeCanvas(document.getElementById('canvas-tree'));
  if (currentTab === 'tab-2-4') drawTree();
}

// 頁面初始化
window.addEventListener('DOMContentLoaded', () => {
  // 頂部導航列支援滑鼠滾輪水平捲動（避免垂直卡住）
  const navTabs = document.getElementById('main-nav-tabs');
  if (navTabs) {
    navTabs.addEventListener('wheel', (e) => {
      if (e.deltaY !== 0) {
        e.preventDefault();
        navTabs.scrollLeft += e.deltaY;
      }
    }, { passive: false });
  }

  // 初始化各模擬器與題目
  initAdaptSim();
  initTransportSim();
  initFlowerSim();
  initDichotomyTree();
  initQuiz();

  window.addEventListener('resize', () => {
    resizeAllCanvases();
  });
});
"""

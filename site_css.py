# -*- coding: utf-8 -*-
CSS_CONTENT = """
:root {
  --bg-dark: #051610;
  --bg-body: #061e16;
  --card-bg: rgba(11, 36, 28, 0.88);
  --card-hover: rgba(16, 52, 40, 0.95);
  --primary: #10b981;
  --primary-hover: #059669;
  --primary-light: #6ee7b7;
  --accent-gold: #fbbf24;
  --accent-cyan: #38bdf8;
  --accent-coral: #fb7185;
  --accent-purple: #c084fc;
  --text-main: #f1fdf6;
  --text-muted: #a7f3d0;
  --text-dim: #6ee7b7;
  --border-color: rgba(52, 211, 153, 0.25);
  --border-glow: rgba(16, 185, 129, 0.45);
  --shadow-card: 0 10px 28px rgba(0, 0, 0, 0.45);
  --font-base: 16px;
  --canvas-bg: #03120c;
}

/* 大電視投影模式（TV Mode） */
body.tv-mode {
  --font-base: 20px;
  --card-bg: rgba(9, 32, 24, 0.96);
  --text-main: #ffffff;
  --text-muted: #bbf7d0;
  --border-color: rgba(52, 211, 153, 0.45);
}

body.tv-mode .site-title {
  font-size: 2.2rem !important;
}

body.tv-mode .section-title {
  font-size: 1.85rem !important;
}

body.tv-mode p, body.tv-mode li, body.tv-mode .quiz-opt {
  font-size: 1.18rem !important;
  line-height: 1.85 !important;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
  -webkit-tap-highlight-color: transparent;
}

body {
  background-color: var(--bg-body);
  background-image: 
    radial-gradient(circle at 10% 12%, rgba(16, 185, 129, 0.15), transparent 45%),
    radial-gradient(circle at 90% 18%, rgba(251, 191, 36, 0.12), transparent 45%),
    radial-gradient(circle at 50% 80%, rgba(56, 189, 248, 0.1), transparent 50%),
    linear-gradient(180deg, #051610 0%, #061e16 50%, #03120c 100%);
  color: var(--text-main);
  font-size: var(--font-base);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
}

/* 頂部 Header */
header {
  background: rgba(5, 22, 16, 0.94);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border-color);
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.header-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 12px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}

.brand-icon {
  width: 44px;
  height: 44px;
  background: linear-gradient(135deg, #10b981, #059669);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  box-shadow: 0 0 16px rgba(16, 185, 129, 0.5);
}

.site-title {
  font-size: 1.45rem;
  font-weight: 800;
  background: linear-gradient(135deg, #a7f3d0, #34d399, #fbbf24);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: 0.5px;
}

.site-subtitle {
  font-size: 0.82rem;
  color: var(--text-muted);
  display: block;
  margin-top: 2px;
}

.header-tools {
  display: flex;
  align-items: center;
  gap: 10px;
}

.btn-tool {
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid var(--border-color);
  color: var(--text-main);
  padding: 8px 14px;
  border-radius: 999px;
  font-size: 0.88rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.25s ease;
}

.btn-tool:hover {
  background: rgba(16, 185, 129, 0.35);
  border-color: var(--primary-light);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.btn-tool.active {
  background: linear-gradient(135deg, #10b981, #059669);
  color: #ffffff;
  font-weight: 700;
  box-shadow: 0 0 14px rgba(16, 185, 129, 0.6);
}

/* 頂部水平滾動導航條 */
.nav-scroll-wrapper {
  background: rgba(4, 18, 13, 0.85);
  border-bottom: 1px solid rgba(52, 211, 153, 0.18);
  position: relative;
  overflow: hidden;
}

.nav-tabs {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--primary) transparent;
  padding: 6px 16px;
  gap: 8px;
  scroll-behavior: smooth;
  user-select: none;
}

.nav-tabs::-webkit-scrollbar {
  height: 4px;
}

.nav-tabs::-webkit-scrollbar-thumb {
  background: var(--primary);
  border-radius: 4px;
}

.nav-tab {
  white-space: nowrap;
  padding: 10px 18px;
  border-radius: 10px;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-muted);
  background: transparent;
  border: 1px solid transparent;
  cursor: pointer;
  transition: all 0.22s ease;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  flex-shrink: 0;
}

.nav-tab:hover {
  color: #ffffff;
  background: rgba(16, 185, 129, 0.12);
  border-color: rgba(52, 211, 153, 0.25);
}

.nav-tab.active {
  color: #042618;
  background: linear-gradient(135deg, #34d399, #10b981);
  font-weight: 700;
  border-color: #6ee7b7;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
}

/* 主容器 */
main {
  flex: 1;
  max-width: 1400px;
  margin: 0 auto;
  padding: 24px 20px 60px 20px;
  width: 100%;
}

.tab-pane {
  display: none;
  animation: fadeIn 0.3s ease;
}

.tab-pane.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

/* 課本專題標準卡片 */
.textbook-section {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 18px;
  padding: 26px;
  margin-bottom: 26px;
  box-shadow: var(--shadow-card);
  backdrop-filter: blur(8px);
}

.tb-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid rgba(52, 211, 153, 0.25);
  padding-bottom: 16px;
  margin-bottom: 22px;
  flex-wrap: wrap;
  gap: 12px;
}

.tb-title {
  font-size: 1.55rem;
  font-weight: 800;
  color: var(--primary-light);
  display: flex;
  align-items: center;
  gap: 10px;
}

.tb-badge {
  background: rgba(16, 185, 129, 0.2);
  color: #34d399;
  border: 1px solid #10b981;
  font-size: 0.78rem;
  padding: 4px 12px;
  border-radius: 999px;
  font-weight: 600;
}

/* 網格系統 */
.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 20px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}

/* 資訊卡片 */
.info-card {
  background: rgba(5, 23, 17, 0.7);
  border: 1px solid rgba(52, 211, 153, 0.2);
  border-radius: 14px;
  padding: 18px;
  transition: all 0.25s ease;
}

.info-card:hover {
  border-color: var(--primary-light);
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(16, 185, 129, 0.2);
}

.info-card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}

.info-card-icon {
  width: 36px;
  height: 36px;
  background: rgba(16, 185, 129, 0.2);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
}

.info-card-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #a7f3d0;
}

.info-card p {
  color: var(--text-muted);
  line-height: 1.68;
  font-size: 0.95rem;
  margin-bottom: 8px;
}

.info-card p:last-child {
  margin-bottom: 0;
}

/* 重點條列與提示框 */
.highlight-box {
  background: rgba(251, 191, 36, 0.08);
  border-left: 4px solid var(--accent-gold);
  border-radius: 8px;
  padding: 14px 18px;
  margin: 16px 0;
}

.highlight-box h4 {
  color: var(--accent-gold);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.highlight-box p {
  color: #fef3c7;
  font-size: 0.95rem;
  line-height: 1.65;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 10px;
}

.tag-item {
  background: rgba(16, 185, 129, 0.18);
  color: #6ee7b7;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 600;
  border: 1px solid rgba(52, 211, 153, 0.25);
}

/* 互動 Canvas 容器 */
.sim-container {
  background: var(--canvas-bg);
  border: 1px solid rgba(52, 211, 153, 0.35);
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6);
  margin-bottom: 20px;
}

.sim-toolbar {
  background: rgba(6, 26, 19, 0.95);
  border-bottom: 1px solid rgba(52, 211, 153, 0.25);
  padding: 12px 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.sim-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--primary-light);
  display: flex;
  align-items: center;
  gap: 8px;
}

.sim-controls {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}

.btn-ctrl {
  background: rgba(16, 185, 129, 0.2);
  border: 1px solid var(--border-color);
  color: #ffffff;
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 0.88rem;
  cursor: pointer;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.btn-ctrl:hover {
  background: rgba(16, 185, 129, 0.4);
  border-color: #34d399;
}

.btn-ctrl.active {
  background: var(--primary);
  color: #031c12;
  font-weight: 700;
  border-color: #6ee7b7;
}

.sim-canvas-box {
  position: relative;
  width: 100%;
  height: 480px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #020f09;
}

canvas.interactive-canvas {
  width: 100%;
  height: 100%;
  display: block;
}

.sim-overlay-info {
  position: absolute;
  top: 14px;
  left: 14px;
  background: rgba(5, 23, 17, 0.85);
  border: 1px solid rgba(52, 211, 153, 0.35);
  border-radius: 10px;
  padding: 10px 14px;
  color: #ecfdf5;
  font-size: 0.88rem;
  pointer-events: none;
  backdrop-filter: blur(6px);
  max-width: 320px;
}

.sim-overlay-info h5 {
  color: var(--accent-gold);
  font-size: 0.95rem;
  margin-bottom: 4px;
}

/* 控制滑桿面板 */
.ctrl-panel {
  background: rgba(6, 26, 19, 0.9);
  padding: 14px 20px;
  border-top: 1px solid rgba(52, 211, 153, 0.2);
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.ctrl-item {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  min-width: 220px;
}

.ctrl-item label {
  font-size: 0.88rem;
  color: var(--text-muted);
  white-space: nowrap;
}

.ctrl-item input[type="range"] {
  flex: 1;
  accent-color: var(--primary);
  cursor: pointer;
}

.ctrl-val {
  font-family: monospace;
  font-weight: 700;
  color: var(--accent-gold);
  min-width: 48px;
  text-align: right;
  font-size: 0.92rem;
}

/* 隨堂測驗評量專區 */
.quiz-card {
  background: rgba(6, 25, 19, 0.9);
  border: 1px solid rgba(52, 211, 153, 0.25);
  border-radius: 14px;
  padding: 20px;
  margin-bottom: 18px;
  transition: all 0.25s;
}

.quiz-card.correct {
  border-color: #34d399;
  background: rgba(16, 185, 129, 0.12);
}

.quiz-card.wrong {
  border-color: #f87171;
  background: rgba(239, 68, 68, 0.12);
}

.quiz-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 14px;
}

.quiz-badge {
  background: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
  border: 1px solid rgba(56, 189, 248, 0.3);
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 700;
}

.quiz-title {
  font-size: 1.12rem;
  font-weight: 700;
  margin-bottom: 16px;
  line-height: 1.6;
  color: #ffffff;
}

.quiz-options {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
}

.quiz-opt {
  background: rgba(11, 38, 29, 0.8);
  border: 1px solid rgba(52, 211, 153, 0.2);
  border-radius: 10px;
  padding: 12px 18px;
  color: var(--text-main);
  text-align: left;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.95rem;
}

.quiz-opt:hover {
  background: rgba(16, 185, 129, 0.25);
  border-color: var(--primary-light);
  transform: translateX(4px);
}

.quiz-opt.selected-correct {
  background: #059669 !important;
  color: #ffffff !important;
  border-color: #34d399 !important;
  font-weight: 700;
}

.quiz-opt.selected-wrong {
  background: #dc2626 !important;
  color: #ffffff !important;
  border-color: #f87171 !important;
  font-weight: 700;
}

.quiz-opt.show-correct {
  border-color: #34d399 !important;
  background: rgba(16, 185, 129, 0.3) !important;
  font-weight: 700;
}

.quiz-feedback {
  margin-top: 14px;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 0.92rem;
  display: none;
  line-height: 1.6;
}

.quiz-feedback.show {
  display: block;
}

.feedback-correct {
  background: rgba(16, 185, 129, 0.2);
  border: 1px solid #10b981;
  color: #a7f3d0;
}

.feedback-wrong {
  background: rgba(239, 68, 68, 0.2);
  border: 1px solid #ef4444;
  color: #fca5a5;
}

/* 學習單列印專區 */
@media print {
  header, .nav-scroll-wrapper, .header-tools, .btn-ctrl, .sim-toolbar, .ctrl-panel, .no-print {
    display: none !important;
  }
  body {
    background: #ffffff !important;
    color: #000000 !important;
    font-size: 12pt !important;
  }
  .tab-pane {
    display: block !important;
    page-break-after: always;
  }
  .textbook-section, .info-card {
    border: 1px solid #999999 !important;
    background: #ffffff !important;
    box-shadow: none !important;
    color: #000000 !important;
    margin-bottom: 20px !important;
  }
  .tb-title, .info-card-title, h1, h2, h3, h4 {
    color: #000000 !important;
  }
  .tag-item, .quiz-badge, .tb-badge {
    border: 1px solid #666666 !important;
    color: #000000 !important;
    background: transparent !important;
  }
}

/* 影音觀察教室卡片樣式 */
.video-card {
  background: rgba(8, 28, 21, 0.85);
  border: 1px solid rgba(52, 211, 153, 0.25);
  border-radius: 14px;
  overflow: hidden;
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
}

.video-card:hover {
  transform: translateY(-4px);
  border-color: var(--primary-light);
  box-shadow: 0 10px 24px rgba(16, 185, 129, 0.25);
}

.video-thumb-wrap {
  position: relative;
  width: 100%;
  padding-top: 56.25%;
  background: #000;
  cursor: pointer;
  overflow: hidden;
}

.video-thumb {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.video-card:hover .video-thumb {
  transform: scale(1.05);
}

.video-play-badge {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 52px;
  height: 52px;
  background: rgba(16, 185, 129, 0.9);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  color: #fff;
  box-shadow: 0 0 18px rgba(0, 0, 0, 0.7);
  transition: transform 0.2s ease, background 0.2s ease;
}

.video-card:hover .video-play-badge {
  transform: translate(-50%, -50%) scale(1.15);
  background: #059669;
}

.video-info {
  padding: 16px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.video-tag {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 6px;
  margin-bottom: 8px;
  width: fit-content;
}

.video-tag.coastal {
  background: rgba(56, 189, 248, 0.2);
  color: #38bdf8;
  border: 1px solid rgba(56, 189, 248, 0.4);
}

.video-tag.alpine {
  background: rgba(251, 191, 36, 0.2);
  color: #fbbf24;
  border: 1px solid rgba(251, 191, 36, 0.4);
}

.video-title {
  font-size: 1.02rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 8px;
  line-height: 1.45;
}

.video-desc {
  font-size: 0.88rem;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 14px;
}

.video-actions {
  display: flex;
  gap: 8px;
  margin-top: auto;
}

.video-btn {
  flex: 1;
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 700;
  text-align: center;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  transition: all 0.2s;
  border: none;
}

.video-btn-play {
  background: var(--primary);
  color: #031c12;
}

.video-btn-play:hover {
  background: #34d399;
}

.video-btn-link {
  background: rgba(255, 255, 255, 0.1);
  color: #f1fdf6;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.video-btn-link:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
}

/* 頁尾 Footer */
footer {
  background: #020d08;
  border-top: 1px solid var(--border-color);
  padding: 24px 20px;
  text-align: center;
  color: var(--text-dim);
  font-size: 0.88rem;
  margin-top: auto;
}

footer a {
  color: var(--primary-light);
  text-decoration: none;
}

footer a:hover {
  text-decoration: underline;
}
"""

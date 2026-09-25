# -*- coding: utf-8 -*-
"""
翰林版國小自然五上第二單元《千變萬化的植物》互動教學網站生成程式
"""
import os
import sys

# 載入模組
from site_css import CSS_CONTENT
from site_content import CONTENT_HTML
from site_js import JS_CONTENT

output_dir = r"H:\其他電腦\我的電腦\暫存檔案資料夾\教學用\outputs\115-1_自然第二單元_課程計畫\千變萬化的植物互動教學網站"
target_html = os.path.join(output_dir, "index.html")

full_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>翰林國小自然五上第二單元：千變萬化的植物 旗艦互動教學系統</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>
{CSS_CONTENT}
</style>
</head>
<body>

<!-- 頂部 Header -->
<header>
  <div class="header-inner">
    <div class="brand">
      <div class="brand-icon">🌿</div>
      <div>
        <h1 class="site-title">千變萬化的植物</h1>
        <span class="site-subtitle">國小自然五上第二單元 • 翰林版 108 課綱旗艦互動教學系統</span>
      </div>
    </div>
    <div class="header-tools">
      <button class="btn-tool" id="btn-tv-mode" onclick="toggleTvMode()">📺 大電視投影模式</button>
      <button class="btn-tool" onclick="openQrModal()" style="border-color: #38bdf8; color: #38bdf8;">📱 學生掃碼</button>
      <button class="btn-tool" onclick="switchTab('tab-lesson')">📋 13節教案與學習單</button>
    </div>
  </div>

  <!-- QR Code 彈窗 -->
  <div id="qrModal" style="display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 9999; justify-content: center; align-items: center; padding: 20px;" onclick="if(event.target === this) closeQrModal()">
    <div style="background: #092018; border: 2px solid #10b981; border-radius: 16px; padding: 26px; max-width: 400px; width: 100%; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.8); position: relative;">
      <button onclick="closeQrModal()" style="position: absolute; top: 12px; right: 16px; background: transparent; border: none; color: #a7f3d0; font-size: 1.6rem; cursor: pointer;">&times;</button>
      <div style="font-size: 1.3rem; font-weight: 800; color: #34d399; margin-bottom: 6px;">📱 線上互動教學網站</div>
      <div style="font-size: 0.9rem; color: #a7f3d0; margin-bottom: 18px;">學生 iPad、Chromebook、手機掃描即開即學</div>
      <div style="background: #ffffff; padding: 14px; border-radius: 12px; display: inline-block; margin-bottom: 16px;">
        <img src="qrcode.svg" alt="千變萬化的植物 QR Code" style="width: 200px; height: 200px; display: block;">
      </div>
      <div style="font-size: 0.85rem; color: #cbd5e1; word-break: break-all; background: rgba(0,0,0,0.4); padding: 8px 12px; border-radius: 8px; margin-bottom: 16px; border: 1px solid rgba(52,211,153,0.3);">
        https://diberchi.github.io/grade5-plants-interactive/
      </div>
      <div style="display: flex; gap: 10px; justify-content: center;">
        <button onclick="copyUrl()" id="copyBtn" style="background: #10b981; color: #042618; border: none; padding: 9px 18px; border-radius: 8px; font-weight: 800; cursor: pointer;">📋 複製網址</button>
        <button onclick="closeQrModal()" style="background: #1e3a30; color: #a7f3d0; border: none; padding: 9px 18px; border-radius: 8px; font-weight: 700; cursor: pointer;">關閉</button>
      </div>
    </div>
  </div>

  <!-- 頂部水平滑動頁籤列（支援滾輪左右滾動） -->
  <div class="nav-scroll-wrapper">
    <div class="nav-tabs" id="main-nav-tabs">
      <button class="nav-tab active" data-tab="tab-intro" onclick="switchTab('tab-intro')">🌱 單元導讀總覽</button>
      <button class="nav-tab" data-tab="tab-2-1" onclick="switchTab('tab-2-1')">🌊 2-1 不同環境的植物</button>
      <button class="nav-tab" data-tab="tab-2-2" onclick="switchTab('tab-2-2')">💧 2-2 植物存活的本事</button>
      <button class="nav-tab" data-tab="tab-2-3" onclick="switchTab('tab-2-3')">🌸 2-3 植物繁衍大顯身手</button>
      <button class="nav-tab" data-tab="tab-2-4" onclick="switchTab('tab-2-4')">🔍 2-4 植物的特徵與分類</button>
      <button class="nav-tab" data-tab="tab-summary" onclick="switchTab('tab-summary')">📚 單元重點筆記</button>
      <button class="nav-tab" data-tab="tab-quiz" onclick="switchTab('tab-quiz')">🎯 10題隨堂搶答測驗</button>
      <button class="nav-tab" data-tab="tab-lesson" onclick="switchTab('tab-lesson')">📝 完整教案與列印學習單</button>
    </div>
  </div>
</header>

<!-- 主內容區 -->
<main>
{CONTENT_HTML}
</main>

<!-- 頁尾 -->
<footer>
  <p>國小自然五上第二單元《千變萬化的植物》互動教學系統 • 依據教育部 108 課綱與翰林版教材設計</p>
  <p style="margin-top: 6px; font-size: 0.82rem; opacity: 0.8;">純前端 HTML5 / Canvas / Web Audio 技術建置 • 免安裝任何套件 • 支援投影大電視與電子白板觸控互動</p>
</footer>

<!-- 互動邏輯 -->
<script>
{JS_CONTENT}
</script>

</body>
</html>
"""

with open(target_html, "w", encoding="utf-8") as f:
    f.write(full_html)

file_size_kb = os.path.getsize(target_html) / 1024
print(f"SUCCESS: Generated index.html, Size: {file_size_kb:.2f} KB")
print(f"Path: {target_html}")

#!/bin/bash
cd "$(dirname "$0")"
echo "=================================================="
echo " 正在啟動 國小自然五上第二單元《千變萬化的植物》互動教學網站..."
echo "=================================================="
echo "本機網址: http://localhost:8080"
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "127.0.0.1")
echo "平板/手機同網域連線網址: http://$IP:8080"
echo "--------------------------------------------------"
echo "正在自動開啟預設瀏覽器..."
open "http://localhost:8080"
python3 -m http.server 8080

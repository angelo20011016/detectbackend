
# 咖啡瑕疵豆雲端辨識專案

本專案以 YOLOv8 模型為核心，結合 FastAPI，並部署於 Azure Container Instance，提供即時的咖啡瑕疵豆圖片辨識雲端 API。前端以 HTML/CSS/JS 製作，並可部署於 Render、Vercel 等靜態主機。

## 專案架構

- **前端**：HTML + CSS + JavaScript，支援圖片上傳與結果顯示
- **後端**：FastAPI + YOLOv8，Docker 化並部署於 Azure ACI
- **雲端**：Azure Container Registry 儲存映像檔，ACI 執行推論服務

## 使用方式

1. 上傳圖片（jpg/png）
2. 送出後，API 會回傳辨識結果
3. 支援雲端部署，前後端完全分離

## 快速體驗

- [線上 Demo](https://你的render網址)
- [API 端點](http://coffee.cbggdwdqf4brgudc.eastasia.azurecontainer.io:8000/predict)

## 技術重點

- YOLOv8 目標偵測模型訓練與推論
- FastAPI RESTful API 開發
- Docker 跨平台（Mac ARM → Azure x86）建置
- Azure ACR/ACI 雲端部署
- CORS 問題處理與前後端分離架構

## 部署流程

1. 本地開發與測試 FastAPI + YOLOv8
2. Docker 化，並用 buildx 編譯 amd64 映像檔
3. 登入 Azure CLI，push image 至 ACR
4. 在 Azure Portal 建立 ACI，設定公開 port 8000 與 DNS 名稱
5. 前端網頁部署於 Render，並串接 API
6. 完成雲端辨識服務

## 專案心得

本專案完整實踐了 AI 模型雲端化、前後端分離、跨平台部署等現代工程流程，並克服了 Mac ARM/x86 架構差異、CORS、雲端權限等常見問題，適合用於作品集或面試展示。

---

> 作者：Angelo  
> 技術：YOLOv8、FastAPI、Docker、Azure、HTML/CSS/JS
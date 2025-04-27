from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
import io
# filepath: /Users/angelo/Downloads/archive/main.py
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開發階段允許所有來源，正式上線可改成你的前端網址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = YOLO("yolov8n.pt") # 請確認 best-2.pt 跟 main.py 在同一個資料夾

class_names = [
    'Broken', 'Cut', 'Dry Cherry', 'Fade', 'Floater', 'Full Black', 'Full Sour',
    'Fungus Damange', 'Husk', 'Immature', 'Parchment', 'Partial Black',
    'Partial Sour', 'Severe Insect Damange', 'Shell', 'Slight Insect Damage', 'Withered'
]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    results = model(image)
    if len(results[0].boxes.cls) == 0:
        return JSONResponse({"result": "No object detected"})
    pred_class = int(results[0].boxes.cls[0])
    pred_name = class_names[pred_class]
    return JSONResponse({"result": pred_name})
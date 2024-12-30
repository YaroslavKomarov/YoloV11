from fastapi import FastAPI, File, UploadFile
import uvicorn
from yolo_prediction import yolo_predict

app = FastAPI()

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    image_data = await file.read()

    return yolo_predict(image_data)
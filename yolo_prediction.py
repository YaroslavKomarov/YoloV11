from ultralytics import YOLO
from PIL import Image
import io


def yolo_predict(image_data):
    image = Image.open(io.BytesIO(image_data))
    model = YOLO("yolo11n.pt")
    predictions = model.predict(image)

    return {model.names[int(cls)] for cls in predictions[0].boxes.cls}
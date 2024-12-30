Установить зависимости:
```
pip install -r requirements.txt
```
Выбрать нужную конфигурацию железа и установить torch: https://pytorch.org/get-started/locally/

Запустить приложение на 8001 порту:
```
uvicorn yolo_api:app --host 127.0.0.1 --port 8001
```

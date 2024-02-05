from Ultralytics import YOLO

model = YOLO('yolov8n.yaml')

model.train('data.yaml', epoch = 100)

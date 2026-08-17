from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model - dataset will auto-download on first run
results = model.train(data="VisDrone.yaml", epochs=5, imgsz=640)
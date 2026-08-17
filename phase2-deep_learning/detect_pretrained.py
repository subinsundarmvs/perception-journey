# detect_pretrained.py -- run a PRETRAINED YOLO detector (no training needed).
# It already knows 80 everyday object classes (person, car, dog, chair, cup, ...)
# from being trained on the COCO dataset. We're just USING it here.
from ultralytics import YOLO

# Load a small, fast pretrained model. First run downloads the weights (~6 MB).
# "yolov8n" = YOLOv8 "nano" -- smallest/fastest; good for a laptop.
model = YOLO("yolov8n.pt")

# ---- Option A: run on a single image ----
# Put any photo with people/cars/objects next to this script as "test.jpg"
results = model("/Users/subin/Perception-journey/perception-journey/phase2-deep_learning/subject.jpeg")          # returns detections for the image

# results[0] holds everything found in the first (only) image
r = results[0]
print(f"objects detected: {len(r.boxes)}")
for box in r.boxes:
    cls_id = int(box.cls[0])                 # which class (index into model.names)
    conf   = float(box.conf[0])              # confidence 0-1
    xyxy   = box.xyxy[0].tolist()            # box corners [x1, y1, x2, y2]
    print(f"  {model.names[cls_id]:12s} conf={conf:.2f}  box={[round(v) for v in xyxy]}")

# Draw the labeled boxes and save the annotated image
r.save(filename="test_detected.jpg")         # writes an image WITH boxes drawn
print("saved test_detected.jpg -- open it to see the boxes")
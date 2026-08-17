# live webcam detection -- boxes drawn on your camera feed in real time
import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)    # detect on this frame
    annotated = results[0].plot()            # draw boxes+labels onto the frame

    cv2.imshow("YOLO live", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
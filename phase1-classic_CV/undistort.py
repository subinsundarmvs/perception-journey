import cv2
import numpy as np

data = np.load("camera_params.npz")     # load YOUR measured camera
K, dist = data["K"], data["dist"]

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Remove the lens distortion using your measured coefficients
    undistorted = cv2.undistort(frame, K, dist, None, K)

    # Show original and corrected side by side to SEE the difference
    combined = np.hstack([frame, undistorted])
    combined = cv2.resize(combined, (1600, 450))   # shrink so both fit on screen
    cv2.putText(combined, "ORIGINAL", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(combined, "UNDISTORTED", (820, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("distortion correction", combined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
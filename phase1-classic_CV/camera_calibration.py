import cv2
import numpy as np

CHESSBOARD = (8, 5)          # your confirmed board size
SQUARE = 1.0                 # 1 unit per square (use real cm later for metric poses)

# --- Build the board's real-world corner grid ONCE (all Z=0, it's flat) ---
objp = np.zeros((CHESSBOARD[0] * CHESSBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHESSBOARD[0], 0:CHESSBOARD[1]].T.reshape(-1, 2) * SQUARE

objpoints = []   # 3D real-world points, one entry per captured view
imgpoints = []   # 2D detected pixel corners, one entry per captured view

cap = cv2.VideoCapture(1)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

print("SPACE = capture a view (when grid locks on) | c = calibrate | q = quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    found, corners = cv2.findChessboardCornersSB(gray, CHESSBOARD, None)

    if found:
        cv2.drawChessboardCorners(frame, CHESSBOARD, corners, found)
    cv2.putText(frame, f"captured: {len(objpoints)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("calibrate", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord(' ') and found:                     # capture this view
        corners_refined = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        objpoints.append(objp)
        imgpoints.append(corners_refined)
        print(f"captured view {len(objpoints)}")
    elif key == ord('c'):                             # solve
        break
    elif key == ord('q'):
        cap.release(); cv2.destroyAllWindows(); exit()

cap.release()
cv2.destroyAllWindows()

# --- THE SOLVE: many views of a known board -> the real camera ---
ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None)

print("\n=== YOUR CAMERA ===")
print("Reprojection error (lower is better, <1.0 is good):", ret)
print("Camera matrix K:\n", K)
print("Distortion coefficients:\n", dist.ravel())

np.savez("camera_params.npz", K=K, dist=dist)   # save for AR / pose later
print("\nSaved to camera_params.npz")
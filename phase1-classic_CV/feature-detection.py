import cv2

img = cv2.imread("ss1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # corners live in brightness, not color

orb = cv2.ORB_create(nfeatures=50)              # find up to 500 keypoints
keypoints = orb.detect(gray, None)               # STAGE 1: where are the corners?
keypoints, descriptors = orb.compute(gray, keypoints)  # STAGE 2: fingerprint each one

print("keypoints found:", len(keypoints))
print("descriptor shape:", descriptors.shape)    # (N, 32) -> 32-byte fingerprint each

# draw the detected keypoints (size = scale, line = orientation)
vis = cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0),
                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("ORB keypoints", vis)

cv2.waitKey(5000)
cv2.destroyAllWindows()
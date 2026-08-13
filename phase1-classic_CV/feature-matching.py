import cv2

img1 = cv2.imread("ss3.jpeg")
img2 = cv2.imread("ss4.jpeg")
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(nfeatures=1)
kp1, des1 = orb.detectAndCompute(gray1, None)   # detect + describe, image 1
kp2, des2 = orb.detectAndCompute(gray2, None)   # detect + describe, image 2

# Match fingerprints by Hamming distance (bit differences); crossCheck keeps only
# pairs that pick EACH OTHER as best match -> fewer false matches.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort by quality (smaller distance = better) and keep the best ones
matches = sorted(matches, key=lambda m: m.distance)
good = matches[:40]                              # top 40 matches

print(f"kp1: {len(kp1)} | kp2: {len(kp2)} | total matches: {len(matches)}")

vis = cv2.drawMatches(img1, kp1, img2, kp2, good, None,
                      flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow("matches", vis)
cv2.waitKey(10000)
cv2.destroyAllWindows()
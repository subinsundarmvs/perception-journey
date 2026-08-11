import cv2
import numpy as np


cap = cv2.VideoCapture(1)          # your working index

while True:                        # the video loop — runs ~30x per second
    ret, frame = cap.read()        # grab ONE frame (an array)
    if not ret:                    # if the grab failed, bail out
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (3, 3), 0)   # smooth out pixel noise first


    # --- MASK: keep only pixels whose color falls in our target range ---
    # OpenCV hue is 0-179. Red is tricky: it wraps around both ends of the hue
    # circle, so we need TWO ranges and combine them. (Start with red; we'll tune.)
    lower1 = np.array([0,   120, 70])
    upper1 = np.array([10,  255, 255])
    lower2 = np.array([170, 120, 70])
    upper2 = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower1, upper1) | cv2.inRange(hsv, lower2, upper2)

    # ... build mask as before ...

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)    # erase tiny specks
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)   # fill small holes
    # mask is now a 2D array: 255 where the color matched, 0 everywhere else.

    # --- LOCATE: find the outline(s) of the white regions in the mask ---
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  

    if contours:
        # pick the BIGGEST white blob — assume that's our object, not stray specks
        biggest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(biggest) > 500:      # ignore tiny noise blobs
            x, y, w, h = cv2.boundingRect(biggest)          # box around it
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # draw green box
            cv2.putText(frame, "tracking", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Live", frame)
    cv2.imshow("Mask", mask)   

    # waitKey(1) = wait 1ms for a keypress. It ALSO gives the window time to
    # redraw — without it, the window freezes. This one line does double duty.
    if cv2.waitKey(1) & 0xFF == ord('q'):   # press 'q' to quit
        break

cap.release()                      # let go of the camera
cv2.destroyAllWindows()            # close the window
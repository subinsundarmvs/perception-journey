import numpy as np
import cv2

# An image is just a 3D array: height x width x 3 color channels (Blue, Green, Red).
# Let's MANUFACTURE one from pure numbers — start with all zeros (black).
img = np.zeros((200, 300, 3), dtype=np.uint16)

print("Shape:", img.shape)      # (200, 300, 3) -> 200 rows, 300 cols, 3 channels
print("One pixel:", img[0, 0])  # [0 0 0] -> black

# Paint a red rectangle by setting those pixels' numbers directly.
# OpenCV uses Blue-Green-Red order, so red is [0, 0, 255].
img[0:150, 0:200] = [0, 0, 255]



# cv2.imwrite("first_image.png", img)  # save the numbers as an image file
print("Saved first_image.png")



img1 = cv2.imread("first_image.png")   # reads the file into a numpy array

print("Type:", type(img1))       # numpy.ndarray -> same thing as before
print("Shape:", img1.shape)      # (height, width, 3)
print("Dtype:", img1.dtype)      # uint8 -> each number is 0..255
print("Top-left pixel:", img1[0, 0])  # three numbers: one pixel's color

import matplotlib.pyplot as plt

# Split the three channels. Each is a 2D grid of one color's intensity.
blue  = img[0:1, 0:1, 0]
green = img[:, :, 1]
red   = img[:, :, 2]
print(blue)

plt.imshow(img)
plt.title("Corrected colors one")
# plt.show()

print("One channel shape:", blue.shape)  # (H, W) -> just a 2D number-grid


# matplotlib expects R,G,B order, so convert before showing.
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("Gray shape:", gray.shape)  # (H, W) -> no color channel anymore
cv2.imwrite("photo_gray.png", gray)


plt.imshow(img_rgb)
plt.title("Corrected colors")
# plt.show()

h, w = gray.shape
center_crop = img_rgb[h//4 : 3*h//4, w//4 : 3*w//4]  # keep the middle box

plt.imshow(center_crop)

plt.title("Cropped middle")
# plt.show()

img = cv2.imread("ss.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Try to brighten by adding 50 to every pixel.
brighter_wrong = img_rgb + 44      # looks innocent...

plt.imshow(brighter_wrong)
plt.title("Brighter? (the trap)")
# plt.show()

# int16 has room for values above 255; np.clip caps them; then back to uint8.
brighter = np.clip(img_rgb.astype(np.int16) + 50, 0, 255).astype(np.uint8)

plt.imshow(brighter)
plt.title("Brighter (done right)")
plt.show()

warm = img_rgb.astype(np.int16)
warm[:, :, 0] += 60                       # channel 0 is Red in RGB -> warmer
# warm = np.clip(warm, 0, 255).astype(np.uint8)

plt.imshow(warm)
plt.title("Warmer (red boosted)")
plt.show()
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("ss.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rows,cols = img.shape[:2]
print( "rows ", img.shape, "cols" , cols )

tx, ty ,tz= 40, 250 ,200  # shift 40 right, 25 down
M_translate = np.float32([[1, 0, tx],
                          [0, 1, ty]])

# warpAffine applies matrix M to pixel POSITIONS and paints the result.
# The size argument is (width, height) -- NOT (height, width). Another convention trap.
shifted = cv2.warpAffine(img, M_translate, (cols, rows))

plt.imshow(shifted); 
plt.title("Translated"); 
# plt.show()

angle = 45
# getRotationMatrix2D(center, angle, scale) builds the 2x3 matrix for us.
M_rot_corner = cv2.getRotationMatrix2D((0, 0), angle, 1.0)   # rotate about top-left
print(M_rot_corner)
rotated_corner = cv2.warpAffine(img, M_rot_corner, (cols, rows))

plt.imshow(rotated_corner); 
plt.title("Rotated about corner (trap)"); 
plt.show()

M_r = cv2.getRotationMatrix2D((cols/2, rows/2), 30, 1.0)

# To combine two 2x3 affine matrices we lift them to 3x3, multiply, then drop back.
def to_3x3(M):
    return np.vstack([M, [0, 0, 1]])

M_t = np.float32([[1, 0, 60],
                  [0, 1, 0]])         # shift 60 right

# Version A: rotate FIRST, then translate  ->  T · R
A = to_3x3(M_t) @ to_3x3(M_r)
# Version B: translate FIRST, then rotate  ->  R · T
B = to_3x3(M_r) @ to_3x3(M_t)

outA = cv2.warpAffine(img, A[:2], (cols, rows))
outB = cv2.warpAffine(img, B[:2], (cols, rows))

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].imshow(outA); ax[0].set_title("rotate then translate")
ax[1].imshow(outB); ax[1].set_title("translate then rotate")
plt.show()
import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y))
print(x + y)

img1 = cv2.imread("lena.jpg", 0)
img2 = cv2.imread("lena_w.jpg")
res = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)
cv2.imshow("res", res)


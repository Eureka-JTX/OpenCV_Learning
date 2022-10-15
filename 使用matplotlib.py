import cv2
import matplotlib.pyplot as plt

img = cv2.imread("lena.jpg")
plt.imshow(img, cmap="gray")
img2 = img[:, :, ::-1]
plt.imshow(img2)
plt.show()


import cv2

img = cv2.imread("lena.jpg")
blur = cv2.blur(img, (3, 3))
gaussian = cv2.GaussianBlur(img, (5, 5), 1)
blur2 = cv2.bilateralFilter(img, 9, 75, 75)  # 双边滤波
cv2.imshow("blur", blur)
cv2.waitKey(0)

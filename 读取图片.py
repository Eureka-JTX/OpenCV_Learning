import cv2

img = cv2.imread('lena.jpg', 0)
cv2.namedWindow('lena', cv2.WINDOW_NORMAL)
cv2.imshow('lena', img)
cv2.waitKey(0)
cv2.imwrite('lena_w.jpg', img)

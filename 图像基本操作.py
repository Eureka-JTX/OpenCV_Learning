import cv2

# 像素
img = cv2.imread("lena.jpg")
px = img[100, 90]
print(px)
px_blue = img[100, 90, 0]
print(px_blue)

# 图片属性
print(img.shape)
height, width, channels = img.shape
print(img.dtype)
print(img.size)

# ROI
face = img[100:200, 115:188]
cv2.imshow("face", face)
cv2.waitKey(0)

# BGR
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
b = img[:, :, 0]
cv2.imshow("blue", b)
cv2.waitKey(0)

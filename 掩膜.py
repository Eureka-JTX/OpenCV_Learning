import cv2

img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('opencv.png')

# 把logo放在左上角，所以我们只关心这一块区域
rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]

# 创建掩膜
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)

# 保留除logo外的背景
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
cv2.imshow("dst", img1_bg)
cv2.waitKey(0)
dst = cv2.add(img1_bg, img2)  # 进行融合
img1[:rows, :cols] = dst  # 融合后放在原图上
cv2.imshow("dst", img1)
cv2.waitKey(0)

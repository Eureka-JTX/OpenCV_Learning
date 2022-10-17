import cv2
import numpy as np

# 读入灰度图0
img = cv2.imread("dao-bin.png", flags=cv2.IMREAD_GRAYSCALE)

# 创建 核
kernel = np.ones((5, 5), np.uint8)
# 腐蚀
erorsion_img = cv2.erode(img, kernel, iterations=1)

cv2.imwrite('dao_erorsion_k5.png', np.hstack((img, erorsion_img)))

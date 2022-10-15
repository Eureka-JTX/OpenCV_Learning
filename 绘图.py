import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (512, 512), (0, 255, 255), 10)
cv2.rectangle(img, (234, 21), (500, 222), (255, 255, 0), 5)
cv2.circle(img, (256, 256), 100, (255, 0, 255), 8)
cv2.ellipse(img, (256, 256), (100, 50), 10, 10, 350, (255, 255, 255), -1)
pts = np.array([[10, 5], [40, 20], [90, 88], [344, 99], [224, 500]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 0))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Arsenever", (10, 100), font, 2, (101, 156, 50), 4, lineType=cv2.LINE_AA)
cv2.imshow("img", img)
cv2.waitKey(0)

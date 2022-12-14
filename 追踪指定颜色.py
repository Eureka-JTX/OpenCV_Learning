import numpy as np
import cv2

cap = cv2.VideoCapture(0)
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # inRange()：介于lower / upper之间的为白色，其余黑色
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    if cv2.waitKey(1) == ord('q'):
        break

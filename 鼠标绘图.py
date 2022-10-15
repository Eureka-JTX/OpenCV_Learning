import cv2
import numpy as np

drawing = False
mode = True
start = (-1, -1)


def mouse_event(event, x, y, flags, param):
    global start, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, start, (x, y), (255, 0, 0), 1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, start, (x, y), (255, 0, 0), 1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("img")
cv2.setMouseCallback('img', mouse_event)

while True:
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord('m'):
        mode = not mode
    elif cv2.waitKey(1) == 27:
        break

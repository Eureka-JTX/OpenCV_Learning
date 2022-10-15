import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
output = cv2.VideoWriter('output.avi', fourcc, 30., (640, 480))
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        output.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

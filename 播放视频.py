import cv2

cap = cv2.VideoCapture("kball.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    if cv2.waitKey(30) == ord('q'):
        break

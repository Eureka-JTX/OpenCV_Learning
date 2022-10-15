import cv2

cap = cv2.VideoCapture(0)
width, height = cap.get(3), cap.get(4)
print(width, height)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2 * width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2 * height)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) == ord('q'):
        break

import cv2

img = cv2.imread("lena.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.imshow("img", img)
cv2.waitKey(0)

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
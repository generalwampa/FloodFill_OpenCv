import cv2
import floodfill

img = cv2.imread("maze_sample.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
img = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
test = [280, 70]
floodfill.fill(img, test, (255, 255, 255))
cv2.imwrite("fill.png", img)

import threading
import os
import cv2
import floodfill

os.environ['DISPLAY'] = ":0"

start = ()
flag = False


def disp():
    global img
    cv2.imshow("Image", img)
    cv2.setMouseCallback('Image', mouse_event)
    while True:
        cv2.imshow("Image", img)
        cv2.waitKey(1)


def mouse_event(event, pX, pY, flags, param):
    global img, start, flag
    if event == cv2.EVENT_LBUTTONUP:
        start = (pX, pY)
        flag = True


img = cv2.imread("maze_sample.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

t = threading.Thread(target=disp, args=())
t.daemon = True
t.start()

while not flag:
    pass

floodfill.fill(img, start, (255, 255, 255))
cv2.waitKey(0)

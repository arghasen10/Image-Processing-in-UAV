import cv2
import numpy as np

hmin=0
hmax=0
smin=0
smax=0
vmin=0
vmax=0
def hminc(x):
    hmin = x
def hmaxc(x):
    hmax = x
def sminc(x):
    smin = x
def smaxc(x):
    smax = x
def vminc(x):
    vmin = x
def vmaxc(x):
    vmax= x
lower_green = np.array([hmin,smin,vmin])
upper_green = np.array([hmax,smax,vmax])
cv2.namedWindow("frame1",50)
cv2.createTrackbar("hmin","frame1",50,255,hminc)
cv2.createTrackbar("hmax","frame1",50,255,hmaxc)
cv2.createTrackbar("smin","frame1",50,255,sminc)
cv2.createTrackbar("smax","frame1",50,255,smaxc)
cv2.createTrackbar("vmin","frame1",50,255,vminc)
cv2.createTrackbar("vmax","frame1",50,255,vmaxc)
cap = cv2.VideoCapture('video1.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture('video1.mp4')
        ret, frame = cap.read()
        continue
    hmin = cv2.getTrackbarPos("hmin","frame1")
    hmax = cv2.getTrackbarPos("hmax","frame1")
    smin = cv2.getTrackbarPos("smin","frame1")
    smax = cv2.getTrackbarPos("smax","frame1")
    vmin = cv2.getTrackbarPos("vmin","frame1")
    vmax = cv2.getTrackbarPos("vmax","frame1")
    lower_green = np.array([hmin, smin, vmin])
    upper_green = np.array([hmax, smax, vmax])
    frame = cv2.rotate(frame,0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    kernel = np.ones((5, 5), np.int)
    dilated = cv2.dilate(mask, kernel)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    ret, thrshed = cv2.threshold(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY), 3, 255, cv2.THRESH_BINARY)

    cv2.imshow('thresh', thrshed)
    cv2.imshow('res', res)
    cv2.imshow('hsv', hsv)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    k = cv2.waitKey(27) & 0xFF
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np


lower_green = np.array([51,14,26])
upper_green = np.array([229,173,55])

cap = cv2.VideoCapture('video1.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture('video1.mp4')
        ret, frame = cap.read()
        continue
    frame = cv2.rotate(frame,0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    kernel = np.ones((5, 5), np.int)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    ret, thrshed = cv2.threshold(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY), 3, 255, cv2.THRESH_BINARY)
    opening = cv2.morphologyEx(thrshed, cv2.MORPH_OPEN, kernel)
    dilated = cv2.dilate(opening, kernel,iterations=5)
    im2, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    for contour in contours:
        area = cv2.contourArea(contour)
        (x, y, w, h) = cv2.boundingRect(contour)

        if area < 4000:
            continue
        if area > 12000:
            continue
        if h < 105:
            continue
        if w > 140:
            continue
        cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
        cv2.putText(frame,str(w)+","+str(h),(x,y),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,255,255),thickness=2)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(27) & 0xFF
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

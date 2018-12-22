import cv2
import numpy as np
cap = cv2.VideoCapture('Trimmed.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 25,(854,480))
lower_black = np.array([0,0,0])
upper_black = np.array([180,255,40])
while True:
    ret ,frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_black, upper_black)
    kernel = np.ones((5,5),np.int)
    dilated = cv2.dilate(mask, kernel)
    closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    res = cv2.bitwise_and(frame, frame, mask=closing)
    ret, thrshed = cv2.threshold(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY), 3, 255, cv2.THRESH_BINARY)
    im2, contours, hierarchy = cv2.findContours(thrshed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 2000:
            continue
        if area > 4000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        if w<30:
            continue
        if w > 100:
            continue
        if h<30:
            continue
        if h>100:
            continue
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        out.write(frame)
    cv2.imshow('thresh',thrshed)
    cv2.imshow('res',res)

    cv2.imshow('hsv',hsv)
    cv2.imshow('frame',frame)
    
    k = cv2.waitKey(27) & 0xFF
    if k == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()

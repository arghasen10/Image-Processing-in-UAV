import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('tree_counted.avi', fourcc, 30,(352,640))

lower_green = np.array([51,14,26])
upper_green = np.array([229,173,55])
count=0
cap = cv2.VideoCapture('video1.mp4')
while True:
    ret, frame = cap.read()
    if not ret:

        break
    frame = cv2.rotate(frame,0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    kernel = np.ones((5, 5), np.int)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    ret, thrshed = cv2.threshold(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY), 3, 255, cv2.THRESH_BINARY)
    opening = cv2.morphologyEx(thrshed, cv2.MORPH_OPEN, kernel)
    dilated = cv2.dilate(opening, kernel,iterations=5)
    im2, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.line(frame,(75,0),(75,frame.shape[0]),(255,0,0),2)
    cv2.putText(frame, str(count), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
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
        X_val = int(x+w/2)
        Y_val = int(y+h/2)
        center = (X_val,Y_val)

        cv2.circle(frame,center,2,(0,0,255),2)
        if(X_val>72.5 and X_val <77):
            count+=1
            cv2.line(frame, (75, 0), (75, frame.shape[0]), (0, 0, 0), 2)
    out.write(frame)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(27) & 0xFF
    if k == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()

import cv2

cam = cv2.VideoCapture('car.mp4')
detector = cv2.CascadeClassifier('cars3.xml')

while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    cv2.line(img, (0,170), (img.shape[1],170), (255, 0, 0), 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        X_val = int(x + w / 2)
        Y_val = int(y + h / 2)
        center = (X_val, Y_val)
    cv2.imshow('frame', img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

import RPi.GPIO as GPIO
import time
import picamera
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_dowm = GPIO.PUD_UP)


def picamerause(num):
    camera=picamera.PiCamera()
    camera.resolution = (640, 480)
    #camera.capture('image'+str(num)+'.jpg')
    #time.sleep(1)
    camera.start_recording('video'+str(num)+'.h264')
    time.sleep(5)   #Video for 5s
    camera.stop_recording()
    time.sleep(1)
    #camera.capture('image'+str(num+1)+'.jpg')
    camera.close()
num=0

while True:
    input_state = GPIO.input(18)
    
    num=num+1
    if inout_state == False:
        print('Button Pressed')
        time.sleep(0.2)
        picamerause(num)

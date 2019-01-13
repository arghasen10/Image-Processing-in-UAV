
import serial
import time

ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
ser.flushOutput()

ser2 = serial.Serial('/dev/ttyMCC',115200,timeout = 1)
ser.flushOutput()
 
while True:
   x=ser.readline()
   y = ser2.readline()

   if x is  '':
      continue
   if y is '':
      continue

   x = x.strip()
   y = y.strip()
   print(x,y)
   #x = x.split(',')
   #print('PM1 = ',x[0],'PM2.5 = ',x[1],'PM10 = ',x[2],'CO2 = ',x[-1])

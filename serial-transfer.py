
import serial
import time

ser = serial.Serial('/dev/ttymxc3',115200,timeout=1)
ser.flushOutput()

while True:
   x=ser.readline()

   if x is  '':
      continue
   x = x.strip()
   print(x)
   x = x.split(',')
   print('PM1 = ',x[0],'PM2.5 = ',x[1],'PM10 = ',x[2],'CO2 = ',x[-1])

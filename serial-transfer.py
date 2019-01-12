
import serial
import time

ser = serial.Serial('/dev/ttymxc3',115200,timeout=1)
ser.flushOutput()

while True:
   x=ser.readline()

   if x is  '':
      continue

   print(x.strip())

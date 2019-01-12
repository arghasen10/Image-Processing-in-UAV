import time
import serial
import csv
import datetime

currenttime = datetime.datetime.now()
print(str(currenttime))
print('Started Receiving from Arduino.....')

ser = serial.Serial('/dev/ttymxc3',115200,timeout=1)
ser.flushOutput()
counter=0

currenttime = datetime.datetime.now()
currenttime = str(currenttime)
currenttime_array = currenttime.split(' ')
time = currenttime_array[1][:8]
filename = time
filename+='.csv'

with open(filename, 'w+') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Date","Time","PM1","PM2.5","PM10","CO2"])
    
    
while True:
   x=ser.readline()

   if x is  '':
      continue
   currenttime = datetime.datetime.now()
   currenttime = str(currenttime)
   currenttime_array = currenttime.split(' ')
   date = currenttime_array[0]
   time = currenttime_array[1][:8]
   x = x.strip()
   x = x.split(',')
   PM1 = int(x[0])
   PM2_5 = int(x[1])
   PM10 = int(x[2])
   CO2 = int(x[-1])
   print(date,time,PM1,PM2_5,PM10,CO2)
   with open(filename, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([date,time,PM1,PM2_5,PM10,CO2])

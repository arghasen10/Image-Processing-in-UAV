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


with open('satya_sensor_data.csv', 'w+') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Date","Time","CO2"])
    
    
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
   print(date,time,x)
   with open('satya_sensor_data.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([date, time,x])

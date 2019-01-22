import time as Tmodule
import serial
import csv
import datetime

currenttime = datetime.datetime.now()
print(str(currenttime))
print('Started Receiving from Arduino.....')

ser = serial.Serial('/dev/ttyMCC',115200,timeout=1)
ser.flushOutput()
counter=0

currenttime = datetime.datetime.now()
currenttime = str(currenttime)
currenttime_array = currenttime.split(' ')
date = currenttime_array[0]
time = currenttime_array[1][:8]
filename = time
filename+='_'
filename+= date 
filename+='.csv'
print('Name of File created :',filename)

with open(filename, 'w+') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Date","Time","PM1","PM2.5","PM10","NO2","CO2","CO","Humidity","Temperature"])
    
#print('[INFO] Waiting for 10s to set the serial communication working properly...')
#Tmodule.sleep(10)    

while True:
   x=ser.readline()

   if x is  '':
      continue
   currenttime = datetime.datetime.now()
   currenttime = str(currenttime)
   currenttime_array = currenttime.split(' ')
   date = currenttime_array[0]
   time = currenttime_array[1][:8]
   x = x.strip().split(',')
   if len(x)<8:
	continue
   '''x = x.split(',')
   PM1 = float(x[0])
   PM2_5 = float(x[1])
   PM10 = float(x[2])
   NO2 = float(x[3])
   CO2 = float(x[4])
   CO = float(x[5])
   humi = float(x[6])

   temp = float(x[7])'''
   PM1,PM2_5,PM10,NO2,CO2,CO,humi,temp=map(float,x)
   print(date,time,PM1,PM2_5,PM10,NO2,CO2,CO,humi,temp)
   with open(filename, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([date,time,PM1,PM2_5,PM10,CO2,humi,temp])

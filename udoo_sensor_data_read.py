import time as Tmodule
import serial
import csv,os
import datetime

currenttime = datetime.datetime.now()
#print(str(currenttime))
#print('Started Receiving from Arduino.....')

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

print('[INFO] Name of File created : '+filename)

filename = os.path.join('/home/udooer/Desktop/aetdrone/Image-Processing-in-UAV/new_output',filename)

with open(filename, 'w+') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Date","Time","PM1","PM2.5","PM10","NO2","CO2","CO","Humidity","Temperature"])

#file1 = open("/gpio/pin25/value","r")
#t_old = file1.read()
#t_old = int(t_old)

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

   PM1,PM2_5,PM10,NO2,CO2,CO,humi,temp=map(float,x)

   #file1 = open("/gpio/pin25/value","r")
   #t = file1.read()
   #t = int(t)
   #file3 = open("/gpio/pin21/value","w")
   #if(t==1):
#       file3.write("0\n")
 #  elif(t==0):
#       file3.write("1\n")

 #  if(t!=t_old):
#       print("[INFO] Stopped by hardware Interrupt")
#       break

   #file = open("/gpio/pin22/value","w")
   #file.write("1\n")
   #file.close()
   Tmodule.sleep(0.1)
   print('[INFO] Date '+date+'  ,Time '+time+'  ,PM1 '+str(PM1)+'  ,PM2_5 '+str(PM2_5)+'  ,PM10 '+str(PM10)+'  ,NO2 '+str(NO2)+'  ,CO2 '+str(CO2)+'  ,CO '+str(CO)+'  ,$
   with open(filename, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([date,time,PM1,PM2_5,PM10,NO2,CO2,CO,humi,temp])
  # file = open("/gpio/pin22/value","w")
  # file.write("0\n")
   #file.close()
   #file1.close()
  # file3.close()



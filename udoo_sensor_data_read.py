import time
import serial
import csv

ser = serial.Serial(
  
   port='/dev/ttyUSB0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
counter=0


with open('sensor_data.csv', 'w+') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Latitude", "Longitude","start_time","end_time","PM1","PM2.5","PM10","NO2","CO2","CO","Humidity","Temperature"])
    
    
while 1:
   x=ser.readline()
   sensor_data = x.split(',')
   Latitude = sensor_data[0]
   Longitude = sensor_data[1]
   start_time = sensor_data[2]
   end_time = sensor_data[3]
   PM1 = sensor_data[4]
   PM2.5 = sensor_data[5]
   PM10 = sensor_data[6]
   NO2 = sensor_data[7]
   CO2 = sensor_data[8]
   CO = sensor_data[9]
   Humidity = sensor_data[10]
   Temperature = sensor_data[11]
   with open('sensor_data.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([Latitude, Longitude,start_time,end_time,PM1,PM2.5,PM10,NO2,CO2,CO,Humidity,Temperature])

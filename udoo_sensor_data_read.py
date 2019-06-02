import time as tm
import serial
import csv
import datetime
import drone_server as ds

currenttime = datetime.datetime.now()
print(str(currenttime))
print('Started Receiving from Arduino.....')

ser = serial.Serial('/dev/ttyMCC',115200,timeout=1)
ser.flushOutput()

ds.socket_create()
ds.socket_bind()
conn = ds.accept_connections()

currenttime = datetime.datetime.now()
currenttime = str(currenttime)
currenttime_array = currenttime.split(' ')
date = currenttime_array[0]
time = currenttime_array[1][:8]
mode = time.split(':')
s1 = int(mode[0])
s2 = int(mode[1])
s3 = int(mode[2])
s1 = s1*10000+s2*100+s3
time = s1
mode = date.split('-')
s1 = int(mode[0])
s2 = int(mode[1])
s3 = int(mode[2])
s1 = s1*10000+s2*100+s3
date = s1
filename = 'output'+str(time)+'_'+str(date)
filename+='.csv'
ds.send_data(conn,filename)
print('Name of File created :',filename)
header_name = ["Date","Time","PM1","PM2.5","PM10","NO2","CO2","CO","Humidity","Temperature"]
with open(filename, 'w+') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_name)


start_time = tm.time()
while True:
   x=ser.readline()
   #print(x)
   end_time = tm.time()
   if x is  None:
            continue
   now_time = end_time-start_time
   if now_time<5:
            print(x)
            print("Ignore state")
            continue
   currenttime = datetime.datetime.now()
   currenttime = str(currenttime)
   currenttime_array = currenttime.split(' ')
   date = currenttime_array[0]
   time = currenttime_array[1][:8]
   x = x.strip()
   x = str(x,'utf-8')
   x = x.split(',')
   if len(x) !=8:
            continue
   PM1 = int(x[0])
   PM2_5 = int(x[1])
   PM10 = int(x[2])
   NO2 = float(x[3])
   CO2 = int(x[4])
   CO = float(x[5])
   humi = float(x[6])
   temp = float(x[7])
   print(date,time,PM1,PM2_5,PM10,NO2,CO2,CO,humi,temp)
   data_list = [date,time,PM1,PM2_5,PM10,NO2,CO2,CO,humi,temp]
   ds.send_data(conn,data_list)
   with open(filename, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data_list)
   data_str=','.join(str(e) for e in data_list)

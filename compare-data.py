import csv
import numpy as np
from matplotlib import pyplot as plt
latitude = []
longitude = []
time =[]
pm1_val = []
pm2_5_val = []
pm10_val = []
no2_val = []
co2_val = []
co_val = []
humidity = []
temp = []
count1 = []
count = 0

with open('data.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rows in csv_reader:
        count+=1
        lat,long,Time,date,PM1,PM2_5,PM10,NO2,CO2,CO,Humidity,Temperature = rows.values()
        latitude.append(lat)
        longitude.append(long)
        time.append(Time)
        pm1_val.append(PM1)
        pm2_5_val.append(PM2_5)
        pm10_val.append(PM10)
        no2_val.append(NO2)
        co2_val.append(CO2)
        co_val.append(CO)
        humidity.append(Humidity)
        temp.append(Temperature)
        count1.append(count)
        print(count,lat,long,Time,date,PM1,PM2_5,PM10,NO2,CO2,CO,Humidity,Temperature)

plt.subplot(4,2, 1)
plt.plot(count1,pm1_val,  'ro')
plt.xlabel('PM1')
plt.ylabel('Count')

plt.subplot(4,2, 2)
plt.plot(count1, pm2_5_val, 'ro')
plt.xlabel('PM2.5')
plt.ylabel('Count')
plt.subplot(4,2,3)
plt.plot( count1,pm10_val, 'ro')
plt.xlabel('PM10')
plt.ylabel('Count')
plt.subplot(4,2, 4)
plt.plot( count1,no2_val, 'ro')
plt.xlabel('NO2')
plt.ylabel('Count')
plt.subplot(4,2, 5)
plt.plot(co2_val, count1, 'ro')
plt.xlabel('CO2')
plt.ylabel('Count')
plt.subplot(4,2,6)
plt.plot(count1,co_val,  'ro')
plt.xlabel('CO')
plt.ylabel('Count')
plt.subplot(4,2,7)
plt.plot(count1,humidity,  'ro')
plt.xlabel('Humidity')
plt.ylabel('Count')
plt.subplot(4,2,8)
plt.plot( count1,temp, 'ro')
plt.xlabel('Temperature')
plt.ylabel('Count')

plt.show()

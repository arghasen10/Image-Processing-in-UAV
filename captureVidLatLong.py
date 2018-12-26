import serial               
import time 
import webbrowser           
import sys                  
import csv
import picamera

def GPS_Info():
    global NMEA_buff
    global lat_in_degrees
    global long_in_degrees
    nmea_time = []
    nmea_latitude = []
    nmea_longitude = []
    nmea_time = NMEA_buff[0]                    
    nmea_latitude = NMEA_buff[1]                
    nmea_longitude = NMEA_buff[3]               
    
    print("NMEA Time: ", nmea_time,'\n')
    print ("NMEA Latitude:", nmea_latitude,"NMEA Longitude:", nmea_longitude,'\n')
    
    lat = float(nmea_latitude)                  
    longi = float(nmea_longitude)               
    
    lat_in_degrees = convert_to_degrees(lat)    
    long_in_degrees = convert_to_degrees(longi) 
  
def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position
    


gpgga_info = "$GPGGA,"
ser = serial.Serial ("/dev/ttyS0")              
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degrees = 0
long_in_degrees = 0


while True:
    received_data = (str)(ser.readline())                   
    GPGGA_data_available = received_data.find(gpgga_info)                   
    if (GPGGA_data_available>0):
        GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  
        NMEA_buff = (GPGGA_buffer.split(','))               
        GPS_Info()                                          

        print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\n')
        

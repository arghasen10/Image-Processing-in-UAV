//#include <SoftwareI2C.h>
//#include <TH02_dev.h>
////#include <SPI.h>
//#include <MutichannelGasSensor.h>
//#include <Wire.h>
////#include "Wire.h"
////#include <Arduino.h>
//#include <SoftwareSerial.h>
//#include "RTClib.h"
//#include <TinyGPS++.h>
//#include <SD.h>
//#define LENG 31   //0x42 + 31 bytes equal to 32 bytes
//unsigned char buf[LENG];
//const int chipSelect = 53;
//int PM01Value=0;          //define PM1.0 value of the air detector module
//int PM2_5Value=0;         //define PM2.5 value of the air detector module
//int PM10Value=0;         //define PM10 value of the air detector module
//String dataString = "";
////SoftwareSerial Serial0(12,13); // RX, TX
//SoftwareSerial gpsSerial(10,11); //RX,TX
//TinyGPSPlus gps;
//RTC_DS1307 rtc;
//char daysOfTheWeek[7][12] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
//
//double lattitude,longitude;
int sensorValue;
//int digitalValue;
//#define GAS_EN      1
//#define TH02_EN     1
//const int pin_scl = 2;      // select a pin as SCL of software I2C
//const int pin_sda = 3;      // select a pin as SDA of software I2C
//int flag=0;
//int filenum =0;
//int writeflag =0;
//String filename = "A";
////Latitude,Longitude,Time,Date,PM1,PM2_5,PM10,N02,CO2,CO,Humidity,Temperature
//String lati,lon,tim,dat,pm1val,pm2_5val,pm10_val,no2_val,co2_val,co_val,humid_val,temper_val;
void setup()
{
  Serial.begin(9600);
}

void loop()
{  
  readMQ135();
  delay(1000);

}
void readMQ135()
{
  //Serial.begin(9600);
  sensorValue = analogRead(A1);       // read analog input pin 1
 // Serial.print("");
  Serial.println(sensorValue,DEC);
  
  //Serial.print(" , ");
//  co2_val = String(sensorValue,DEC);
  //dataString += String(sensorValue);
    //dataString += ",";
//  Serial.println();
//Serial.end();
}


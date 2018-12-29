#include <SoftwareI2C.h>
#include <TH02_dev.h>
//#include <SPI.h>
#include <MutichannelGasSensor.h>
#include <Wire.h>
//#include "Wire.h"
//#include <Arduino.h>
#include <SoftwareSerial.h>
#include "RTClib.h"
#include <TinyGPS++.h>
#include <SD.h>
#define LENG 31   //0x42 + 31 bytes equal to 32 bytes
unsigned char buf[LENG];
const int chipSelect = 53;
int PM01Value=0;          //define PM1.0 value of the air detector module
int PM2_5Value=0;         //define PM2.5 value of the air detector module
int PM10Value=0;         //define PM10 value of the air detector module
String dataString = "";
//SoftwareSerial Serial0(12,13); // RX, TX
SoftwareSerial gpsSerial(10,11); //RX,TX
TinyGPSPlus gps;
RTC_DS1307 rtc;
char daysOfTheWeek[7][12] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};

double lattitude,longitude;
int sensorValue;
int digitalValue;
#define GAS_EN      1
#define TH02_EN     1
const int pin_scl = 2;      // select a pin as SCL of software I2C
const int pin_sda = 3;      // select a pin as SDA of software I2C
int flag=0;
int filenum =0;
int writeflag =0;
String filename = "A";
//Latitude,Longitude,Time,Date,PM1,PM2_5,PM10,N02,CO2,CO,Humidity,Temperature
String lati,lon,tim,dat,pm1val,pm2_5val,pm10_val,no2_val,co2_val,co_val,humid_val,temper_val;
void setup()
{
  Serial.begin(9600);
  setupSD();
  setupRTC();
  setupGPS();
  pinMode(53, OUTPUT);
  //Serial0.begin(9600); 
  setuphumi();
  setupmulti();
 setupdust();
   readRTC();
}

void loop()
{  
  //gpsSerial.begin(9600);
  dataString = "";
 while(gpsSerial.available())
  {
    float data = gpsSerial.read();
    if(gps.encode(data)) 
  {
 lattitude = {gps.location.lat()*1000000}; 
  longitude = {gps.location.lng()*1000000}; 
//gpsSerial.end();
//Serial.begin(9600);

  flag = 1;
 // Serial.print("lattitude:");
  Serial.print(lattitude/1000000,6);
  Serial.print(" , ");
  lati = String(lattitude/1000000,6);
  //dataString += String(lattitude/1000000,6);
    //dataString += ","; 
        
 // Serial.print("longitude:");
  Serial.print(longitude/1000000,6);
  Serial.print(" , ");
  lon = String(longitude/1000000,6);
  //dataString += String(longitude/1000000,6);
    //dataString += ","; 
  
}
  }
  
  if (flag ==1){
    readRTC();
    readdust();
    readmultino2();
  readMQ135();
  readmultico();
  readhumi();
  writeSD();
  }
  
  //delay(1000);
  flag =0 ;
  //Serial.println("Inside tge loop but GPS not working");
}

////////////////////////////////////////////////
void setupSD()
{
  Serial.print("Initializing SD card...");
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    return;
  }
  Serial.println("card initialized.");
}
void writeSD()
{
  File dataFile = SD.open(filename, FILE_WRITE);
  if (dataFile) {
    if(writeflag == 0){
      dataFile.println("Latitude,Longitude,Time,Date,PM1,PM2_5,PM10,N02,CO2,CO,Humidity,Temperature");
      writeflag=1;
    }
    dataFile.println(lati+","+lon+","+tim+","+dat+","+pm1val+","+pm2_5val+","+pm10_val+","+no2_val+","+co2_val+","+co_val+","+humid_val+","+temper_val);
    Serial.println(lati+","+lon+","+tim+","+dat+","+pm1val+","+pm2_5val+","+pm10_val+","+no2_val+","+co2_val+","+co_val+","+humid_val+","+temper_val);
    dataFile.close();
    // print to the serial port too:
   // Serial.println(dataString);
  }  
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
  }
}

////////////////////////////////////////////////
void setupRTC()
{
  if (! rtc.begin()) 
  {
    //lcd.print("Couldn't find RTC");
    Serial.println("Couldn't find RTC");
    while (1);
  }

  if (! rtc.isrunning()) 
  {
    Serial.print("RTC is NOT running!");
  }
  
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));//auto update from computer time
    //rtc.adjust(DateTime(2018, 1, 21, 3, 0, 0));// to set the time manualy 
}

void readRTC()
{
    if(filenum == 0){
      DateTime now = rtc.now();
      filename += String(now.day());
    filename+= String(now.hour());
    filename+= String(now.minute());
    filename += ".csv";
    filenum =1;
      }
    String datertc = "";
    String timertc = "";
    DateTime now = rtc.now();
    timertc+= String(now.hour());
    timertc+=":";
    timertc+= String(now.minute());
    timertc+=":";
    timertc+= String(now.second());
    
    //Serial.println(daysOfTheWeek[now.dayOfTheWeek()]);
    
    datertc += String(now.day());
    datertc +="/";
    datertc += String(now.month());
    datertc +="/";
    datertc += String(now.year());
    Serial.print(timertc);
    Serial.print(" , ");
    Serial.print(datertc);
    Serial.print(" , ");
    tim = timertc;
    dat = datertc;
   /* dataString+=timertc;
    dataString+=",";
    dataString+=datertc;
    dataString+=",";*/
}
////////////////////////////////////////////////
 void setupGPS()
{
  gpsSerial.begin(9600);
}
////////////////////////////////////////////////
/*void readGPS()
{
   gpsSerial.begin(9600);
  while(gpsSerial.available())
  {
    int data = gpsSerial.read();
     gpsSerial.end();
    if(gps.encode(data))
    
  {
  
  
 
 lattitude = {gps.location.lat()}; 
  longitude = {gps.location.lng()}; 

  Serial.begin(9600);
 // Serial.print("lattitude:");
  Serial.println(lattitude);
  Serial.print(" , ");
 // Serial.print("longitude:");
  Serial.println(longitude);
  Serial.print(" , ");
}
  }
  Serial.end();
}
*/
////////////////////////////////////////////////


void readMQ135()
{
  //Serial.begin(9600);
  sensorValue = analogRead(A1);       // read analog input pin 1
 // Serial.print("");
  Serial.print(sensorValue,DEC);
  Serial.print(" , ");
  co2_val = String(sensorValue,DEC);
  //dataString += String(sensorValue);
    //dataString += ",";
//  Serial.println();
//Serial.end();
}
//////////////////////////////////////////////////////////
void setupmulti()
{
    //Serial.begin(115200);  // start serial for output
    gas.begin(0x04);//the default I2C address of the slave is 0x04

}

void readmultino2()
{ 
  //serial.begin(9600);
    float n;  
    n = gas.measure_NO2();    
    Serial.print(n);
    Serial.print(" , ");
    //dataString += String(n);
    //dataString += ","; 
    no2_val = String(n);
//    Serial.println();
//Serial.end();
}


void readmultico()
{ 
    float c;
    c = gas.measure_CO();
    Serial.print(c);
    Serial.print(" , ");
    //dataString += String(c);
    //dataString += ",";
    co_val = String(c);
}
//////////////////////////////////////////////////////////////

void setuphumi()
{  
 //TH02.begin();
  TH02.begin(pin_scl, pin_sda);
 // delay(100);  
}

void readhumi()
{ 
  
    float humidity = TH02.ReadHumidity();
  Serial.print(humidity);
    Serial.print(" , ");
    //dataString += String(humidity);
    //dataString += ",";
   float temper = TH02.ReadTemperature();   
   Serial.println(temper);
  //dataString += String(temper);
   humid_val = String(humidity);
   temper_val = String(temper);
          

//  Serial.println();
}


void setupdust()
{
   
//  Serial0.setTimeout(1500);    
 // Serial.begin(9600);
 Serial1.begin(9600);
}

void readdust()
{
  //Serial0.begin(9600);  
  
  if(Serial1.find("B")){    
    Serial1.readBytes(buf,LENG);

    if(buf[0] == 0x4d){
      if(checkValue(buf,LENG)){
        PM01Value=transmitPM01(buf); //count PM1.0 value of the air detector module
        PM2_5Value=transmitPM2_5(buf);//count PM2.5 value of the air detector module
        PM10Value=transmitPM10(buf); //count PM10 value of the air detector module 
      }           
    }
  }
  //Serial1.end();
  //Serial.begin(9600);
  static unsigned long OledTimer=millis();  
  //  if (millis() - OledTimer >=1000) 
    {
      OledTimer=millis(); 
   
//      Serial.print("PM1.0: ");  
      Serial.print(PM01Value);
      Serial.print(" , ");
      //dataString += String(PM01Value);
    //dataString += ","; 
    pm1val = String(PM01Value);
//      Serial.println("  ug/m3");            
    
//      Serial.print("PM2.5: ");  
      Serial.print(PM2_5Value);
      Serial.print(" , ");
      //dataString += String(PM2_5Value);
    //dataString += ",";
    pm2_5val= String(PM2_5Value);
   
//      Serial.println("  ug/m3");     
      
//      Serial.print("PM1 0: ");  
      Serial.print(PM10Value);
//      Serial.println("  ug/m3");   
      Serial.print(" , ");
       pm10_val  = String(PM10Value);
      //dataString += String(PM10Value);
    //dataString += ","; 
    }
  //Serial0.end();
  //Serial.end();
}

char checkValue(unsigned char *thebuf, char leng)
{  
  char receiveflag=0;
  int receiveSum=0;

  for(int i=0; i<(leng-2); i++){
  receiveSum=receiveSum+thebuf[i];
  }
  receiveSum=receiveSum + 0x42;
 
  if(receiveSum == ((thebuf[leng-2]<<8)+thebuf[leng-1]))  //check the serial data 
  {
    receiveSum = 0;
    receiveflag = 1;
  }
  return receiveflag;
}


//transmit PM01 Value to PC
int transmitPM01(unsigned char *thebuf)
{
  int PM01Val;
  PM01Val=((thebuf[3]<<8) + thebuf[4]); //count PM1.0 value of the air detector module
  return PM01Val;
}

//transmit PM2.5 Value to PC
int transmitPM2_5(unsigned char *thebuf)
{
  int PM2_5Val;
  PM2_5Val=((thebuf[5]<<8) + thebuf[6]);//count PM2.5 value of the air detector module
  return PM2_5Val;
  }

//transmit PM10 Value to PC
int transmitPM10(unsigned char *thebuf)
{
  int PM10Val;
  PM10Val=((thebuf[7]<<8) + thebuf[8]); //count PM10 value of the air detector module  
  return PM10Val;
}
  


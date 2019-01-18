

#include <TH02_dev.h>

#include <SoftwareI2C.h>
#include <Wire.h>
#include <MutichannelGasSensor.h>
#define LENG 31   //0x42 + 31 bytes equal to 32 bytes
unsigned char buf[LENG];
int PM01Value=0;          //define PM1.0 value of the air detector module
int PM2_5Value=0;         //define PM2.5 value of the air detector module
int PM10Value=0;   
int sensorValue;
int digitalValue;
#define GAS_EN      1
#define TH02_EN     1
const int pin_scl = 2;      // select a pin as SCL of software I2C
const int pin_sda = 3;      // select a pin as SDA of software I2C
int flag=0;
int writeflag =0;
String lati,lon,tim,dat,pm1val,pm2_5val,pm10_val,no2_val,co2_val,co_val,humid_val,temper_val;
void setup()
{
  Serial.begin(9600);
  setuphumi();
 setupmulti();
  setupdust();
  setuphumi();
}

void loop()
{
  readdust();
 readmultino2();
  readMQ135();
  readmultico();
  readhumi();
  delay(1000);

}
void readMQ135()
{
  sensorValue = analogRead(A1);       // read analog input pin 1
  Serial.print(sensorValue,DEC);
  Serial.print(",");
}

void setupdust()
{
 Serial0.begin(9600);
}

void readdust()
{
  if(Serial0.find("B")){    
    Serial0.readBytes(buf,LENG);

    if(buf[0] == 0x4d){
      if(checkValue(buf,LENG)){
        PM01Value=transmitPM01(buf); //count PM1.0 value of the air detector module
        PM2_5Value=transmitPM2_5(buf);//count PM2.5 value of the air detector module
        PM10Value=transmitPM10(buf); //count PM10 value of the air detector module 
      }           
    }
  }
  static unsigned long OledTimer=millis();  
    {
      OledTimer=millis(); 
    
      Serial.print(PM01Value);
      Serial.print(",");
    pm1val = String(PM01Value);
      Serial.print(PM2_5Value);
      Serial.print(",");
    pm2_5val= String(PM2_5Value); 
      Serial.print(PM10Value);  
      Serial.print(",");
       pm10_val  = String(PM10Value);
    }
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

void setupmulti()
{
    gas.begin(0x04);//the default I2C address of the slave is 0x04

}

void readmultino2()
{ 
    float n;  
    n = gas.measure_NO2();    
    Serial.print(n);
    Serial.print(",");
}


void readmultico()
{ 
    float c;
    c = gas.measure_CO();
    Serial.print(c);
    Serial.print(",");
}
////////////////////////////////////////////////////////////

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
    Serial.print(",");
    //dataString += String(humidity);
    //dataString += ",";
   float temper = TH02.ReadTemperature();   
   Serial.println(temper);
}


#include <MutichannelGasSensor.h>
#include <SoftwareI2C.h>
#define LENG 31   //0x42 + 31 bytes equal to 32 bytes
unsigned char buf[LENG];
int sensorValue;
int digitalValue;
const int pin_scl = 2;      
const int pin_sda = 3;

void setup()
{
  Serial.begin(9600);
  setupmulti();
}

void loop()
{  
  
    readmultino2();
  readmultico();
}

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
}


void readmultico()
{ 
    float c;
    c = gas.measure_CO();
    Serial.print(c);
    Serial.print(" , ");
}

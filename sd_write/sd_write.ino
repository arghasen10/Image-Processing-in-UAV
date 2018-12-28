/*
  http://www.bajdi.com
  SD card datalogger for Arduino Mega (this sketch will ONLY work with Arduino Mega) 
 
 This example shows how to log data from three analog sensors 
 to an SD card using the SD library.
   
 The circuit:
 * analog sensors on analog ins 0, 1, and 2
 * SD card attached to SPI bus as follows:
 ** MOSI - pin 51
 ** MISO - pin 50
 ** CLK - pin 52
 ** CS - pin 53
 
 created  24 Nov 2010
 updated 2 Dec 2010
 by Tom Igoe
 updated 22 Jan 2012 for Arduino Mega
 by Bajdi.com 
 
 This example code is in the public domain.
   
 */

#include <SD.h>

// On the Ethernet Shield, CS is pin 4. Note that even if it's not
// used as the CS pin, the hardware CS pin (10 on most Arduino boards,
// 53 on the Mega) must be left as an output or the SD library
// functions will not work.
const int chipSelect = 53;
int i =0;
void setup()
{
  Serial.begin(9600);
  Serial.print("Initializing SD card...");
  // make sure that the default chip select pin is set to
  // output, even if you don't use it:
  pinMode(53, OUTPUT);
  
  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    return;
  }
  Serial.println("card initialized.");
}

void loop()
{
  i=0;
  // make a string for assembling the data to log:
  String dataString = "";

  // read three sensors and append to the string:
  /*for (int analogPin = 0; analogPin < 3; analogPin++) {
    //int sensor = analogRead(analogPin);
    dataString += "100";
    if (analogPin < 2) {
      dataString += ","; 
    }
  }*/
  while(i<5){
    i++;
    dataString += "100";
    dataString += ","; 
  }

  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  File dataFile = SD.open("datalog.txt", FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    // print to the serial port too:
    Serial.println(dataString);
  }  
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
  } 
  delay(1000);
}


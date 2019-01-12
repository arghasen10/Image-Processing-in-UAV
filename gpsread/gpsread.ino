#include <SoftwareSerial.h>
#include <TinyGPS++.h>
TinyGPSPlus gps;

SoftwareSerial mySerial(8,9);

void setup() {
  mySerial.begin(9600);
  Serial.begin(9600);
  Serial.println("GPS start");
}

void loop() {
  while (mySerial.available()) {
    gps.encode(mySerial.read());
  }
  if (gps.location.isUpdated()) {
    //double a = gps.location.lat();
    //Serial.println(a);
    Serial.print(gps.location.lat(), 6);
    //double b = gps.location.lng();
    Serial.print(" , ");
    Serial.print(gps.location.lng(), 6);
    Serial.println(" , ");
  }
}

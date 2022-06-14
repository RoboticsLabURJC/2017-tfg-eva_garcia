#include "MeMCore.h"
// Onboard LED port/slot definitions
const int PORT = 7;
const int SLOT = 2;
// Declare the MeRGLed object
MeRGBLed led(PORT, SLOT);


void setup() {
  // put your setup code here, to run once:
  //iniciamos el puerto serie
  Serial.begin(9600);
}
String red = "red";
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    String leer = Serial.readString();    
    if (leer.equalsIgnoreCase("red")) {
        led.setColor(0, 255, 0, 0);
        led.show();
    } else if (leer.equalsIgnoreCase("blue")) {
        led.setColor(0, 0, 0, 255);
        led.show();
    } else if (leer.equalsIgnoreCase("green")) {
        led.setColor(0, 0, 255, 0);
        led.show();
    } else if (leer.equalsIgnoreCase("quit")) {
        led.setColor(0, 0, 0, 0);
        led.show();
        exit(0);
    } else {
        led.setColor(0, 255, 255, 255);
        led.show();      
    }
    delay (100);
  }
}

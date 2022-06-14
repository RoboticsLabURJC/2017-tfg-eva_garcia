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

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    char leer = Serial.read();   
    if (leer == 'r') {
        led.setColor(0, 255, 0, 0);
        led.show();
    } else if (leer == 'b') {
        led.setColor(0, 0, 0, 225);
        led.show();
    } else if (leer == 'g') {
        led.setColor(0, 0, 255, 0);
        led.show();
    } else if (leer == 'q') {
        led.setColor(0, 0, 0, 0);
        led.show();
    }
    delay (100);
  }
}

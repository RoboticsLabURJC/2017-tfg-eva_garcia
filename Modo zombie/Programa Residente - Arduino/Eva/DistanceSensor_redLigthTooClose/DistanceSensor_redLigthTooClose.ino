#include "MeMCore.h"
// Onboard LED port/slot definitions
const int PORT = 7;
const int SLOT = 2;
// Declare the MeRGLed object
MeRGBLed led(PORT, SLOT);
MeUltrasonicSensor ultraSensor(PORT_3);
void setup() {
  // put your setup code here, to run once:
  //iniciamos el puerto serie
  Serial.begin(9600);
}


void loop()
{

  Serial.println(ultraSensor.distanceCm());
  if (Serial.available()>0){
    String mensaje = Serial.readString();
    int IndexLeds = mensaje.indexOf(';');
    String leds = mensaje.substring(0, IndexLeds);
    int IndexRed = mensaje.indexOf(';', IndexLeds+1);   //finds location of second ,
    String red = mensaje.substring(IndexLeds+1, IndexRed+1);
    int IndexGreen = mensaje.indexOf(';', IndexRed+1);   //finds location of third ,
    String green = mensaje.substring(IndexRed+1, IndexGreen+1);
    String blue = mensaje.substring(IndexGreen+1,-1); //captures remain part of data after last ,
    int ledsInt = leds.toInt();
    int redInt = red.toInt();
    int greenInt = green.toInt();
    int blueInt = blue.toInt();
    led.setColor(ledsInt, redInt, greenInt, blueInt);
    led.show();
  }
  delay(100); /* the minimal measure interval is 100 milliseconds */
}

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
    String mensaje = Serial.readString();
    if (mensaje.equalsIgnoreCase("quit")) {
        led.setColor(0, 0, 0, 0);
        led.show();
        exit(0);
    }
    Serial.print("captured String is : "); 
    Serial.println(mensaje);  
    int IndexLeds = mensaje.indexOf(';');
    String leds = mensaje.substring(0, IndexLeds);
    int IndexRed = mensaje.indexOf(';', IndexLeds+1);   //finds location of second ,
    String red = mensaje.substring(IndexLeds+1, IndexRed+1);
    int IndexGreen = mensaje.indexOf(';', IndexRed+1);   //finds location of third ,
    String green = mensaje.substring(IndexRed+1, IndexGreen+1);
    String blue = mensaje.substring(IndexGreen+1,-1); //captures remain part of data after last ,
        
    //Serial.print("leds = ");
    //Serial.println(leds);
    //Serial.print("red = ");
    //Serial.println(red);
    //Serial.print("green = ");
    //Serial.println(green);
    //Serial.print("blue = ");
    //Serial.println(blue);
    int ledsInt = leds.toInt();
    int redInt = red.toInt();
    int greenInt = green.toInt();
    int blueInt = blue.toInt();
    led.setColor(ledsInt, redInt, greenInt, blueInt);
    led.show();
    delay (100);
  }
}

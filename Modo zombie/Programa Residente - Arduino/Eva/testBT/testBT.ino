
#include <Wire.h>
#include <SoftwareSerial.h>
#include <MeMCore.h>

MeUltrasonicSensor ultrasonic_3(3);
MeRGBLed rgbled_7(7, 7==7?2:4);

void setup(){
}

void loop(){
    if((ultrasonic_3.distanceCm()) < (30)){
        rgbled_7.setColor(0,255,0,0);
        rgbled_7.show();
    }else{
        rgbled_7.setColor(0,0,255,0);
        rgbled_7.show();
    }
}

#include "MeMCore.h"
MeDCMotor motorIzdo(M1);
MeDCMotor motorDcho(M2);

void setup() {
  // put your setup code here, to run once:
  //iniciamos el puerto serie
  Serial.begin(15000);
}


void loop()
{

  Serial.println(ultraSensor.distanceCm());
  if (Serial.available()>0){
    int IndexIzdo = mensaje.indexOf(';');
    String izdo = mensaje.substring(0, IndexIzdo);
    String dcho = mensaje.substring(IndexIzdo+1,-1); //captures remain part of data after last ,

    int izdoInt = izdo.toInt();
    int dchoInt = dcho.toInt();
    motorIzdo.run(izdoInt);
    motorDcho.run(dchoInt);
    delay (100);
  }
  delay(100); /* the minimal measure interval is 100 milliseconds */
}

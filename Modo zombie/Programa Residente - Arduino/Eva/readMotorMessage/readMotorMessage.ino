
#include "MeMCore.h"
MeDCMotor motorIzdo(M1);
MeDCMotor motorDcho(M2);


void setup() {
  // put your setup code here, to run once:
  //iniciamos el puerto serie
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    String mensaje = Serial.readString();
    if (mensaje.equalsIgnoreCase("quit")) {
        motorIzdo.stop();
        motorDcho.stop();
        exit(0);
    }
    Serial.print("captured String is : "); 
    Serial.println(mensaje);  
    int IndexIzdo = mensaje.indexOf(';');
    String izdo = mensaje.substring(0, IndexIzdo);
    String dcho = mensaje.substring(IndexIzdo+1,-1); //captures remain part of data after last ,

    int izdoInt = izdo.toInt();
    int dchoInt = dcho.toInt();
    motorIzdo.run(izdoInt); //el motor izdo va del revés
    motorDcho.run(dchoInt);
    delay (100);
  }
}

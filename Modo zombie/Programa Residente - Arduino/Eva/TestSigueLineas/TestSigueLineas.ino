#include "MeMCore.h"



MeLineFollower SigueLineas(PORT_1); 

void setup() {
  // put your setup code here, to run once:
  //iniciamos el puerto serie
  Serial.begin(9600);
}

void loop()
// put your main code here, to run repeatedly:
{
  int ValorSigueLineas = SigueLineas.readSensors();
  switch(ValorSigueLineas)
  {
    case S1_IN_S2_IN: 
      Serial.println("Sensor 1 and 2 are inside of black line"); break;
    case S1_IN_S2_OUT: 
      Serial.println("Sensor 2 is outside of black line"); break;
    case S1_OUT_S2_IN: 
      Serial.println("Sensor 1 is outside of black line"); break;
    case S1_OUT_S2_OUT: 
      Serial.println("Sensor 1 and 2 are outside of black line"); break;
    default: 
      break;
  }
  delay(500);
}

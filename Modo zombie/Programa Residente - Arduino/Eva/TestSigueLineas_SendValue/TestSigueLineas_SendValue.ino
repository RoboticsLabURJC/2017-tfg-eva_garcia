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
  Serial.println(ValorSigueLineas);
  delay(500);
}

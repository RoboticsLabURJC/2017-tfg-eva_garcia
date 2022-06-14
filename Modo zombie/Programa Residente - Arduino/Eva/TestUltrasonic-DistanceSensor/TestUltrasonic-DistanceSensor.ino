#include "MeMCore.h"

MeUltrasonicSensor ultraSensor(PORT_3);
void setup() {
  // put your setup code here, to run once:
  //iniciamos el puerto serie
  Serial.begin(9600);
}


void loop()
{
  Serial.println(ultraSensor.distanceCm() );
  delay(200); /* the minimal measure interval is 100 milliseconds */
}

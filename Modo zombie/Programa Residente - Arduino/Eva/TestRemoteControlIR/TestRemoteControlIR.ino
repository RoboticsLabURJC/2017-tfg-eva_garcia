#include "MeMCore.h"

#include <SoftwareSerial.h>

MeIR ir;

void setup()
{
  ir.begin();
  Serial.begin(9600);
  
}

void loop()
{

  if(ir.keyPressed(22))
  {
    Serial.println("available");
    ReceiverCode = ir.read();
    Serial.println(ReceiverCode);
     
  }
}

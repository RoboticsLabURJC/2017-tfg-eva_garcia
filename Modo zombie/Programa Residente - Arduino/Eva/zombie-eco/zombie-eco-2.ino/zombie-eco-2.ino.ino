char escribir='a';
 
void setup(){
  //iniciamos el puerto serie
  Serial.begin(9600);
}

void loop(){
    Serial.println(escribir);
    delay(1000);
}

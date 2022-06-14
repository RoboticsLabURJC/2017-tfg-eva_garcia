String leer;
 
void setup(){
  //iniciamos el puerto serie
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()>0){
    leer = Serial.readString();
      Serial.println(leer);
  }
}

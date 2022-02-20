char leer;
 
void setup(){
  //iniciamos el puerto serie
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()>0){
    leer = Serial.read();  
    if (leer == 'q') {
      exit (0);
    } else {
      Serial.println(leer);
    }
  }
}

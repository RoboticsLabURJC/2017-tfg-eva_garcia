
#include "MeMCore.h"

// Onboard LED port/slot definitions
const int PORT = 7;
const int SLOT = 2;
// Declare the MeRGLed object
MeRGBLed led(PORT, SLOT);

char leer; // variable para almacenamiento de caracteres
boolean encendido = true; // variable de almacenamiento de estado binario

void setup() {
  Serial.begin(9600);  // inicialización del puerto serial para la comunicación a 9600 baudios
}

void loop() {
  leer = Serial.read(); //almacena la lectura del puerto serial en la variable "leer" que es de tipo caracter
  if ((leer == 'a')&&(encendido == false)){ //si en la variable leer aparece la letra "a"; y si el led no está encendido hacer lo siguiente:
    led.setColor(0, 255, 0, 0); //Encender el led
    led.show();
    encendido = true; // asigna el valor 1 a la variable encendido, que da seguimiento al estado booleano del led
  } else if ((leer == 'a')&&(encendido == true)){
    led.setColor(0, 0, 0, 0); //Encender el led
    led.show();
    encendido = false; // asigna el valor 0 a la variable encendido, que da seguimiento al estado booleano del led
  }

}

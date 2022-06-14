
#include "MeMCore.h"
MeBuzzer buzzer;

void setup() {
   // put your setup code here, to run once:
   Serial.begin(9600);
}

void loop() {

  if (Serial.available()>0){
    String mensaje = Serial.readString();
    if (mensaje.equalsIgnoreCase("quit")) {
        buzzer.noTone();
        exit(0);
    }  
    int IndexNote = mensaje.indexOf(';');
    String note = mensaje.substring(0, IndexNote);  
    String duration = mensaje.substring(IndexNote+1,-1); //captures remain part of data after last ;
    int NoteInt = note.toInt() ;
    int DurationInt = duration.toInt();
    // put your main code here, to run repeatedly:
    play(NoteInt, DurationInt);//Play the music.
    delay(300);//Pause for a while.
  }

}

void play(int note, int seconds)
{
  int duration = 1000 * seconds; // la duracion de la funcion es en milisegundos, por lo que hay que multiplicar
  int pauseBetweenNotes = duration * 1.30; // note's duration + 30% seems to work well
  buzzer.tone(note,duration);
  delay(pauseBetweenNotes);
  // stop the tone playing:
  buzzer.noTone();
}

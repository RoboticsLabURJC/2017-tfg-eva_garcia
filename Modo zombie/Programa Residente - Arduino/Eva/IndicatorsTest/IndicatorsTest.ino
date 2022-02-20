#include "MeMCore.h"

// Onboard LED port/slot definitions
const int PORT = 7;
const int SLOT = 2;
// Declare the MeRGLed object
MeRGBLed led(PORT, SLOT);

// LED Control settings
const int BOTH_LEDS = 0;
const int RIGHT_LED = 1;
const int LEFT_LED  = 2;


void setup()
{
}

void showColor(int LedSelection, int red, int green, int blue)
{
  int duration = 10;  
  led.setColor(LedSelection, red, green, blue);
  led.show();
  delay(duration);
}

/*------------*/
void loop()
{
  for (int i = 0; i <= 255; i++) {
    int select = random(0, 2);
    /* generates random numbers */
    int r = random (0,255);
    int g = random (0,255);
    int b = random (0,255);
    showColor(select,r,g,b);
    delay(150);
  }
  /* clear the board */
  showColor(0,0,0,0);
  exit (0);
}

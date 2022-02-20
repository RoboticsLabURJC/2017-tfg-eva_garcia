
#include <MeMCore.h>

// Onboard LED port/slot definitions
const int PORT = 7;
const int SLOT = 2;

// LED Control settings
const int BOTH_LEDS = 0;
const int RIGHT_LED = 1;
const int LEFT_LED  = 2;

// Declare the MeRGLed object
MeRGBLed onboardLEDs(PORT, SLOT);

void updateLED(int led, int red, int green, int blue) {
  onboardLEDs.setColor(led, red, green, blue);
  onboardLEDs.show();
}

/***********************************************************************
 * Method:       setup
 *
 * Arguments:    None
 *
 * Returns:      N/A
 *
 * Description:
 *    This method handles all of the initialization for the program.
 ************************************************************************/
void setup() {
  // set the led color components to generate a shade of red
  int red = 150;
  int green = 0;
  int blue = 0;
  int wait_duration = 2000;  // duration in milliseconds

  // set the color of the leds to a shade of red
  updateLED(BOTH_LEDS, red, green, blue);

  // wait for wait duration
  delay(wait_duration);

  // set the led color components to generate black (off)
  red = green = blue = 0;

  // set the color of the leds to black (off)
  updateLED(BOTH_LEDS, red, green, blue);
}


void loop() {
}

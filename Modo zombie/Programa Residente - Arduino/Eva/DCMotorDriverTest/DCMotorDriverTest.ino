/**
 * \par Copyright (C), 2012-2016, MakeBlock
 * @file    DCMotorDriverTest.ino
 * @author  MakeBlock
 * @version V1.0.0
 * @date    2015/09/09
 * @brief   Description: this file is sample code for Me DC motor device (default ones) in a loop that finish.
 *
 * Function List:
 *    1. void MeDCMotor::run(int16_t speed)
 *    2. void MeDCMotor::stop(void)

#include "MeMCore.h"

/*MeDCMotor motor1(PORT_1);

MeDCMotor motor2(PORT_2);*/

MeDCMotor motor3(M1);
MeDCMotor motor4(M2);

uint8_t motorSpeed = 100;

void setup()
{
}
void loop ()
{
  for (int i = 0; i <= 2; i++) {
    motor3.run(motorSpeed);
    motor4.run(motorSpeed);
    delay(2000);
    motor3.stop();
    motor4.stop();
    delay(100);
    motor3.run(-motorSpeed);
    motor4.run(-motorSpeed);
    delay(2000);
    motor3.stop();
    motor4.stop();
    delay(2000);    
  }
  exit (0);
}

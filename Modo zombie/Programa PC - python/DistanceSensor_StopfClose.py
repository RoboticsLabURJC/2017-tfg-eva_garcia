import sys
import serial
from time import sleep
from Mbot import *
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Lee del sensor de distancia (ultrasonic) y enciende led rojo si la pared está muy cerca y verde si no")

serial = open_PortSerial(15000,'com3',1)


while 1:
    distance = read_Sensor_Message(serial)
    if (distance -1):
        continue
    else:
        if (distance < 10):
            turnOn_Motors([100,100])
        else:
            turnOn_Motors([0,0])
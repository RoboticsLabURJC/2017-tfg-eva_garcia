import sys
import serial
from time import sleep
from Mbot import *
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Avanza a velocidad 100, leyendo del sensor de distancia (ultrasonic) y se para si la pared está muy cerca")

serial = open_PortSerial(50000,'com3',1)


while 1:
    sensorMessage = read_Sensor(serial)
    
    
    if (sensorMessage == -1):
        continue
    else:
      if (sensorMessage[0].lower() == 'distance'):
        if (sensorMessage[1] < 10):
            turnOn_Motors([0,0], serial)
        else:
            turnOn_Motors([100,100], serial)

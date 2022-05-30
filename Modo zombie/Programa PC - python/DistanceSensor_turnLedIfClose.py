import sys
import serial
from time import sleep
from Mbot import *
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Lee del sensor de distancia (ultrasonic) y enciende led rojo si la pared está muy cerca y verde si no")

serial = open_PortSerial(9600,'com3',1)


while 1:
    Data = serial.readline()
    decoded = Data.decode()
    try:
      distance = float(decoded)
    except (ValueError):
      continue
    if (distance < 10):
      turnOn_Leds([0,255,0,0])
    else:
      turnOn_Leds([0,0,255,0])


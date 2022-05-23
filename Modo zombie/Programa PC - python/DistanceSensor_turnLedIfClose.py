import sys
import serial
from time import sleep
from Mbot import *
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Lee del sensor de distancia (ultrasonic) y enciende led rojo si la pared está muy cerca y verde si no")

serial = open_PortSerial(9600,'com3',1)

""" try:
  serial = serial.Serial('com3', 9600, timeout=1)
except serial.SerialException:
  #-- Error al abrir el puerto serie
  sys.stderr.write("Error al abrir puerto (%s)\n")
  sys.exit(1)

serial.setDTR(False)
sleep(1)
serial.flushInput()
serial.setDTR(True)
sleep (1) """
while 1:
    Data = serial.readline()
    decoded = Data.decode()
    try:
      distance = float(decoded)
    except (ValueError):
      continue
    if (distance < 10):
      leds = create_Message_Led([0,255,0,0])
    else:
      leds = create_Message_Led([0,0,255,0])
    send_Message(leds,serial)


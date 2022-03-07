#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import sys
import serial
from time import sleep
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Pruebas del puerto serie")

try:
  serial = serial.Serial('com3', 9600)
  serial.timeout=1
except serial.SerialException:
  #-- Error al abrir el puerto serie
  sys.stderr.write("Error al abrir puerto (%s)\n")
  sys.exit(1)

cadena= ''
serial.setDTR(False)
sleep(1)
serial.flushInput()
serial.setDTR(True)

while True:
  serial.write(b'h')
  sleep(1)
  cadena = serial.readline()
  print (cadena)
  cadena=''








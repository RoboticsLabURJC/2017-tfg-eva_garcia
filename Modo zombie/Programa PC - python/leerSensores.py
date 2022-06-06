from base64 import decode
from posixpath import split
import sys
import serial
from time import sleep
from Mbot import *
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Prueba 1 de residente completo: leer valores y distinguir entre diferentes mensajes de sensores")

serial = open_PortSerial(9600,'com3',1)


while 1:
    sensorMessage = read_SensorMessage(serial)
    
    if (sensorMessage[0].lower() == 'distance'):
        print ("distance: " + sensorMessage[1])
    elif (sensorMessage[0].lower() == 'siguelineas'):
        print ("siguelíneas: " + sensorMessage[1])
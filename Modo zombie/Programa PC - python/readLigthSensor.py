import sys
import serial
from time import sleep
from Mbot import *
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Lee el valor del sensor de luz integrado")

serial = open_PortSerial(57600,'com3',1)



while 1:
    try:
        sensorMessage = read_Sensor(serial)    
        if (sensorMessage == -1):
            continue
        else:
            if (sensorMessage[0].lower() == 'luz'):
                print (sensorMessage[1])
    except KeyboardInterrupt:
        print ("INTERRUPT")
        sys.exit(0)
        
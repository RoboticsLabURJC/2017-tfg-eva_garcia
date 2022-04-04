import sys
import serial
from time import sleep
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Encender luz led componiendo el mensaje completo para mandar exactamente los valores")

try:
  serial = serial.Serial('com3', 9600, timeout=1)
except serial.SerialException:
  #-- Error al abrir el puerto serie
  sys.stderr.write("Error al abrir puerto (%s)\n")
  sys.exit(1)

serial.setDTR(False)
sleep(1)
serial.flushInput()
serial.setDTR(True)
cadena= ''
mensaje = []
while True:
    print ("Send or quit?")
    cadena=input()
    if (cadena.lower() == 'quit'):
        break
    print ("Enter which ones led want to turn on")
    leds=input()
    serial.write(bytes(leds, 'utf-8'))
    """ print ("Enter red value")
    red=input()
    serial.write(bytes(red, 'utf-8'))
    print("Enter green value")
    green=input()
    serial.write(bytes(green, 'utf-8'))
    print("Enter blue value")
    blue=input()
    serial.write(bytes(blue, 'utf-8'))
    sleep (1) """
    while 1:
        Data = serial.read()
        sleep (1)
        
        decoded = Data.decode('utf-8')
        print (decoded)
        break

serial.close()
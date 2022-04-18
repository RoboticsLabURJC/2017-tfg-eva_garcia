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
while True:
  print ("Send new message or quit?")
  cadena=input()
  if (cadena.lower() == 'quit'):
    serial.write(bytes(cadena, 'utf-8'))
    break
  print ("Enter which ones led want to turn on: 0-both, 1-rigth, 2-left")
  leds=input()
  print ("Enter red value")
  red=input()
  print("Enter green value")
  green=input()
  print("Enter blue value")
  blue=input()
  mensaje = f"{leds},{red},{green},{blue}"
  print (mensaje)
  serial.write(bytes(mensaje, 'utf-8'))
  while 1:
    Data = serial.read()
    sleep (1)
    dataLeft = serial.inWaiting()
    Data += serial.read(dataLeft)
    decoded = Data.decode('utf-8')
    print (decoded)
    break

serial.close()
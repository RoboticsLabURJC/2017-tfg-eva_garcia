import sys
import serial
from time import sleep
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Usar los motores (M1 y M2) componiendo el mensaje completo para mandar exactamente los valores")

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
  print ("Enter velocity for left motor (-255,255)")
  izdo=input()
  print ("Enter velocity for rigth motor (-255,255)")
  dcho=input()
  
  mensaje = f"{izdo};{dcho}"
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
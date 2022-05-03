import sys
import serial
from time import sleep
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Leer del sensor de distancia (ultrasonic): el valor se decodifica en el lado PC (python)")

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
sleep (1)
while 1:
    Data = serial.readline()
    decoded = Data.decode()
    print(decoded)
    
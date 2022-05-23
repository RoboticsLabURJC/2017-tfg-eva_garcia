import sys
import serial
from time import sleep
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Eco: python solo escucha")

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

while 1:
    Data = serial.read()
    sleep (1)
    dataLeft = serial.inWaiting()
    Data += serial.read(dataLeft)
    decoded = Data.decode('utf-8')
    print (decoded)
serial.close()
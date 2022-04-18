import sys
import serial
from time import sleep
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Leer del sensor infrarrojo: el valor se envía por el puerto serial y se interpreta en el lado pc (python)")

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
    value = int(decoded)
    if (value == 0):
        print ("sensor 1 y 2 no reciven valor: 00")
    elif (value == 1):
        print ("sensor 2 recive valor y el 1 no: 01")
    elif (value == 2):
        print ("sensor 1 recive valor y el 2 no: 10")
    elif (value == 3):
        print ("sensores 1 y 2 reciven valor: 11")
    else:
        print("valor inesperado")


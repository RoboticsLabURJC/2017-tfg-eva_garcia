# Nombre: potenciometro.py
# Descripcion: usamos un potenciometro y mostramos su salida
# Autor: Julio Vega

import pyfirmata
import os
from pyfirmata import Arduino, util
from time import sleep

# placa representa a nuestro objeto de Arduino
placa = pyfirmata.Arduino('/dev/ttyACM0')

print('Firmata version: %d.%d' % placa.get_firmata_version())
print('pyFirmata version:', pyfirmata.__version__)

sleep(5) # esperamos para que la conexion sea estable

it = util.Iterator(placa)

it.start()

a0 = placa.get_pin('a:0:i') # a0 pin analogico usado como pin de entrada

try:
  while True: # monitorizamos continuamente la salida del potenciometro
    p = a0.read()
    print p

except KeyboardInterrupt: # evita que al cerrar programa no se cierre bien
  board.exit()
  os._exit()

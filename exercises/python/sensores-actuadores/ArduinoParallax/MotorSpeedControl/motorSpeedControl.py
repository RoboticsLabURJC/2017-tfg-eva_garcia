# Nombre: motorSpeedControl.py
# Descripcion: controlamos la velocidad de un motor
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

motor = placa.get_pin('d:3:p') # motor conectado en pin 3 en modo PWM

def motorDCControl(s, t):
  motor.write(s/100.00)
  sleep(t)
  motor.write(0)

try:
  while True: # monitorizamos continuamente el estado del motor
    s = input("Por favor, introduzca un valor de velocidad al motor (1-100): ")

    if (s > 100) or (s <= 0):
      print "Por favor, introduzca un valor adecuado."
      placa.exit()
      break

    t = input("¿Durante cuánto tiempo? (segundos)")
    motorDCControl(s, t)

except KeyboardInterrupt: # evita que al cerrar programa no se cierre bien
  placa.exit()
  os._exit


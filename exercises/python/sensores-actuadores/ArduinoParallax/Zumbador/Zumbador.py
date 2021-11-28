# Nombre: Zumbador.py
# Descripcion: controlamos un zumbador. Mostramos dos patrones de ejemplo
# Autor: Julio Vega

import pyfirmata
from time import sleep

def patronZumbador(pin, repeticion, patron):
  patron1 = [0.8, 0.2, 0.8]
  patron2 = [0.1, 0.3, 0.5]
  flag = True

  for i in range(repeticion):
    if patron == 1:
      p = patron1
    elif patron == 2:
      p = patron2

    else:
      print "Introduzca un patron valido: 1 o 2."
      exit

    for delay in p:
      if flag is True:
        placa.digital[pin].write(1)
        flag = False
        sleep(delay)
      else:
        placa.digital[pin].write(0)
        flag = True
        sleep(delay)

  placa.digital[pin].write(0)
  placa.exit()

# placa representa a nuestro objeto de Arduino
placa = pyfirmata.Arduino('/dev/ttyACM0') # puerto al que tenemos conectado la placa Arduino

print('Firmata version: %d.%d' % placa.get_firmata_version()) # version de Firmata que esta usando la placa
print('pyFirmata version:', pyfirmata.__version__) # version de pyFirmata que tenemos en el ordenador

sleep(5) # esperamos para que la conexion sea estable

patronZumbador(4, 10, 2) # llamamos a funcion que ejecuta un patron de sonidos


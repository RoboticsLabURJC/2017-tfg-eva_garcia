# Nombre: luzSensor.py
# Descripcion: usamos un sensor de luz BH1750 con librería PyMata
# Autor: Julio Vega

import time
from PyMata.pymata import PyMata

port = PyMata("COM5")

port.i2c_config(0, port.ANALOG, 4, 5)

port.i2c_read(0x23, 0, 2, port.I2C_READ) # pedimos al dispositivo enviar 2 bytes

time.sleep(3) # esperamos al mismo

data = port.i2c_get_read_data(0x23) # leemos informacion

LuxSum = (data[1] << 8 | data[2]) >> 4 # obtenemos valores de luz de lo recibido

lux = LuxSum/1.2

print str(lux) + ' lux'

firmata.close()

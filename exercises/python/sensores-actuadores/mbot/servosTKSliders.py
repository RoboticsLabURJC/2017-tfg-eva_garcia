#!/usr/bin/python
# Nombre: P3-PythonServoControl.py
# Descripcion: controlamos dos servos mediante un par de sliders con libreria Tk
# Autor: Julio Vega

import pyfirmata
from Tkinter import *

# placa representa a nuestro objeto de Arduino
placa = pyfirmata.Arduino('/dev/ttyACM0') # puerto al que tenemos conectado la placa Arduino

print('Firmata version: %d.%d' % placa.get_firmata_version()) # version de Firmata que esta usando la placa
print('pyFirmata version:', pyfirmata.__version__) # version de pyFirmata que tenemos en el ordenador

# Si se utilizan uno o mas pines de entrada es necesario crear un thread iterador, de lo contrario la placa puede seguir enviando datos por la conexion serial hasta producir un desbordamiento. Asi que lanzamos un thread:
iterator = pyfirmata.util.Iterator(placa)
iterator.start()

# configuramos los pines 12 y 13 como servos derecho e izquierdo respectivamente
pinDerecho = placa.get_pin('d:12:s')
pinIzquierdo = placa.get_pin('d:13:s')
 
def move_servo1(a):
    pinDerecho.write(a)

def move_servo2(b):
    pinIzquierdo.write(b)
 
# configuramos el GUI
root = Tk()
 
# dibujamos un par de sliders para controlar las posiciones de los servos
scale1 = Scale(root,
    command = move_servo1,
    to = 175,
    orient = HORIZONTAL,
    length = 400,
    label = 'Servo Derecho (95 = centro/parado)')
scale1.pack(anchor = CENTER)

scale2 = Scale(root,
    command = move_servo2,
    to = 175,
    orient = HORIZONTAL,
    length = 400,
    label = 'Servo Izquierdo (95 = centro/parado)')
scale2.pack(anchor = CENTER)

# lanzamos el bucle del GUI Tk
root.mainloop()

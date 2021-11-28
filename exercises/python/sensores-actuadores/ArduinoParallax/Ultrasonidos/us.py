# Nombre: us.py
# Descripcion: leemos lo sensado por el ultrasonidos
# Autor: Julio Vega

import serial # Hacemos uso de la libreria serial

puerto = serial.Serial('/dev/ttyACM0', 9600) # puerto serial de comunicacion

while (1==1):
    if (puerto.inWaiting()>0):
        myData = puerto.readline()
        print myData # mostramos los valores leidos del sensor de Ultrasonidos

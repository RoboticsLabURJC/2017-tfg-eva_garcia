import sys
from time import sleep
from Library_Mbot_v1 import *

print ("Usar los motores (M1 y M2) componiendo el mensaje completo para mandar exactamente los valores")

serial = open_PortSerial("com3")

while True:
    try:
        print ("Send new message or quit?")
        cadena=input()
        if (cadena.lower() == 'quit'):
            send_Quit(serial)
            break
        print ("Enter velocity for left motor (-255,255)")
        izdo=input()
        print ("Enter velocity for rigth motor (-255,255)")
        dcho=input()
        
        mensaje = f"{izdo};{dcho}"
        turnOn_Motors([100,100],serial)
    except KeyboardInterrupt:
        send_Quit(serial)
        break

serial.close()
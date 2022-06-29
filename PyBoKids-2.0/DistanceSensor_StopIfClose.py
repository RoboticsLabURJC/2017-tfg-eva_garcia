# -- Aquí los módulos necesarios
import sys
import serial
from time import sleep
from Library_Mbot_v1 import *


#-- Poner aquí las variables globales, si se necesitan

#-- Sacar mensaje inicial: qué va a hacer el robot



while 1: # -- para que sea infinito
    try:
        #--Escribe aquí el programa principal
        functions_mbot()
        break
    except KeyboardInterrupt:
        send_Quit(serial)
        break

sys.exit(0)

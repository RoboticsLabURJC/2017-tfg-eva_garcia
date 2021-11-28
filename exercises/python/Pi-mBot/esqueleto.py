#Plantilla para el Pi-mBot; hasta que no se pulse el boton principal de la placa
#Arduino, no se empieza el programa.
#Eva García

import sys
import time
from ArduinoJdeRobot import MBot

def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)


robot = MBot("/dev/ttyUSB0") # Conectamos con el robot

#hacemos la llamada a leer boton "bloqueante", hasta que no lo lea, se queda
#esperando a que se pulse.
while True:
	but = robot.leerBoton() # leemos el boton
	if (but == 1):
		empezar = True
		break #si lo hemos leído, salimos del bucle
	time.sleep(0.2)

if empezar == True:
	##lo que tenga que hacer el robot
	pass

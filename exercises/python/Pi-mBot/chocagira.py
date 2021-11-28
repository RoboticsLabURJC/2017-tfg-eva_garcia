#Choca-gira de Kids rehecho para el Pi-mBot;
#Eva García

import sys
import time
from mBotReal import *

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
	vel_lineal = 100
	vel_giro = 100

	while True:
		robot.move(vel_lineal, 0)
		val = robot.leerUltrasonido()
		if (val < 10):
			robot.move(0,0)
			time.sleep(0.5)
			robot.move(-vel_lineal, 0)
			time.sleep(1)
			robot.move(0, -vel_giro)
			time.sleep(1)
			val = robot.leerUltrasonido()

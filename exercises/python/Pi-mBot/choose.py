#Eva García

import sys
import time
from ArduinoJdeRobot import MBot

def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)


robot = MBot("/dev/ttyUSB0") # Conectamos con el robot
patron1 = [1, 2, 3]
patron2 = [3, 2, 1]
#hacemos la llamada a leer boton "bloqueante", hasta que no lo lea, se queda
#esperando a que se pulse.
# while True:
# 	but = robot.leerBoton() # leemos el boton
# 	if (but == 1):
# 		empezar = True
# 		break #si lo hemos leído, salimos del bucle
# 	time.sleep(0.2)
#
# if empezar == True:
while True:
	robot.escribirFrase(4, "Que quieres?")
	time.sleep(1)
	robot.borrarMatriz(4)
	patron = input("choice")
	patron = int(patron)
	if patron == 1:
		robot.avanzar(100)
	elif patron == 2:
		robot.retroceder(100)
	time.sleep(2)
	robot.parar()

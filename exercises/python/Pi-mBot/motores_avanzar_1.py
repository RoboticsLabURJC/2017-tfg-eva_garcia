# Descripcion: Avanza durante 5 segundos el Pi-mBot, pero no empieza hasta que
#no se pulsa el botón, para que sea más autónomo
# Autora: Eva García

# Módulos necesarios
import sys
import time
from ArduinoJdeRobot import MBot

def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)

robot = MBot("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

while True:
	but = robot.leerBoton() # leemos el boton
	if (but == 1):
		empezar = True
		break #si lo hemos leído, salimos del bucle
	time.sleep(0.2)

if empezar == True:
	robot.avanzar(-100)
	time.sleep(10)
	robot.parar()
	robot.girarDerecha(-100)
	time.sleep(2)
	robot.parar()
	robot.avanzar(-100)
	time.sleep(10)
	robot.parar()

	sys.exit(0)

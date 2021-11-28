# Importando modulos necesarios
import sys
import signal
import time
from ArduinoRobot.arduinoRobot import *


# Señal para poder desconectar del robot bien
def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	if robot is not None:
		robot.reset()
	sys.exit(0)


robot = ArduinoRobot("/dev/ttyACM0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

signal.signal(signal.SIGINT, signal_handler) #activamos la señal de desconexion


# introduce tu codigo aqui

ant_val = -1
while True:

	val = robot.leerSensorLuz(2)
	if val != ant_val:
		print(str(val))

	ant_val = val

	time.sleep(0.1)

		
robot.reset() # resetea el robot

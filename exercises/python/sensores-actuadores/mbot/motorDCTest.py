# Nombre: avance.py
# Descripcion: Avanza durante 5 segundos
# Autor: Julio Vega y Aitor Martinez

# Importando modulos necesarios
import sys
from time import sleep
from ArduinoJdeRobot import MBot

robot = MBot("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

while(True):
	robot.avanzar(100)
	print( "Avanzando")
	sleep(2)
	robot.retroceder(100)
	print( "Retrocediendo")
	sleep(2)
	robot.parar()
	print ("Parado")
	sleep(2)
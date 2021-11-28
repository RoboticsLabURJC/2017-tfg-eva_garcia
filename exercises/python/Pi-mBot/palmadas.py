#Práctica "reformada" de kids para el pi-mbot
#Eva García

import sys
import time
from ArduinoJdeRobot import MBot

def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)


def start(robot):
	while True:
		but = robot.leerBoton() # leemos el boton
		if (but == 1):
			empezar = True
			return empezar #si lo hemos leído, salimos del bucle
		time.sleep(0.2)

def calibrado(robot):
	ambiente = 0
	for i in range(100):
		ambiente += robot.leerIntensidadSonido()
		ambiente = ambiente / 100
	calibrado = 0
	lvl = 5
	print("Da una palmada")
	for i in range(lvl):
		while True:
			calibrar = robot.leerIntensidadSonido()
			if calibrar > ambiente + 150:
				time.sleep(1)
				calibrado += calibrar
				break
		print("Da otra")
	calibrado /= lvl
	print("el nivel de calibrado es", calibrado)
	return calibrado

if __name__ == "__main__":
	robot = MBot("/dev/ttyUSB0") # Conectamos con el robot
	threshold = calibrado(robot)
	avanzando = True
	while True:
		val = robot.leerIntensidadSonido()
		print (val)
		if val > threshold:
			avanzando = not avanzando
			if avanzando:
				print ("para!")

				robot.parar()
				time.sleep(1)
			else:
				print ("Avanza!")
				robot.avanzar(100)

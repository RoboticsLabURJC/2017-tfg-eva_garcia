#práctica de kids de lucha de sumo "reformada" para pi-mbot
#Eva García

import sys
import time
from ArduinoJdeRobot import MBot

def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)


def start (self, robot):
	#hacemos la llamada a leer boton "bloqueante", hasta que no lo lea, se queda
	#esperando a que se pulse.
	while True:
		but = robot.leerBoton() # leemos el boton
		if (but == 1):
			empezar = True
			break #si lo hemos leído, salimos del bucle
		time.sleep(0.2)
	return empezar


if __name__ == "__main__":
	robot = MBot("/dev/ttyUSB0") # Conectamos con el robot
	empezar = start(robot)
	if empezar == True:
		while True:
			distancia = robot.leerUltrasonidos()
			linea = robot.leerIRSigueLineas()

			if (linea == 3 or linea == 2 or linea == 1):  #estamos al borde del ring!
				robot.parar()
				robot.retroceder(100)
				time.sleep(1)
				robot.girarIzquierda(100)  # podemos hacer un giro aleatorio.
				time.sleep(1)
			else:
				if distancia < 50:   #oponente localizado!
					robot.avanzar(255)
					if distancia < 10:  #estamos pegados, usemos el servo!
						robot.moverServo(4,1,170)
						time.sleep(0.5)
					else:
						robot.moverServo(4,1,60)
						time.sleep(0.5)
				else:   #buscamos a nuestro oponente
					robot.girarDerecha(90)

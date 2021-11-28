# Descripcion: para mbot o pi-mbot; control remoto con el mando.
# Tipo joystick: para mantener el movimiento hay que mantener la tecla pulsada
# Autora: Eva García

# Módulos necesarios
import sys
import time
from mBotReal import *

def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)

robot = MBotReal("/dev/ttyUSB0") # Conectamos con el robot
vel = 100
while True:
	valor_mando = robot.leerMandoIR()
	if (valor_mando == "DERECHA"):
		print("girando derecha")
		robot.girarDerecha(vel)
	elif (valor_mando == "IZQUIERDA"):
		print("girando izquierda")
		robot.girarIzquierda(vel)
	elif (valor_mando == "ARRIBA"):
		print ("avanzando")
		robot.avanzar(vel)
	elif (valor_mando == "ABAJO"):
		print ("retrocediendo")
		robot.retroceder(vel)
	elif (valor_mando == "0"):
		robot.parar()

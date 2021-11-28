# Nombre: Zumbador.py
# Descripcion: controlamos un zumbador. Mostramos dos patrones de ejemplo
# Autor: Julio Vega y Aitor Martinez




# Importando modulos necesarios
import sys
import signal
import time
from ArduinoJdeRobot import ArduinoRobot
from ArduinoJdeRobot import BOTON_CEN, BOTON_DER, BOTON_IZQ, BOTON_SUP, BOTON_INF


# Señal para poder desconectar del robot bien
def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	if robot is not None:
		robot.reset()
	sys.exit(0)


robot = ArduinoRobot("/dev/ttyACM0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

signal.signal(signal.SIGINT, signal_handler) #activamos la señal de desconexion


def patronZumbador(robot, repeticion, patron):
	patron1 = [0.8, 0.2, 0.8]
	patron2 = [0.1, 0.3, 0.5]

	for i in range(repeticion):
		if patron == 1:
			p = patron1
		elif patron == 2:
			p = patron2
		else:
			print("Introduzca un patron valido: 1 o 2.")
			return
		for delay in p:
			robot.playTono(delay)

patronZumbador(robot, 10, 2) # llamamos a funcion que ejecuta un patron de sonidos
		
robot.reset() # resetea el robot
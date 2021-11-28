# Nombre: Zumbador.py
# Descripcion: controlamos un zumbador. Mostramos dos patrones de ejemplo
# Autor: Julio Vega y Aitor Martinez

# Importando modulos necesarios
import sys
import signal
import time
from ArduinoJdeRobot import MBot


# Señal para poder desconectar del robot bien
def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler) #activamos la señal de desconexion

robot = MBot("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)




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
			robot.playTono("C3", delay)

patronZumbador(robot, 10, 2) # llamamos a funcion que ejecuta un patron de sonidos

robot.reset() # resetea el robot

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

print("Empieza a pulsar")

while True:
	but = robot.leerBoton() # leemos el valor de los botones
	# comparamos con cada uno de los botones para saber cual es
	if (but == 1):
		print("Boton Pulsado")
		
	time.sleep(0.2) # esperamos 0.2 segundos para no saturar al robot

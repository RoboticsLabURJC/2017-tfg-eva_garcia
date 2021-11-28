# Importando modulos necesarios
import sys
import signal
import time
from ArduinoJdeRobot import MBot


# Señal para poder desconectar del robot bien
def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)


robot = MBot("/dev/ttyUSB0") # Conectamos con el robot

signal.signal(signal.SIGINT, signal_handler) #activamos la señal de desconexion


encender = True # permite encender y apagar el led con un boton
print("Empieza a pulsar")

while True:
	but = robot.leerBoton() # leemos el valor del boton
	
	if (but == 1):
		if (encender):
			robot.encenderLed(2) # encendemos el LED izquierdo
		else:
			robot.apagarLed(2) # apagamos el LED derecho
			
		encender = not encender
	
	
	time.sleep(0.2) # esperamos 0.2 segundos para no saturar al robot

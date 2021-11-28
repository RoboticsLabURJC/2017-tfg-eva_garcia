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


robot = ArduinoRobot("/dev/ttyACM0") # Conectamos con el robot

signal.signal(signal.SIGINT, signal_handler) #activamos la señal de desconexion


encender = True # permite encender y apagar el led con un boton
print("Empieza a pulsar")

while True:
	but = robot.leerBoton() # leemos el valor de los botones
	# comparamos con cada uno de los botones para saber cual es
	
	if (but == BOTON_CEN):
		if (encender):
			robot.encenderLed(2) # encendemos el LED frontal
		else:
			robot.apagarLed(2) # apagamos el LED frontal
			
		encender = not encender
	
	
	time.sleep(0.2) # esperamos 0.2 segundos para no saturar al robot
		
robot.reset() # resetea el robot

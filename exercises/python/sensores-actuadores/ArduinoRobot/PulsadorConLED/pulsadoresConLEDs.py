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

print("Empieza a pulsar")

while True:
	but = robot.leerBoton() # leemos el valor de los botones
	# comparamos con cada uno de los botones para saber cual es
		
	if (but == BOTON_IZQ):
		robot.encenderLed(4)
		
			
	if (but == BOTON_DER):
		robot.encenderLed(0)
		
		
	if (but == BOTON_SUP):
		robot.encenderLed(2)
		
	
	if (but == BOTON_CEN):
		# Apagamos todos los LEDs
		robot.apagarLed(0)
		robot.apagarLed(2)
		robot.apagarLed(4)
		
	
	
	time.sleep(0.2) # esperamos 0.2 segundos para no saturar al robot
		
robot.reset() # resetea el robot


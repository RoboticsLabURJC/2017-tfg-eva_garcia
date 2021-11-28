# Descripcion: Para el Pi-mBot, enciende leds de la placa, pero no empieza hasta que
#no se pulsa el boton
# Autora: Eva García

# Módulos necesarios
import sys
import time
from ArduinoJdeRobot import MBot

def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)

robot = MBot("/dev/ttyUSB0") # Conectamos con el robot
	#hacemos la llamada a leer boton "bloqueante", hasta que no lo lea, se queda
	#esperando a que se pulse.
while True:
	but = robot.leerBoton() # leemos el boton
	if (but == 1):
		empezar = True
		break #si lo hemos leído, salimos del bucle
	time.sleep(0.2)

patron_leds = [0,1,2]
if empezar == True:
	
	for i in patron_leds:
		robot.encenderLedPlaca(i, 255,0,0)
		time.sleep(2)
		robot.apagarLedPlaca(i)
		time.sleep(0.2)

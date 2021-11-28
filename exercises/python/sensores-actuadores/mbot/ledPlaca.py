# Importando modulos necesarios
import sys
import signal
import time
from ArduinoJdeRobot import MBot
#from ArduinoJdeRobot import BOTON_CEN, BOTON_DER, BOTON_IZQ, BOTON_SUP, BOTON_INF


# Señal para poder desconectar del robot bien
def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)

if __name__ == "__main__":
	robot = MBot("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

	signal.signal(signal.SIGINT, signal_handler) #activamos la señal de desconexion

	time.sleep(2) #para que no empieze nada más arrancar

	#Los Led de la placa son 1 o 2. El 0, para encender o apagar los dos
	robot.encenderLedPlaca(1,255,0,0) #rojo
	time.sleep(2)
	robot.encenderLedPlaca(2, 0, 255, 0) #verde
	time.sleep(2)

	robot.apagarLedPlaca(0)#apagamos los dos porque si no se queda encendido

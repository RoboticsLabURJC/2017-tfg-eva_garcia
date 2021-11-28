# Importando modulos necesarios
import sys
import signal
import time
from ArduinoJdeRobot import MBot
#from ArduinoJdeRobot import BOTON_CEN, BOTON_DER, BOTON_IZQ, BOTON_SUP, BOTON_INF

# Senal para poder desconectar del robot bien
def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)

if __name__ == "__main__":

        robot = MBot("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

        signal.signal(signal.SIGINT, signal_handler) #activamos la senal de desconexion

        # introduce tu codigo aqui
        while True:
                
                val = robot.leerIntensidadSonido()
                print(val)
                time.sleep(0.1)

# Importando modulos necesarios
import sys
import signal
import time
from ArduinoJdeRobot import MBot

# Señal para poder desconectar del robot bien
def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)

if __name__ == "__main__":

        robot = MBot("/dev/ttyUSB0") # Conectamos con el robot

        signal.signal(signal.SIGINT, signal_handler) #activamos la señal de desconexion

        robot.pintarDibujo(4, "FLECHA_ABAJO")

        time.sleep(3)
        robot.borrarMatriz(4)

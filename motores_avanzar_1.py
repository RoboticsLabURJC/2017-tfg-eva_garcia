# Descripcion: Avanza durante 5 segundos el Pi-mBot, pero no empieza hasta que
#no se pulsa el botón, para que sea más autónomo
# Autora: Eva García

# Módulos necesarios
import sys
import time
from ArduinoJdeRobot import MBot

def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)
robot = MBot("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

while True:
	but = robot.leerBoton()
    if (but == 1):
            robot.avanzar(100)
            time.sleep(5)
            robot.parar()
            break
    break

sys.exit(0)

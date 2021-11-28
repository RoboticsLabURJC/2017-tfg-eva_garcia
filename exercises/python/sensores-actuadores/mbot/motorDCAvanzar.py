# Nombre: avance.py
# Descripcion: Avanza durante 5 segundos
# Autor: Julio Vega y Aitor Martinez

# Importando modulos necesarios
import sys
import time
from ArduinoJdeRobot import MBot


print("+++++++++++++++++++++++++++++++++++")
robot = MBot("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

robot.avanzar(100)
#robot.bot.doMove(100,100)
time.sleep(5)
robot.parar()
print("parado")

sys.exit(0)

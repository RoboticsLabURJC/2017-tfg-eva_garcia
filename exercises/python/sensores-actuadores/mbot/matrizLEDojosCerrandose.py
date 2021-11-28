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

    ojos1 = [0,24,36,66,66,36,24,0,0,24,36,66,66,36,24,0]
    ojos2 = [0,24,36,34,34,36,24,0,0,24,36,34,34,36,24,0]
    ojos3 = [0,24,20,18,18,20,24,0,0,24,20,18,18,20,24,0]
    ojos4 = [0,8,12,10,10,12,8,0,0,8,12,10,10,12,8,0]
    ojos5 = [0,8,4,6,6,4,8,0,0,8,4,6,6,4,8,0]
    ojos6 = [0,8,4,2,2,4,8,0,0,8,4,2,2,4,8,0]

    lista = [ojos1, ojos2, ojos3, ojos4, ojos5, ojos6, ojos5, ojos4, ojos3, ojos2]

    while True:
        for i in lista:
           robot.dibujar(4, i)
           time.sleep(0.2)
        
    robot.borrarMatriz(4)

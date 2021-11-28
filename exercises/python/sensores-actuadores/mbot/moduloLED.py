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

        while True:
                robot.apagarLed(0,4)
                modo = input("Selecciona modo de encendido \n a) Carrusel rojo (por defecto) \n b) Carrusel verde \n c) Carrusel azul \n d) Carrusel personalizado \n e) Salir \n")
                if modo == "a":
                        r = 255
                        g = 0
                        b = 0
                elif modo == "b":
                        r = 0
                        g = 255
                        b = 0
                elif modo == "c":
                        r = 0
                        g = 0
                        b = 255
                elif modo == "d":
                        r = int(input("Introduce el valor de rojo "))
                        g = int(input("Introduce el valor de verde "))
                        b = int(input("Introduce el valor de azul "))
                        if r > 255 and r < 0:
                                r = 0
                        if g > 255 and g < 0:
                                g = 0
                        if b > 255 and b < 0:
                                b = 0
                elif modo == "e":
                        break
                else:
                        r = 255
                        g = 0
                        b = 0

                vueltas = int(input("Introduce numero de vueltas "))
                for v in range(vueltas):
                        robot.apagarLed(0,4)
                        for i in range (1,5):
                                robot.encenderLed(i,r,g,b,4) # encendemos el LED izquierdo
                                time.sleep(0.2) # esperamos 0.2 segundos para no saturar al robot

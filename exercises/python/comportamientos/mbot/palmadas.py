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

def calibracion(robot):
        ambiente = 0
        for i in range(100):
                ambiente += robot.leerIntensidadSonido()
        ambiente = ambiente / 100

        print("el ruido ambiente es:",ambiente)

        calibrado = 0
        lvl = 0
        while lvl < 5 or lvl > 10:
                lvl = input("Vamos a calibrar el sensor. Elige nivel de calibrado (5-10)")
                lvl = int(lvl)

        print("Da una palmada")
        for i in range(lvl):
                while True:
                        calibrar = robot.leerIntensidadSonido()
                        if calibrar > ambiente + 150:
                                time.sleep(1)
                                calibrado += calibrar
                                break
                print("Da otra")
        calibrado /= lvl
        print("el nivel de calibrado es", calibrado)
        return calibrado
                

if __name__ == "__main__":

        robot = MBot("COM4") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

        signal.signal(signal.SIGINT, signal_handler) #activamos la señal de desconexion

        threshold = calibracion(robot)
        avanzando = True
        
        # introduce tu codigo aqui
        while True:
        
                val = robot.leerIntensidadSonido()
                if val > threshold:
                        time.sleep(1)
                        avanzando = not avanzando
                        if avanzando:
                                print("Para!")
                                robot.parar(100)
                        else:
                                print("Avanza!")
                                robot.avanzar(100)
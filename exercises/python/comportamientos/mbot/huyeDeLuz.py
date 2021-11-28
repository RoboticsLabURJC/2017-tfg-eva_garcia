# Importando modulos necesarios
import time
from ArduinoJdeRobot import MBot

# Señal para poder desconectar del robot bien
def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)

if __name__ == "__main__":

        robot = MBot("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)
        
        ambiente = 0
        for i in range(10000):
                ambiente += robot.leerIntensidadLuz()
        ambiente = ambiente / 10000

        print("La intensidad de luz ambiente es ambiente es:",ambiente)
        
        # introduce tu codigo aqui
        vel = 100
        while True:
        	
        	val = robot.leerIntensidadLuz()
        	print(val)
        	if (val > ambiente+100):
        		robot.retroceder(vel)
        		time.sleep(0.5)
        		robot.girarDerecha(vel)
        		time.sleep(0.3)
        	robot.avanzar(vel)
        	time.sleep(0.3)
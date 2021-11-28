# Importando modulos necesarios
import time
from ArduinoJdeRobot import MBot

# Señal para poder desconectar del robot bien
def signal_handler(sig, frame):
	print('Has pulsado Ctrl+C')
	sys.exit(0)

if __name__ == "__main__":

        robot = MBot("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot si no se va a conectar por wifi
        
        while True:
            distancia = robot.leerUltrasonidos()
            linea = robot.leerIRSigueLineas()
            
            if (linea == 3 or linea == 2 or linea == 1):  #estamos al borde del ring!
                robot.parar()
                robot.retroceder(100)
                time.sleep(1)
                robot.girarIzquierda(100)  # podemos hacer un giro aleatorio.
                time.sleep(1)
            else:
                if distancia < 50:   #oponente localizado!
                    robot.avanzar(255)
                    if distancia < 10:  #estamos pegados, usemos el servo!
                        robot.moverServo(4,1,170)
                        time.sleep(0.5)
                    else:
                        robot.moverServo(4,1,60)
                        time.sleep(0.5)
                else:   #buscamos a nuestro oponente
                    robot.girarDerecha(90)


# Nombre: PiedraPapelTijera.py
# Descripcion: en este clásico juego, vamos a necesitar la matriz de LEDs, un zumbador y un pulsador. La idea es obtener un número aleatorio en cada tirada del juego, para que juguemos contra el ordenador. El símbolo que saque éste se representará en la matriz de LEDs, emitiendo un pitido según sea piedra, papel o tijera.
# Autor: Julio Vega

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

    # Simbolo P I E
    piedra = [0,0,0,126,74,74,48,0,62,0,62,42,42,0,0,0,0]
    # Simbolo P A
    papel = [0,0,0,126,74,74,48,0,30,40,40,30,0,0,0,0]
    # Simbolo T I J
    tijera = [0,0,64,64,126,64,64,0,62,0,2,2,60,0,0,0]

    lista = [piedra, papel, tijera]

    patron1 = [0.8, 0.2, 0.8]
    patron2 = [0.1, 0.3, 0.5]
    patron3 = [0.5, 0.1, 0.8]

    while True:
        for i in range(lista):
           if i == 0:
             robot.dibujar(4, piedra)
             p = patron1

           if i == 1:
             robot.dibujar(4, papel)
             p = patron2

           if i == 2:
             robot.dibujar(4, tijera)
             p = patron3

           but = robot.leerBoton() # leemos el valor de los botones
           # comparamos con cada uno de los botones para saber cual es
           if (but == 1):
             print("Boton Pulsado")
             time.sleep(2.0) # esperamos 2 seg. para que usuario compare con lo que ha sacado
           else:
             time.sleep(0.2)

           for delay in p:
             robot.playTono("C3", delay)

    robot.borrarMatriz(4)

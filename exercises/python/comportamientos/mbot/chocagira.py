import time
from mBotReal import *


robot = MBotReal("/dev/ttyUSB0") # Conectamos con el robot, hay que indicar el puerto del robot (mirar aplicacion arduino)

# introduce tu codigo aqui
vel = 100
while True:

	val = robot.leerUltrasonido()
	print(val)
	if (val < 10):
		robot.mvoe(-vel_lineal, 0)
		time.sleep(0.5)
		robot.mvoe(0, vel_gir)
		time.sleep(0.3)
	robot.move(vel_lineal, 0)
	time.sleep(0.3)

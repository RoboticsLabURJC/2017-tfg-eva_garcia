from lib.mBot import *
bot = mBot()
bot.startWithSerial("/dev/ttyUSB0")

while(1):
	try:
	
		bot.moverServo(2, 1, 90)
		print( "[2,1] Garra Abriendo...")
		sleep(2)
		bot.moverServo(2, 1, 0)
		print( "[2,1] Garra Cerrando...")
		sleep(2)

	except Exception:
		print (str(Exception.msg))

# Nombre: P2-PythonConArduinoLED.py
# Descripcion: controlamos un led mediante un pulsador para encender y apagar
# Autor: Julio Vega

import pyfirmata

# placa representa a nuestro objeto de Arduino
placa = pyfirmata.Arduino('/dev/ttyACM0') # puerto al que tenemos conectado la placa Arduino

print('Firmata version: %d.%d' % placa.get_firmata_version()) # version de Firmata que esta usando la placa
print('pyFirmata version:', pyfirmata.__version__) # version de pyFirmata que tenemos en el ordenador

# Si se utilizan uno o mas pines de entrada es necesario crear un thread iterador, de lo contrario la placa puede seguir enviando datos por la conexion serial hasta producir un desbordamiento. Asi que lanzamos un thread:
pyfirmata.util.Iterator(placa).start()

entrada = placa.get_pin('d:8:i') # (d=digital(a=analog):pin 8:input(o=output,p=pwm)
entrada.enable_reporting() # para poder leer las senales recibidas a traves del pin 8
salida = placa.get_pin('d:12:o')

try:
    encendido = False
    while True: # bucle infinito
        if entrada.read(): # este metodo devuelve 0 si el voltaje de entrada es menor a 2.5V, o 1 si es mayor a 2.5V. 
            encendido = not encendido
            salida.write(encendido) # escribe a un pin digital, enviando como argumento False (0V) o True (5V)
            placa.pass_time(0.2) # para pausar el programa durante 0.2 segundos, si no se pone el programa puede no sensar nuestra pulsacion de boton

finally:
    salida.write(False)
    placa.exit()


import sys
import serial
from time import sleep
#-- Cadena de pruebas a enviar

#-- Sacar mensaje inicial
print ("Encender Buzzer componiendo el mensaje completo para mandar la nota deseada, siguiendo el sistema americano de escala: C es Do [...] hasta el Si que es la B. Para elegir notas más graves o más agudas, después de la letra, va un numero desde el 1 hasta el 7. Por ejmplo: D4")

notas_diccionario = {'B0':31,'C1':33,'D1':37,'E1':41,'F1':44,'G1':49,'A1':55,'B1':62,
                    'C2':65,'D2':73,'E2':82,'F2':87,'G2':98,'A2':110,'B2':123,
                    'C3':131,'D3':147,'E3':165,'F3':175,'G3':196,'A3':220,'B3':247,
                    'C4':262,'D4':294,'E4':330,'F4':349,'G4':392,'A4':440,'B4':494,
                    'C5':523,'D5':587,'E5':659,'F5':698,'G5':784,'A5':880,'B5':988,
                    'C6':1047,'D6':1175,'E6':1319,'F6':1397,'G6':1568,'A6':1760,'B6':1976,
                    'C7':2093,'D7':2349,'E7':2637,'F7':2794,'G7':3136,'A7':3520,'B7':3951,'C8':4186,'D8':4699}

try:
    serial = serial.Serial('com3', 9600, timeout=1)
except serial.SerialException:
    #-- Error al abrir el puerto serie
    sys.stderr.write("Error al abrir puerto (%s)\n")
    sys.exit(1)
cadena= ''
while True:
    print ("Send new message or quit? Type 'show' for seeing all possible notes")
    cadena=input()
    if (cadena.lower() == 'quit'):
        serial.write(bytes(cadena, 'utf-8'))
        break
    elif (cadena.lower() == 'show'):
        print (notas_diccionario.keys())
        continue

    print ("Enter the note")
    note=input()
    noteInt = notas_diccionario[note.upper()]
    print ("Enter the duration -in seconds- for the note")
    duration=input()
    mensaje = f"{noteInt};{duration}"
    serial.write(bytes(mensaje, 'utf-8'))

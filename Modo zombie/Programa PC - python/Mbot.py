import sys
import serial
from time import sleep

Buzzer_Dictionary = {'B0':31,'C1':33,'D1':37,'E1':41,'F1':44,'G1':49,'A1':55,'B1':62,
                    'C2':65,'D2':73,'E2':82,'F2':87,'G2':98,'A2':110,'B2':123,
                    'C3':131,'D3':147,'E3':165,'F3':175,'G3':196,'A3':220,'B3':247,
                    'C4':262,'D4':294,'E4':330,'F4':349,'G4':392,'A4':440,'B4':494,
                    'C5':523,'D5':587,'E5':659,'F5':698,'G5':784,'A5':880,'B5':988,
                    'C6':1047,'D6':1175,'E6':1319,'F6':1397,'G6':1568,'A6':1760,'B6':1976,
                    'C7':2093,'D7':2349,'E7':2637,'F7':2794,'G7':3136,'A7':3520,'B7':3951,'C8':4186,'D8':4699}


def open_PortSerial (baudios, port, timeOutSec):
    try:
        serialAux = serial.Serial(port, baudios, timeout=timeOutSec)
        serialAux.setDTR(False)
        sleep(1)
        serialAux.flushInput()
        serialAux.setDTR(True)
        sleep (1)
        return serialAux
    except serial.SerialException:
        #-- Error al abrir el puerto serie
        sys.stderr.write("Error al abrir puerto (%s)\n")
        sys.exit(1)

#### ---- funciones de serial
def send_Message (message, serial):
    serial.write(bytes(message, 'utf-8'))


def read_Text_Message (serial):
    Data = serial.read()
    sleep (1)
    dataLeft = serial.inWaiting()
    Data += serial.read(dataLeft)
    decoded = Data.decode('utf-8')
    return decoded

def read_Sensor (serial):
    Data = serial.readline()
    try:
        decoded = Data.decode()
    except (UnicodeDecodeError):
        return -1 

    list = decoded.split(';')
    try:
      sensorValue = float(list[1])
    except (ValueError,IndexError):
      return -1 
    if (int(list[0]) == 0):
        return ["distance",sensorValue]
    elif (int(list[0]) == 1):
            return ["siguelineas",sensorValue]
    
 
"""def read_Sensor_Message (serial):
    Data = serial.readline()
    decoded = Data.decode()
    try:
      sensorValue = float(decoded)
      return sensorValue
    except (ValueError):
      return -1 """


#### ----- funciones de actuadores

# como estandar, los mensajes se mandan con un primer valor para que el residente distinga que actuador tiene que leer:
# 0 para los leds; 1 para los motores, 2 para el buzzer


def create_Message_Led (list):
    mensaje = f"0;{list[0]};{list[1]};{list[2]};{list[3]}"
    return mensaje

def create_Message_Buzzer(list):
    mensaje = f"2;{list[0]};{list[1]}"
    return mensaje

def create_Message_Motor(list):
    mensaje = f"1;{list[0]};{list[1]}"
    return mensaje

######

def ask_Message_Motors (serial): 
    print ("Type 'quit' for stopping or anything to send new message to motors")
    cadena=input()
    if (cadena.lower() == 'quit'):
        send_Message(cadena,serial)
        return -1
    print ("Enter velocity for left motor (-255,255)")
    izdo=input()
    print ("Enter velocity for rigth motor (-255,255)")
    dcho=input()
    list = [izdo,dcho]
    motors = create_Message_Motor(list)
    return motors

def ask_Message_Buzzer(serial):
    print ("Type 'quit' for stopping, 'show' for seeing all possible notes or anything to send new message to the buzzer")
    cadena=input()
    if (cadena.lower() == 'quit'):
        send_Message(cadena,serial)
        return -1
    elif (cadena.lower() == 'show'):
        print (Buzzer_Dictionary.keys())
    print ("Enter the note")
    note=input()
    noteInt = Buzzer_Dictionary[note.upper()]
    print ("Enter the duration -in seconds- for the note")
    duration=input()
    list = [noteInt,duration]
    Buzzer = create_Message_Buzzer(list)
    return Buzzer

def ask_Message_Led(serial):
    print ("Type 'quit' for stopping or anything to send new message to leds")
    cadena=input()
    if (cadena.lower() == 'quit'):
        send_Message(cadena,serial)
        return -1
    print ("Enter which ones led want to turn on: 0-both, 1-rigth, 2-left")
    leds=input()
    print ("Enter red value")
    red=input()
    print("Enter green value")
    green=input()
    print("Enter blue value")
    blue=input()
    list = [leds,red,green,blue]
    leds = create_Message_Led(list)
    return leds

######

def turnOn_Leds(list,serial):
    mensaje = create_Message_Led(list)
    send_Message(mensaje,serial)

def turnOn_Buzzer(list,serial):
    mensaje = create_Message_Buzzer(list)
    send_Message(mensaje,serial)

def turnOn_Motors(list,serial):
    mensaje = create_Message_Motor(list)
    send_Message(mensaje,serial)

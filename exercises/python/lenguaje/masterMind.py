#!/usr/bin/python
import random

def main():
 
 cadena = input ("Dime la longitud de la cadena: ")
 eleccion = raw_input ("Intenta adivinar la cadena: ")
 print ""

 aleatorio = num_aleat(cadena)
 tot = evalua(cadena, aleatorio, eleccion)
 print aleatorio
 print ""
 
 while eleccion != aleatorio:
  print "Con el numero", eleccion, "has tenido", tot, "aciertos"
  print ""
  eleccion = raw_input ("Intenta adivinar la cadena: ")
  tot = evalua(cadena, aleatorio, eleccion)
 
 print "" 
 print "Felicitaciones, has ganado...."
 raw_input()

def num_aleat(cad):
 numero_aleatorio = ""
 for i in range(cad):
  x = random.randint(0, 9)
  x = str(x)
  numero_aleatorio += x
 return numero_aleatorio
 
def evalua(cad, aleat, elecc):
 cont = 0
 a = 0
 b = 0
 for i in range(cad):
  if aleat[a] == elecc[b]:
   cont += 1
   a += 1
   b += 1
  else:
   a += 1
   b += 1
 return cont
    
main()

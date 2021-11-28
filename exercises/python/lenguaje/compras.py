#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

def promocion(): #Información del descuento
 print ""
 print "SU GASTO IGUALA O SUPERA LOS 100.00€ Y POR TANTO PARTICIPA EN LA PROMOCION."
 print ""
 print "  COLOR    DESCUENTO"
 print ""
 print "  BOLA BLANCA   NO TIENE"
 print "  BOLA ROJA   10 POR CIENTO"
 print "  BOLA AZUL   20 POR CIENTO"
 print "  BOLA VERDE   25 POR CIENTO"
 print "  BOLA AMARILLA   50 POR CIENTO"
 print ""
 
def calculo(valor): #Calculo de la función
 
 descuento = 0
 
 x = random.choice([0, 10, 20, 25, 50])
 
 bolas = {0:"BOLA BLANCA", 10:"BOLA ROJA", 20:"BOLA AZUL", 25:"BOLA VERDE", 50:"BOLA AMARILLA"}
 
 if x == 0:
  print "ALEATORIAMENTE USTED OBTUVO UNA BOLA BLANCA"
  print ""
  print "LAMENTABLEMENTE EN ESTA OCASIÓN NO HAY DESCUENTO"
  
 else:
  print "ALEATORIAMENTE USTED OBTUVO UNA", bolas[x]
  print ""
  print "FELICIDADES, HA GANADO UN", x, "POR CIENTO DE DESCUENTO"
  print ""
  print "SU NUEVO TOTAL A PAGAR ES:", (valor * x/100), " €"
  print ""
  
def compras(): #Funcion principal
 
 valor_compra = raw_input("INTRODUZCA LA CANTIDAD TOTAL DE LA COMPRA: ")
 
 valor_compra = float(valor_compra)
 
 if valor_compra < 100:
  print ""
  print "El cliente no tiene derecho a promocion!!!"
 else:
  promocion()
  calculo(valor_compra)
  
compras()

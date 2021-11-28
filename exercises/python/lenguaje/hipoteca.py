#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
 dolares = input ("Cuánto dinero: ")
 interes = input ("Tipo de interés: ")
 interes = float(interes)
 anos = input ("Número de años: ")
 print ""

 resultado = calculo (dolares, interes, anos)
 print "Cuando pasen", anos, u"años, con un", interes, u"de interes, usted habrá generado", resultado, "euros."

def calculo (dinero, inte, cant_anos):
 x =dinero * ((1 + inte/100) **cant_anos)
 return x

main()

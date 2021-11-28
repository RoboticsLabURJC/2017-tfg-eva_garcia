#!/usr/bin/python
uno = raw_input ("Dime la primera palabra: ")
print ""
dos = raw_input ("Dime la segunda palabra: ")
print ""

if len(uno) < 3 or len(dos) < 3:
 print "Las palabras tienen menos de 3 letras"
 print ""
elif uno[-3:] == dos[-3:]:
 print "Riman"
 print ""
elif uno[-2:] == dos[-2:]:
 print "Riman un poco"
 print ""
else:
 print "No riman"
 print ""

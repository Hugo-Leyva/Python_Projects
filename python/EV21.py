"""21.-Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde
 a Navidad."""
 
dia=int(input("Ingresa el día"))
mes=int(input("Ingresa el mes"))
año=int(input("Ingresa el año"))

if dia==25 and mes==12:
    print("Feliz Navidad")
else:
    print("No corresponde a navidad")


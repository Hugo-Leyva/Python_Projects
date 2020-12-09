"""Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre
un mensaje indicando si tiene 1, 2, o 3 cifras. 
Mostrar un mensaje de error si el número de cifras es mayor."""

#Lectura de datos
num=int(input("Ingresa un numero de hasta 3 cifras"))

if num<10:
    print("Tiene un digito")
else:
    if num<100:
        print("Tiene dos digitos")
    else:
        if num<1000:
            print("tiene 3 digitos")
        else:
            print("ERROR DE ENTRADA")
if num<=0:
    print("ERROR DE ENTRADA")
    
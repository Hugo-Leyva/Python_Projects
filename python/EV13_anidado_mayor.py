"""Se cargan por teclado tres numeros distintos, mostrar por pantalla el mayor de ellos"""

#Lectura de datos
num1=int(input("Primer Valor"))
num2=int(input("Segundo Valor"))
num3=int(input("Tercer Valor"))

#Condicionales
if num1>num2 and num1>num3:
    print(num1)
if num2>num1 and num2>num3:
    print(num2)
if num3>num1 and num3>num2:
    print(num3)
    
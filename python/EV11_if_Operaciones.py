"""Realizar un programa que solicite la carga por teclado de dos numeros,
si el primero es mayor al segundo imprimir su suma y resta,
en caso contrario imprimir la multiplicacion y division del primero respecto al segundo"""

#Lectura de datos
num1=int(input("Ingresa el Primer numero"))
num2=int(input("Ingresa el Segundo numero"))

suma=num1+num2
resta=num1-num2
mult=num1*num2
div=num1/num2
#Condicional
if num1>num2:
    print("la suma es: ",suma,"Y la resta es: ",resta)
else:
    print("la multiplicación es: ",mult,"y la división es: ",div)
    
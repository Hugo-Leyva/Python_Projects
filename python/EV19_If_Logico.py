"""EV19 Programa que lea por teclado 3 numero enteros distintos, y nos muestre cuál seria el mayor"""

#LECTURA DE DATOS
num1=int(input("Ingresa Primer Valor: "))
num2=int(input("Ingresa Segundo Valor: "))
num3=int(input("Ingresa Tercer Valor: "))

#IMPRESIÓN DE RESULTADO
print("El numero mayor es: ")

#CONDICIONALES
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)

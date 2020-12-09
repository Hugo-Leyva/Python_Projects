"""23.-Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10,
imprimir en pantalla la leyenda "Alguno de los números es menor a diez"."""

#LECTURA DE DATOS
num1=int(input("Ingresa el primer número"))
num2=int(input("Ingresa el segundo número"))
num3=int(input("Ingresa el tercer número"))

#CONDICIONALES
if num1<10 or num2<10 or num3<10:
    print("Alguno de los números es menos a diez")

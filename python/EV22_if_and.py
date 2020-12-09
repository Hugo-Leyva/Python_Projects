
"""22.-Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, 
imprimir en pantalla la leyenda "Todos los números son menores a diez"."""

num1=int(input("Ingresa el primer número"))
num2=int(input("Ingresa el segundo número"))
num3=int(input("Ingresa el tercer número"))

if num1<10 and num2<10 and num3<10:
    print("Todos los números son menores a diez")
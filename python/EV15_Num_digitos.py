"""Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el 
número tiene uno o dos dígitos. (Tener en cuenta que condición debe cumplirse para tener dos dígitos 
un número entero)"""

num=float(input("Ingresa un numero positivo"))

if num>10:
    print("El numero 2 digitos")
else:
    print("El numero es de 1 digito")

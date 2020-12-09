"""24.-Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero
con el segundo y a este resultado se lo multiplica por el tercero."""

num1=int(input("Ingresa el primer número"))
num2=int(input("Ingresa el segundo número"))
num3=int(input("Ingresa el tercer número"))

suma_mult=(num1+num2)*num3

if num1==num2 and num2==num3:
    print(suma_mult)


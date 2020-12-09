#Programa para encontrar el factorial de un numero proporcionado por el usuario

numero = int(input("Dime un numero"))
factorial = 1

if numero < 0:
   print("El factorial no se puede sacar en numero negativos")
elif numero == 0:
   print("El factorial de 0 es 1")
else:
   for i in range(1,numero + 1):
       factorial = factorial*i
   print("El factorial de",numero,"es",factorial)

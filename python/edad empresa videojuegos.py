#Si son menores de 4 años el precio es gratis
#si son de entre 4 y 18 años el precio es de 5 euros
#y si son mayores de 18 el precio es de 10 euros

edad=int(input("Cuantos años tienes"))

if edad<=4:
    print("El coste de entrada es gratis!")
elif edad>=4 and edad<=18:
    print("El coste de entrada es de 5 Euros")
elif edad>18:
    print("El coste de entrada es de 10 Euros")
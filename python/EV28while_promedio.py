x=1
suma=0

while x<=10:
    valor=int(input("Ingresa valor : "))
#acomulador
    suma=suma+valor

#incrementador
    x=x+1

#Aqui termina el while

promedio=suma/10

print("La suma de los 10 valores es : ")
print(suma)

print("El promedio es : ")
print(promedio)
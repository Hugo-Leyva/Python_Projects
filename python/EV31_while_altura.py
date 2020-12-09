"""Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las 
personas."""

x=1
n=int(input("Número personas"))
suma=0

while x<=n:
    altura=float(input("Ingrese la altura"))
    #acomulador
    suma=suma+altura

    #Incrementador
    x=x+1

promedio=suma/n

print("Altura promedio: ")
print(promedio)

    
    
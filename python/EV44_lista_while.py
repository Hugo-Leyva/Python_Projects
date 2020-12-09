lista=[1000,6000,400,23,130,300,60,2000]
cantidad=0
x=0

while x<len(lista):
    if lista[x]>100:
        cantidad=cantidad+1
    x=x+1

print("Las cantidades de la lista son: ")
print(lista)
print("cantidad de numeros mayores a 100 de la lista son")
print(cantidad)



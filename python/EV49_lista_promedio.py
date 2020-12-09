"""Almacenar en una lista los sueldos (valores float) de 5 operarios,
a)imprimir la lista
b)imprimir el promedio de los sueldos"""

lista=[]
suma=0

for x in range (5):
    sueldo=float(input("Ingresa 5 sueldos: "))
    lista.append(sueldo)
    suma=suma+sueldo

promedio=suma/5
print(lista)
print(promedio)


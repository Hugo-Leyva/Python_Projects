lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

#LISTA COMPLETA
print(lista)
print("___________________")

#IMPRIMIR EL PRIMER COMPONENTE
print(lista[0])
print("___________________")

#IMPRIMIR EL PRIMER COMPONENTE DE LA LISTA
print(lista[0][0])
print("___________________")

#IMPRIMIR LA LISTA DE MI PRIMER COMPONENTE
for x in range(len(lista[0])):
    print(lista[0][x])
print("___________________")

#IMPRIMIR TODOS LOS COMPONENTES DE LA LISTA
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
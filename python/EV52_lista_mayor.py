lista = []

for x in range (5):
    valor=int(input("Ingrese un valor"))
    lista.append(valor)

mayor=lista[0]
#SI EL NUMERO QUE ESTE EN LA X DE LISTA ES > A MAYOR: ENTONCES MAYOR ES IGUAL A LISTA X
#ES DECIR, QUE SI ES MAYOR AL ANTERIOR ENTONCES SE GUARDA EN MAYOR ESE VALOR.
for x in range (1,5):
    if lista [x] > mayor:
        mayor=lista[x]
print("lista: ")
print(lista)

print("Número mayor de la lista: ")
print(mayor)

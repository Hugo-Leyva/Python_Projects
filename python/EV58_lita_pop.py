
#la función pop sirve para eliminar elementos de una lista

lista=[10,20,30,40,50]

print(lista)

#nos deja impreso el 20 y el 40 porque se elimina el 10 y el 20 ahora es la posicion 0 y el 30 la posicion 1
#luego se elimina la posicion 1 osea el 30 y queda 20,40,50 luego como el 50 esta en la posicion 2 se elimina 
#y al final queda solo el 20 y el 40
lista.pop(0)
lista.pop(1)
lista.pop(2)

print(lista)

"""PROGRAMACION AVANZADA MARTES 13 DE OCTUBRE 10:00 AM"""
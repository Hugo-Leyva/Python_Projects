lista=[]
valor = int(input("Ingresa un valor (presiona 0 para finalizar): "))

#Mientras que el valor sea diferente a 0 le puedes seguir agregando valors hasta que pongas un 0
while valor!=0:
    lista.append(valor)
    valor = int(input("Ingresa valor (presiona 0 para finalizar"))
    
print ("Tamaño de la lista: ")
print(len(lista))
cantidad=0
x=1
n=int(input("Número de piezas a analizar"))

while x<=n:
    largo=float(input("Ingresa la medida de la barra de acero: "))
    if largo>=2.3 and largo<=2.5:
        #Acomulador
        cantidad=cantidad+1

        #Incrementador
    x=x+1
    
print("Cantidad de piezas aptas para venta al publico : ")
print(cantidad)


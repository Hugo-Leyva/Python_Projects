"""Se ingresa por teclado un valor entero, mostrar una leyenda que indique si
el número es positivo, negativo o nulo (es decir cero)"""

#lectura de datos
value=int(input("Ingresa un valor no decimal"))

#condicionales
if value>0:
    print("El valor es positivo")
elif value<0:
    print ("El valor es negativo")
if value==0:
    print("El valor es nulo")
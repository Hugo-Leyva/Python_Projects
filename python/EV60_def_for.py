def carga_suma():
    valor1=int(input("Ingresa el primer valor: "))
    valor2=int(input("Ingresa el segundo valor: "))
    suma=valor1+valor2
    print("La suma de los valores es: ",suma)
def separacion():
    print("*********************************")

#MANDAR LLAMAR AL PROGRAMA (FUNCIONES)

for suma in range(3):
    carga_suma()
    separacion()
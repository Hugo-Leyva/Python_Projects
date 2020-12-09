"""DESARROLLAR UN PROGRAMA CON DOS FUNCIONES LA PRIMERA QUE SOLICITE EL INGRESO DE UN ENTERO Y MUESTRE
EL CUADRADO DE DICHO VALOR"""

def calcular_cuadrado():
    print("CALCULAR CUADRADO: ")
    valor=int(input("Ingrese el entero"))
    cuadrado=valor*valor
    print("el cuadrado es: ", cuadrado)


def calcular_cubo():
    print("CALCULAR CUBO: ")
    valor1=int(input("Ingrese primer valor: "))
    cubo=valor1*valor1*valor1
    print("el cubo es: ",cubo)

#BLOQUES PRINCIPALES

calcular_cuadrado()
calcular_cubo()
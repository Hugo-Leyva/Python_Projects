"""62.- DESARROLLAR UN PROGRAMA QUE SOLICITE LA CARGA DE 3 VALORES Y MUESTRE EL MENOR 
a)DESDE EL BLOQUE PRINCIPAL DEL PROGRAMA LLAMAR 2 VECES A DICHA FUNCION SIN UTILIZAR UNA ESTRUCTURA
REPETITIVA"""

def menor_valor():
    valor1=int(input("Ingresa el primer valor"))
    valor2=int(input("Ingresa el segundo valor"))
    valor3=int(input("Ingresa el tercer valor"))
    print("Menor de los tres")
    if valor1<valor2 and valor1<valor3:
        print(valor1)
    elif valor2<valor3:
        print(valor2)
    else:
        print(valor3)

#BLOQUE PRINCIPAL

menor_valor()
menor_valor()
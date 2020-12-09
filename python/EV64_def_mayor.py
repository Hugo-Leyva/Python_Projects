def cargar_valores():
    valor1=int(input("Ingresa primer valor"))
    valor2=int(input("Ingresa segundo valor"))
    valor3=int(input("Ingresa tercer valor"))
    mostrar_mayor(valor1,valor2,valor3)

def mostrar_mayor(v1,v2,v3):
    print("el valor mayor de los 3 es: ")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)



#programa principal

cargar_valores()

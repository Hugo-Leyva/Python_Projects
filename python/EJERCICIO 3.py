numero=int(input("Bienvenido al programa, si desea comenzar a ingresar palabras a la lista ponga 1, si aun no esta listo ponga 0: "))
i=0
lista=[]
while numero > 0:
    print("digame la palabra", ": ", end="")
    palabra=input()
    lista += [palabra[0:10]]
    numero= int(input("Desea seguir agregando palabras a la lista? Si = 1, No = 0:"))
    print("La lista creada es", lista)

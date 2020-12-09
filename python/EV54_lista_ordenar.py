sueldos=[]

for x in range(5):
    valor=int(input("Ingrese sueldo"))
    sueldos.append(valor)

print("Sueldos sin ordenar")
print(sueldos)


#LO QUE HACE ES QUE LO SUSTITUYE POR EL VALOR MENOR PARA ACOMODARLOS DE MENOR A MAYOR
for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Sueldos de la lista ordenada")
print(sueldos)
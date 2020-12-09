aprobados=0
reprobados=0

for f in range(10):
    nota=int(input("Ingrese nota"))
    if nota>=7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1

print("Cantidad aprobados: ", aprobados)

print("Cantidad reprobados: ", reprobados)

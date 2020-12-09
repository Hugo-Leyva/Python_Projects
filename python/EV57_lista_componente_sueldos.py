nombres=[]
sueldos=[]
total_sueldos=[]

for x in range(3):
    nom=input("Ingrese el nombre del empleado")
    nombres.append(nom)

    su1=int(input("Ingresa el primer sueldo"))
    su2=int(input("Ingresa el segundo sueldo"))
    su3=int(input("Ingresa el tercer sueldo"))
    sueldos.append([su1,su2,su3])

#AHORA SE VA A SUMAR LOS 3 SUELDOS PARA TENER EL TOTAL DE SUELDOS
for x in range(3):
    total=sueldos[x][0]+sueldos[x][1]+sueldos[x][2]
    total_sueldos.append(total)
    
for x in range(3):
    print(nombres[x],total_sueldos[x])
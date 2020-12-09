"""51 una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 en la mañana 
y 4 por la tarde)
a)confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
b)imprimir las dos listas de sueldos"""

sueldos_mañana=[]
print("Sueldos Mañana")

for x in range(4):
    valor=float(input("Ingrese sueldo:"))
    sueldos_mañana.append(valor)

sueldos_tarde=[]
print("Sueldos Tarde")

for x in range(4):
    valor=float(input("Ingrese sueldo:"))
    sueldos_tarde.append(valor)

print("Turno mañana")
print(sueldos_mañana)
print("Turno tarde")
print(sueldos_tarde)
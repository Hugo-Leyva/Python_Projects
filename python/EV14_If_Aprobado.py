"""Se ingresan tres notas de un alumno,
si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"."""

#Lectura de datos
not1=int(input("Ingrese primer calificacion: "))
not2=int(input("Ingrese segunda calificación: "))
not3=int(input("Ingrese tercera calificación: "))

#operaciones
prom=(not1+not2+not3)/3

if prom>=7:
    print("Promocionado")



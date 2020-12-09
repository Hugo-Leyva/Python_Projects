"""Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio
e imprima alguno de estos mensajes:
si el promedio es >= 7 mostrar "aprobado".
si el promedio es >=4 y <7 mostrar "regular".
si el promedio es <4 imprimir "reprobado"."""

#Lectura de datos
cal1=int(input("Ingrese primer calificación: "))
cal2=int(input("Ingrese segunda calificación: "))
cal3=int(input("Ingrese tercera calificación: "))

#operaciones
prom=(cal1+cal2+cal3)/3

#condicionales
if prom>=7:
    print("Aprobado")
else:
    if prom>=4:
        print("Regular")
    else:
        print("Reprobado")
"""30.-Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas
 mayores o iguales a 7 y cuántos menores."""

x=1
conta1=0
conta2=0
while x<=10:
    nota=int(input("Ingrese nota: "))
    if nota>=7:
        conta1=conta1+1
    else:
        conta2=conta2+1
    x=x+1
print("Cantidad de alumnos con notas mayores o iguales a 7: ",conta1)
print("Cantidad de alumnos con notas menores a 7: ",conta2)

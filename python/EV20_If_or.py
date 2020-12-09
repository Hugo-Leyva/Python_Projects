"""20.- Se carga una fecha (Día, Mes y Año) por teclado. Mostrar un mensaje si
corresponde al primer trimestre del año (Enero, Febrero o Marzo) Cargar por teclado
el valor numérico del Día, Mes y Año.
Ejemplo: dia:10 mes:2 año:2018"""

dia=int(input("Ingresa el día: "))
mes=int(input("Ingresa el mes: "))
año=int(input("Ingresa el año: "))

if mes==1 or mes==2 or mes==3:
    print("Corresponde al 1er trimestre")
elif mes==4 or mes==5 or mes==6:
    print("Corresponde al 2do trimestre")
elif mes==7 or mes==8 or mes==9:
    print("Corresponde al 3er trimestre")
elif mes==10 or mes==11 or mes==12:
    print("Corresponde al 4to trimestre")
else:
    print("No corresponde a ninguno")

if dia>31:
    print("Un mes no puede tener mas de 31 días ")

"""Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información:
cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente.
Se pide confeccionar un programa que ingrese los dos datos por teclado e informe
el nivel del mismo según el porcentaje de respuestas 
correctas que ha obtenido, y sabiendo que:
    Nivel máximo:    Porcentaje>=90%.
    Nivel medio:    Porcentaje>=75% y <90%.
    Nivel regular:    Porcentaje>=50% y <75%.
    Fuera de nivel:    Porcentaje<50%."""

#Lectura de datos
tot_preguntas=int(input("Ingresa la cantidad de preguntas que realizaste: "))
tot_correctas=int(input("Ingresa la cantidad de aciertos: "))

#Operaciones
porc=tot_correctas*100/tot_preguntas
if porc>=90:
    print("Nivel Máximo")
else:
    if porc>=75 and porc<90:
        print("Nivel Medio")
    else:
        if porc>=50 and porc<75:
            print("Nivel Regular")
        else:
            if porc<50:
                print("Fuera De Nivel")

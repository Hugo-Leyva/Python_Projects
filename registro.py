import os
import csv
import re
import datetime
import json
from clases import Participante

Limpiar = lambda: os.system('cls')
ListaRegistros = []

#Elías Armando Cervantes Piña colabró estructurando el caso y ayudando con la identación
#CARGAR DATOS 
persona1 = Participante("ISRAEL","robertisrael@gmail.com","1980-11-25",'2020-09-22 19:31:34.133146')
persona2 = Participante("ROBERT","marcosifuentes@icloud.com","2001-01-22",'2020-09-22 29:16:63.881023')
persona3 = Participante("EMILIANO ISAAC","antoniojesus@edu.com","2002-09-11",'2020-09-21 19:50:29.231435')
ListaRegistros.append(persona1)
ListaRegistros.append(persona2)
ListaRegistros.append(persona3)

#Busqueda correo
#Marco Antonio Sifuentes estuvo con Elías ayudando a identar el codigo de manera correcta
def BuscaCorreo(valor):
    i=0
    resultado=False
    for i in range(0,len(ListaRegistros)):
        if (ListaRegistros[i].correo==valor):
            resultado=True
            break
    return resultado


#Busqueda_Indice
#Pedro Alejandro Delgado Rodriguez ayudó con el menu y su estructura e identación

def BuscaIndice(valor):
    i=0
    for i in range(0,len(ListaRegistros)):
        if (ListaRegistros[i].correo==valor):
            resultado=i
            break
    return resultado

#Jimena Reynosa Garza ayudo a que el codigo corriera de manera correcta y solucionar los errores
def PrintParticipante(valor):
    print(ListaRegistros[valor].nombre, ListaRegistros[valor].correo, ListaRegistros[valor].nacimiento, ListaRegistros[valor].momento)


#Jimena Reynosa Garza 

def TabulaLista():
    print("{:>10} {:>20} {:>35} {:>20}".format( 
        "NOMBRE",
        "CORREO",
        "NACIMIENTO",
        "MOMENTO"))
    print("{:>10} {:>20} {:>30} {:>25}".format( 
        "-----------------",
        "-----------------",
        "-----------------",
        "-----------------"))
    for elemento in ListaRegistros:
        print("{:>10} {:>35} {:>20} {:>32}".format( 
        elemento.nombre, elemento.correo, elemento.nacimiento, elemento.momento))


"""Adrian Esau Reyes Ibarra y los demas integrantes también le ayudaron a Elías en terminar el archivo PDF
con todos las instrucciones pedidas"""

#MENU
def main():
    while True:
        Limpiar()
        print("Bienvenido Registrate para la rifa")
        print("")
        print("[1] Cargar informacion de CSV")
        print("[2] Registro de participantes")
        print("[3] Busqueda de participantes")
        print("[4] Modificacion de participantes") 
        print("[5] Eliminación de participantes") 
        print("[6] Visualiza participantes")
        print("[7] Actualizar info CSV")
        print("[8] Serializar informacion a JSON")
        print("[X] Salir")
        pregunta = input("¿Que opcion deseas? \n")
        
        if pregunta == '1':
            ruta_archivo=os.path.abspath(os.getcwd())
            archivo_respaldo=ruta_archivo+"\\registros.bak"
            archivo_normal=ruta_archivo+"\\registros.csv"
            
            if os.path.exists(archivo_normal):
                print('')
                print("Archivo csv encontrado en",archivo_normal)
                with open('registros.csv', newline='') as archivo_csv:
                    lector_csv = csv.reader(archivo_csv, delimiter='|')
                    DatosCSV= []
                    for e in lector_csv:                                                
                        if len(e[0]) >40:
                            print("No puede exceder los 40 caracteres en el nombre. Registro invalido. \n")
                            print("Menu Principal. \n")
                            main()
                        elif len(e[0]) <5:
                            print("Minimo de caracteres permitidos (5). Registro invalido. \n")
                            print("Menu Principal. \n")
                            main()
                        elif (re.search(r"(/^[a-zA-Z]+(\s*[a-zA-Z]*)*[a-zA-Z]+$/)", e[0])):
                            print("No se permite Ñ ni Acentos. Registro invalido. \n")
                            print("Menu Principal. \n")
                            main()
                        else:
                            minombre = e[0].upper()
                            
                            
                        if (re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", e[1])):
                            if BuscaCorreo(e[1]) == False:
                                micorreo = e[1]
                            else:
                                print("Correo ya esta en uso. Registro Invalido. \n")
                                print("Menu Principal \n")
                                main()
                            
                        else:
                            print("invalido. \n")
                            print("Menu Principal \n")
                            main()
                        
                        if (re.search(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", e[2])):
                            mifecha = e[2]
                            
                            mimomento = str(datetime.datetime.now())
                            registrofinal = Participante(minombre,micorreo,mifecha,mimomento)
                            ListaRegistros.append(registrofinal)
                            print('')
                            print("El registro ha sido completao correctamente. \n")
                            print("Menu Principal. \n")
                        
                        else:
                            print("La fecha de nacimiento debe estar en el siguiente formato YYYY-MM-DD. Registro invalido. \n")
                            print("Menu Principal \n")
                            main()
                            
                                              
                        

                    
                       
            
            else:
                print('')
                print("No tiene un archivo csv, ¿Desea crear uno?")
                creararchivo = input("[1] Si \n[2] No \n")
                
                if creararchivo == '1':
                    while True:
                        nombre = input("Ingresar nombre: \n")               
                        if len(nombre)>40:
                            print("Su nombre no puede tener mas de 40 caracteres. \n")
                        elif len(nombre)<5:
                            print("Su nombre debe tener minimo 5 caracteres. \n")
                        elif (re.search(r"(/^[a-zA-Z]+(\s*[a-zA-Z]*)*[a-zA-Z]+$/)", nombre)):
                            print("Su nombre no puede llevar acentos ni ñ. \n")
                        else:
                            minombre = nombre.upper()
                            break
                    
                    while True:
                        correo = input("Ingresar correo: \n")
                        if (re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", correo)):
                            if BuscaCorreo(correo) == False:
                                micorreo = correo
                                break
                            else:
                                print("Correo en uso. \n")
                        else:
                            print("Ingrese un correo valido. \n")
                    
                    while True:
                        fecha = input("Ingresar fecha de nacimiento: \n")
                        if (re.search(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", fecha)):
                            mifecha = fecha
                            break
                        else:
                            print("Su fecha debe estar en el siguiente formato YYYY-MM-DD. \n")
                    
                    
                    
                    f = open(archivo_normal,"w+")
                    registrofinal = str(minombre) + '|' + str(micorreo) + '|' + str(mifecha) + '|'
                    f.write(registrofinal)
                    f.close()
                    print('')
                    print("Archivo csv creado en",archivo_normal)
                    print("Devuelta al Menu Principal.")
                    print("")
                else:
                    print("Devuelta al Menu Principal.")
                    print("")
        
        
        elif pregunta == '2':
            while True:
                correo = input("Ingrese su correo: \n[X] Volver al Menu Principal \n")
                if correo == 'x' or correo == 'X':
                    print('')
                    print("Devuelta al Menu Principal. \n")
                    main()
                
                else:                    
                    if (re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", correo)):
                        if BuscaCorreo(correo) == False:
                            micorreo = correo
                            break
                        else:
                            print("Este correo ya esta en uso. \n")
                            volver= input("¿Volver a Menu Principal? \n[1] Volver \n[2] No Volver \n")
                            if volver == '1':
                                main()
                    else:
                        print("Ingrese un correo valido. \n")
                    
            while True:
                print('')
                nombre = input("Ingrese su nombre: \n")               
                if len(nombre)>40:
                    print("Su nombre no puede exceder 40 caracteres. \n")
                elif len(nombre)<5:
                    print("Su nombre debe tener al menos 5 caracteres. \n")
                elif (re.search(r"(/^[a-zA-Z]+(\s*[a-zA-Z]*)*[a-zA-Z]+$/)", nombre)):
                    print("Su nombre no puede llevar acentos ni ñ. \n")
                else:
                    minombre = nombre.upper()
                    break
                    
                    
            while True:
                print('')
                fecha = input("Ingrese su fecha de nacimiento: \n")
                if (re.search(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", fecha)):
                    mifecha = fecha
                    break
                else:
                    print("Su fecha debe estar en formato YYYY-MM-DD. \n")
                    
            mimomento = str(datetime.datetime.now())
            registrofinal = Participante(minombre,micorreo,mifecha,mimomento)
            ListaRegistros.append(registrofinal)
            print('')
            print("Se ha registrado correctamente. \n")
            print("Devuelta al Menu Principal. \n")
            
        elif pregunta == '3':
            while True:
                correo = input("Ingrese el correo del Participante: \n[X] Volver al Menu Principal \n")
                if correo == 'x' or correo == 'X':
                    print('')
                    print("Devuelta al Menu Principal. \n")
                    main()
                
                else:                    
                    if (re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", correo)):
                        if BuscaCorreo(correo) == True:
                            print('')
                            print("Correo coincide con el Participante " + str(BuscaIndice(correo)) + ': \n')
                            PrintParticipante(BuscaIndice(correo))
                            print('')
                            print("Devuelta al Menu Principal. \n")
                            main()
                            
                        else:
                            print("Este correo no esta en uso. \n")
                            volver= input("¿Volver a Menu Principal? \n[1] Volver \n[2] No Volver \n")
                            if volver == '1':
                                main()
                    else:
                        print("Ingrese un correo valido. \n")
                        
         
        elif pregunta == '4':
            while True:
                correo = input("Ingrese su correo: \n[X] Volver al Menu Principal \n")
                if correo == 'x' or correo == 'X':
                    print('')
                    print("Devuelta al Menu Principal. \n")
                    main()
                
                else:                    
                    if (re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", correo)):
                        if BuscaCorreo(correo) == True:
                            print('')
                            print("Correo coincide con el Participante " + str(BuscaIndice(correo)) + ': \n')
                            PrintParticipante(BuscaIndice(correo))
                            print("Introduzca los nuevos valores. \n")
                            while True:
                                print('')
                                nombre = input("Nombre: \n")               
                                if len(nombre)>40:
                                    print("Su nombre no puede exceder 40 caracteres. \n")
                                elif len(nombre)<5:
                                    print("Su nombre debe tener al menos 5 caracteres. \n")
                                elif (re.search(r"(/^[a-zA-Z]+(\s*[a-zA-Z]*)*[a-zA-Z]+$/)", nombre)):
                                    print("Su nombre no puede llevar acentos ni ñ. \n")
                                else:
                                    minombre = nombre.upper()
                                    break
                            
                            while True:
                                print('')
                                fecha = input("Fecha de nacimiento: \n")
                                if (re.search(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", fecha)):
                                    mifecha = fecha
                                    break
                                else:
                                    print("Su fecha debe estar en formato YYYY-MM-DD. \n")
                            
                            ListaRegistros[BuscaIndice(correo)].nombre = minombre
                            ListaRegistros[BuscaIndice(correo)].nacimiento = mifecha
                            print('')
                            print("Se ha actualizado su registro correctamente. \n")
                            PrintParticipante(BuscaIndice(correo))
                            print('')
                            print("Devuelta al Menu Principal. \n")
                            main()
                                  
                        else:
                            print("Este correo no esta registrado. \n")
                            volver= input("¿Volver a Menu Principal? \n[1] Volver \n[2] No Volver \n")
                            if volver == '1':
                                main()
                    else:
                        print("Ingrese un correo valido. \n")
                        
             
        elif pregunta == '5':
            while True:
                correo = input("Ingrese el correo del Participante: \n[X] Volver al Menu Principal \n")
                if correo == 'x' or correo == 'X':
                    print('')
                    print("Devuelta al Menu Principal. \n")
                    main()
                
                else:                    
                    if (re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", correo)):
                        if BuscaCorreo(correo) == True:
                            print('')
                            print("Correo coincide con el Participante " + str(BuscaIndice(correo)) + ': \n')
                            PrintParticipante(BuscaIndice(correo))
                            print('')                            
                            eliminar = input("¿Desea eliminar este registro? \n[1] Eliminar \n[2] No Eliminar \n")
                            if eliminar == '1':
                                ListaRegistros.pop(BuscaIndice(correo))
                                print('')
                                print("Su registro se ha eliminado correctamente. \n")
                                print("Devuelta al Menu Principal. \n")                            
                                main()
                                
                            else:
                                print('')
                                print("No se elimino registro. \n")
                                print("Devuelta al Menu Principal. \n")
                                main()
                                
                            
                            
                        else:
                            print("Este correo no esta en uso. \n")
                            volver= input("¿Volver a Menu Principal? \n[1] Volver \n[2] No Volver \n")
                            if volver == '1':
                                main()
                    else:
                        print("Ingrese un correo valido. \n")         
            
                        
                        
        elif pregunta == '6':
            while True:
                TabulaLista()
                print('')
                volver = input("¿Volver a Menu Principal? \n[1] Volver \n[2] No Volver \n")
                if volver == '1':
                    break
            
                        
        elif pregunta == '7':
            ruta = os.path.abspath(os.getcwd())
            archivo_normal=ruta+"\\registros.csv"
            archivo_respaldo=ruta+"\\registros.bak"
            if os.path.exists(archivo_normal):
                print('')
                print("Archivo csv encontrado en",archivo_normal)
                if os.path.exists(archivo_respaldo):
                    os.remove(archivo_respaldo)                           
                    os.rename(archivo_normal,archivo_respaldo)                    
                while True:
                    print('')
                    print("Introduzca sus datos. \n")
                    nombre = input("Ingrese su nombre: \n")               
                    if len(nombre)>40:
                        print("Su nombre no puede exceder 40 caracteres. \n")
                    elif len(nombre)<5:
                        print("Su nombre debe tener al menos 5 caracteres. \n")
                    elif (re.search(r"(/^[a-zA-Z]+(\s*[a-zA-Z]*)*[a-zA-Z]+$/)", nombre)):
                        print("Su nombre no puede llevar acentos ni ñ. \n")
                    else:
                        minombre = nombre.upper()
                        break
                    
                while True:
                    correo = input("Ingrese su correo: \n")
                    if (re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", correo)):
                        if BuscaCorreo(correo) == False:
                            micorreo = correo
                            break
                        else:
                            print("Este correo ya está en uso. \n")
                    else:
                        print("Ingrese un correo valido. \n")
                    
                while True:
                    fecha = input("Ingrese su fecha de nacimiento: \n")
                    if (re.search(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", fecha)):
                        mifecha = fecha
                        break
                    else:
                        print("Su fecha debe estar en formato YYYY-MM-DD. \n")
                    
                    
                    
                f = open(archivo_normal,"w+")
                registrofinal = str(minombre) + '|' + str(micorreo) + '|' + str(mifecha) + '|'
                f.write(registrofinal)
                f.close()
                print('')
                print("Archivo csv actualizado en",archivo_normal)
                print("Devuelta al Menu Principal. \n")                   
                            
                    
                       
            
            else:
                print('')
                print("Su equipo no tiene un archivo csv. \n")
                print("Devuelta al menu Principal. \n")
                
                        
        elif pregunta == '8':
            json_data = json.dumps(ListaRegistros, default=lambda o: o.__dict__, indent=4)            
            while True:
                print(json_data)
                print('')
                volver = input("¿Volver a Menu Principal? \n[1] Volver \n[2] No Volver \n")
                if volver == '1':
                    break
        
        
        elif pregunta=='x' or pregunta=='X':
            print('')
            print("Vuelva pronto~ \n")
            break
    
            
main()

    


    
   


    
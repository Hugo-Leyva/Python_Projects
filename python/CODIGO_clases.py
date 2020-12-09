#PRODUCTO INTEGRADOR DE APRENDIZAJE
import tkinter as tk
from tkinter import ttk  #otra libreria de diseño de formularios
from tkinter import messagebox as mb  #importamos otra libreria de mensajes
from tkinter import scrolledtext as st
import EV81_Crude

class Participante:
    def __init__(self):            # INIT CONTENEDOR DE MI VENTANA CON LA INFORMACION QUE VOY A UTILIZAR
        self.articulo1=EV81_Crude.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("JUGADORES")
        self.cuaderno1 = ttk.Notebook(self.ventana1)   #NOTEBOOK ES PARA CAMBIAR LAS PESTAÑAS DE LA VENTANA CARGA DE ART Y LIST COMPLETO
        self.cargar_articulos() #mandar llamar al def de alta que esta en la ev 80
        #self.consulta_por_nombre() #mandar llamar al de consulta
        self.listado_completo() #mandar llamar al de recuperar_todos
        self.borrado()  #mandar llamar el de borrado
        #self.modificar() #mandar llamar el de modificacion
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)   #UBICACION HORIZONTAL Y VERTICAL PADX Y PADY
        self.ventana1.mainloop()




    def cargar_articulos(self):
        #pestaña
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de jugador")
        
        #label articulo
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="JUGADORES")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        #label descripcion
        self.label1=ttk.Label(self.labelframe1, text="Nombre: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        #caja texto
        self.nombre=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.nombre)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)

        #label correo
        self.label2=ttk.Label(self.labelframe1, text="Correo Electronico")
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        #caja texto correo
        self.telefono=tk.StringVar()   #El stringvar es para que la variable que le estoy asignando la tome como string
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.telefono)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        #label fecha
        self.label3=ttk.Label(self.labelframe1, text="Fecha Nacimiento")
        self.label3.grid(column=0, row=2, padx=4, pady=4)

        #caja texto fecha
        self.telefono=tk.StringVar()   
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.telefono)
        self.entryprecio.grid(column=1, row=2, padx=5, pady=5)

        #boton confirmar
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=3, padx=6, pady=6)

        #Referencia a base de datos tabla articulos
    def agregar(self):
        datos=(self.nombre.get(), self.telefono.get())  #GET quiere decir que tome los datos de mi label y se los da a la variable decripcion
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.nombre.set("")
        self.telefono.set("")





    def borrado(self):
        #Pestaña
        self.pagina4 = ttk.Frame(self.cuaderno1)      #FRAME son las pestañas
        self.cuaderno1.add(self.pagina4, text="Borrado de Jugador")
        
        #label articulo
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Laboratorio")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        #label codigo
        self.label1=ttk.Label(self.labelframe4, text="codigo: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        
        #caja texto codigo
        self.codigoborrar=tk.StringVar()
        self.entryborrar=ttk.Entry(self.labelframe4, textvariable=self.codigoborrar)
        self.entryborrar.grid(column=1, row=0, padx=4, pady=4)

        #boton confirmar
        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

        #Referencia a base de datos tabla articulos
    def borrar(self):
        datos=(self.codigoborrar.get(),)
        cantidad=self.articulo1.baja(datos)
        if cantidad==1:                     #Si existe un articulo con ese codigo que diga eso y si no lo otro
            mb.showinfo("Informacion", "Se borro el proveedor con dicho nombre")
        else:
            mb.showinfo("Informacion", "No existe un proveedor con dicho nombre")


    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Fecha Registro")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="REGISTRO_CARGA")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="MOSTRAR", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END,
                                              "\nHORA_REGISTRO:"+fila[1]+"\n\n")
                                              






    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar Jugador")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="JUGADOR")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe5, text="Codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe5, text="nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        
        self.descripcionmod=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe5, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe5, text="correo:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        self.fechamod=tk.StringVar()
        self.entryfecha=ttk.Entry(self.labelframe5, textvariable=self.descripcionmod)
        self.entryfecha.grid(column=1, row=2, padx=5, pady=5)
        self.label4=ttk.Label(self.labelframe5, text="Fecha de Nacimiento:")        
        self.label4.grid(column=0, row=3, padx=5, pady=5)

        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos=(self.descripcionmod.get(), self.fechamod.get(), self.codigomod.get())
        cantidad=self.articulo1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")



    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcionmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
            self.fechamod.set(respuesta[0][2])

        else:
            self.descripcionmod.set('')
            self.preciomod.set('')
            self.fechamod.set('')

            mb.showinfo("Información", "No existe un laboratorio con dicho código")





    def consulta_por_nombre(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por codigo")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="JUGADORES")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="correo:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.nombre.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.nombre.set('')
            mb.showinfo("Información", "No existe un Jugador con dicho código")
    
aplicacion1=Participante()
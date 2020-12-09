import tkinter as tk
from tkinter import ttk  #otra libreria de diseño de formularios
from tkinter import messagebox as mb  #importamos otra libreria de mensajes
from tkinter import scrolledtext as st
import EV80_VS_Code_SQLite_articulos

class FormularioArticulos:
    def __init__(self):            # INIT CONTENEDOR DE MI VENTANA CON LA INFORMACION QUE VOY A UTILIZAR
        self.articulo1=EV80_VS_Code_SQLite_articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento Articulos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)   #NOTEBOOK ES PARA CAMBIAR LAS PESTAÑAS DE LA VENTANA CARGA DE ART Y LIST COMPLETO
        self.cargar_articulos() #mandar llamar al def de alta que esta en la ev 80
        #self.consulta_por_codigo() #mandar llamar al de consulta
        #self.listado_completo() #mandar llamar al de recuperar_todos
        #self.borrado()  #mandar llamar el de borrado
        #self.modificar() #mandar llamar el de modificacion
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)   #UBICACION HORIZONTAL Y VERTICAL PADX Y PADY
        self.ventana1.mainloop()

    def cargar_articulos(self):
        #pestaña
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga Jugador")
        
        #label articulo
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Jugador")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        #label descripcion
        self.label1=ttk.Label(self.labelframe1, text="Nombre: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        #caja texto
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)

        #label precio
        self.label2=ttk.Label(self.labelframe1, text="Fecha Nacimiento")
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        #caja texto precio
        self.preciocarga=tk.StringVar()   #El stringvar es para que la variable que le estoy asignando la tome como string
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        #label correo
        self.label3=ttk.Label(self.labelframe1, text="Correo Electronico")
        self.label3.grid(column=0, row=2, padx=5, pady=5)

        #caja texto correo
        self.correo=tk.StringVar()  
        self.entrycorreo=ttk.Entry(self.labelframe1, textvariable=self.correo)
        self.entrycorreo.grid(column=1, row=2, padx=5, pady=5)


        #boton confirmar
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=4, padx=7, pady=7)

        #Referencia a base de datos tabla articulos
    def agregar(self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())  #GET quiere decir que tome los datos de mi label y se los da a la variable decripcion
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados 6:18")
        self.descripcioncarga.set("")
        self.preciocarga.set("")


aplicacion1=FormularioArticulos()
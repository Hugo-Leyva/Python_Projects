import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import EV80_VS_Code_SQLite_articulos

class FormularioArticulos:
    def __init__(self):
        self.articulo1=EV80_VS_Code_SQLite_articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Lista de Medicamento")
        self.cuaderno1= ttk.Notebook(self.ventana1)
        self.cargar_articulos()
        #self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        #self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()
    
    def cargar_articulos(self):
        #pestaña
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de Medicamento")
        
        #laber articulo
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Medicamento")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        #label descripcion
        self.label1=ttk.Label(self.labelframe1, text="Descripcion:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
      
       #caja texto descripcion
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
      
       #label precio
        self.label2=ttk.Label(self.labelframe1, text="Precio: ")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        
        #caja text precio
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        #Boton confirmar
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)
    
    def agregar(self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Informacion", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")
    
    def borrado(self):
        #pestaña
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de Medicamentos")

        #laber articulo
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Medicamento")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        #label Codigo
        self.label1=ttk.Label(self.labelframe1, text="Codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

         #caja texto borrar
        self.codigoborrar=tk.StringVar()
        self.entryborrar=ttk.Entry(self.labelframe1, textvariable=self.codigoborrar)
        self.entryborrar.grid(column=1, row=0, padx=4, pady=4)

        #Boton Borrar
        self.boton1=ttk.Button(self.labelframe1, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def borrar(self):
       datos=(self.codigoborrar.get(),)
       cantidad=self.articulo1.baja(datos)
       if cantidad==1:
           mb.showinfo("Informacion", "Se borro el medicamento con dicho precio")
       else:
           mb.showinfo("Informacion", "No existe un medicamento con dicho precio")

    
    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado Completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Medicamento")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=0)
        self.boton1=ttk.Button(self.labelframe3, text="Listado Completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)
    
    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1,0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "Medicamento:"+str(fila[0])+
                                            "\ndescripcion:"+fila[1]+
                                            "\nprecio:"+str(fila[2])+"\n\n")  
    
    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por medicamento")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Medicamento")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
            
    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un medicamento con dicho medicamento")   
                

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar medicamento")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Medicamento")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe5, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe5, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcionmod=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe5, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe5, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos=(self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad=self.articulo1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el medicamento")
        else:
            mb.showinfo("Información", "No existe un medicamento con dicho precio")

    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcionmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
        else:
            self.descripcionmod.set('')
            self.preciomod.set('')
            mb.showinfo("Información", "No existe un medicamento con dicho precio")
                  


aplicacion1=FormularioArticulos()
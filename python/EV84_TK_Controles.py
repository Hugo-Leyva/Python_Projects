import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        #Formulario/Ventana
        self.ventana1=tk.Tk()

        #Etiqueta/label
        self.label1=tk.Label(self.ventana1, text="HOla y saludos")
        self.label1.grid(column=0, row=0)

        #Caja de texto/Entry
        self.entry1=tk.Entry(self.ventana1, width=10)
        self.entry1.grid(column=0, row=1)

        #radiobutton
        self.radio1=tk.Radiobutton(self.ventana1, text="Seleccion")
        self.radio1.grid(column=0, row=2)

        #checkbutton
        self.check1=tk.Checkbutton(self.ventana1, text="Python")
        self.check1.grid(column=0, row=3)

        #listbox
        self.list1=tk.Listbox(self.ventana1)
        self.list1.grid(column=0, row=4)
        self.list1.insert(0,"galletas")
        self.list1.insert(1,"pan")

        #combobox
        dias=("lunes", "martes", "miercoles")
        self.combobox1=ttk.Combobox(self.ventana1, width=10, values=dias)
        self.combobox1.current(0)
        self.combobox1.grid(column=0, row=5)

        #menubar
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1)
        opciones1.add_command(label="Abrir")
        opciones1.add_command(label="Guardar")
        opciones1.add_command(label="Salir")
        menubar1.add_cascade(label="Archivo", menu=opciones1)

        self.ventana1.mainloop()

aplicacion1=Aplicacion()
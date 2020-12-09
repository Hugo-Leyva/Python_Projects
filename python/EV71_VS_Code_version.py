import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Version Sistema")           #TITULO
        self.label1=tk.Label(self.ventana1, text="Sistema de Ventas")   #DECLARACION ETIQUETA 1
        self.label1.grid(column=0, row=0)               #POSICION DE LA ETIQUETA 1
        self.label2=tk.Label(self.ventana1, text="2020")          #DECLARACION DE LA ETIQUEDA 2
        self.label2.grid(column=0, row=1)               #POSICION DE LABEL2
        self.boton1=tk.Button(self.ventana1, text="Salir", command=self.salir)          #PARA SALIR
        self.boton1.grid(column=0, row=2)                    #POSICION
        self.ventana1.resizable(False, False)        #PARA QUE NO ME PERMITA CAMBIAR DE TAMAÑO LA VENTANA

        self.ventana1.mainloop()

    def salir(self):
        sys.exit(0)


aplicacion1=Aplicacion()

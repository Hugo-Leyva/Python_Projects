import tkinter as tk

class Aplicacion:
    def __init__(self):    #porque vamos a trabajar en esta misma parte del codigo
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="green")
        self.canvas1.grid(column=0, row=0)
        self.ventana1.mainloop()

aplicacion1=Aplicacion()
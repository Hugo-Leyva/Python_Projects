"""72.-disponer dos objetos de la clase Button con las etiquetas: "hombre" y "mujer", al presionarse
mostrar en la barra de titulos de la ventana la etiqueta del boton presionado"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba")
        self.boton1=tk.Button(self.ventana1, text="Varón", command=self.presionvaron)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana1, text="Mujer", command=self.presionmujer)
        self.boton2.grid(column=1, row=0)
        self.ventana1.mainloop()

    def presionvaron(self):
        self.ventana1.title('Varón')

    def presionmujer(self):
        self.ventana1.title('Mujer')


aplicacion1=Aplicacion()

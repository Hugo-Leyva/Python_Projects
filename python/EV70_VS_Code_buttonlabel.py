import tkinter as tk
 
class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()              #VENTANA 
        self.ventana1.title("Objetos button y lable")           #TITULO DE LA VENTANA
        self.label1=tk.Label(self.ventana1, text=self.valor)   #DECLARACION DE LA ETIQUETA
        self.label1.grid(column=0,row=0)               #POSICION DE LA ETIQUETA
        self.label1.configure(foreground="red")          #COLOR DEL TEXTO
 
        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)
 
        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)
 
        self.ventana1.mainloop()

    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)
 
    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)        
 
aplicacion1=Aplicacion()

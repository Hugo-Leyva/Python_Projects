import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=800, height=600, background="white")
        self.canvas1.grid(column=0, row=0)
        
        archi1=tk.PhotoImage(file="logo.png")
        self.canvas1.create_image(20, 100, image=archi1, anchor="nw")

        self.ventana1.mainloop()

aplicacion1=Aplicacion()


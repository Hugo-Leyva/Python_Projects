class Humano:
    def __init__(self,edad):
        self.edad = edad
        print ("soy un nuevo objeto")

    def hablar(self,mensaje):
        print (mensaje)
        print (self.edad)

Hugo = Humano(18)
Devany = Humano(18)

Hugo.hablar("Hola conejita")
Devany.hablar("Hola conejito")
class robot:
    def introduce_self(self):
        print ("My name is " + self.name + " " + self.color + " " + self.weight)
        
r1 = robot()
r1.name = "Hugo"
r1.color = "Rojo"
r1.weight = "49"

r1.introduce_self()

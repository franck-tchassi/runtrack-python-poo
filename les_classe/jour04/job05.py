
class Forme:
    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    def aire(self):
        pi =3.14
        return pi * self.radius**2
    
cercle =Cercle(5)
print(cercle.aire())
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def périmètre(self):
        perimetre = (self.__longueur + self.__largeur) /2
        return perimetre
    
    def surface(self):
        surf = self.__longueur * self.__largeur
        return surf
    
    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur


    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur



class Parallélépipède(Rectangle):
    def __init(self, longueur, largeur, hauteur):
        Rectangle.__init__(self)
        self.hauteur = hauteur
    
    def volume(self):
        vol = (self.__longueur * self.__largeur * self.hauteur)
        return vol
    

rectangle = Rectangle(10, 5)
#Parallé = Parallélépipède(4)

#calculer le périmètre et la surface
print(rectangle.périmètre())
print(rectangle.surface())
print(rectangle.get_largeur())
print(rectangle.get_longueur())

#modifier la longueur et la largeur
rectangle.set_longueur(20)
rectangle.set_largeur(10)
print(rectangle.get_largeur())
print(rectangle.get_longueur())













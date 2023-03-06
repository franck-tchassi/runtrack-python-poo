class Rectangle:
    def __init__(self, Longueur, Largeur):
        self.__Longueur = Longueur
        self.__Largeur = Largeur

    def get_Longueur(self):
        return self.__Longueur
    def set_Longueur(self, Longueur):
        self.__Longueur = Longueur

    def get_Largeur(self):
        return self.__Largeur
    def set_Largeur(self, Largeur):
        self.__Largeur = Largeur

rectangle_1 = Rectangle(10, 5)

#modifier les valeur de la longueur et la largeur
rectangle_1.set_Longueur(2)
rectangle_1.set_Largeur(20)

#afficher les valeurs modifiés
longueur = rectangle_1.get_Longueur()
largeur = rectangle_1.get_Largeur()
print (f'la longueur apres modification est {longueur}')
print(f'la largeur apres modification est {largeur} ')


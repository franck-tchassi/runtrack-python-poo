class Livre:
    def __init__(self, tittle, autor, pageNumber):
        self.__tittle = tittle
        self.__autor = autor
        self.__pageNumber = pageNumber
        self.__disponible = True

    def vérification(self):
        return self.__disponible

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("livre disponible")       
        else:
            print("le livre à été empreinté")

    def rendre(self): 
        if not self.__disponible:
            self.__disponible = True
            print("le livre à été rendu")
        else:
            print("le livre n'a pas encore été empreinté")
        

book1 = Livre("le diable arrive", "satan", 99)
book1.emprunter()
book1.rendre()
print(book1.vérification())
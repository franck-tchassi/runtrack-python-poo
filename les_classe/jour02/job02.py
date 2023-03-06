class Livre:
    def __init__(self, tittle, autor, pageNumber):
        self.__tittle = tittle
        self.__autor = autor
        self.__pageNumber = pageNumber

    def get_tittle(self):
        return self.__tittle
    def set_tittle(self, tittle):
        self.__tittle = tittle

    def get_autor(self):
        return self.__autor
    def set_autor(self, autor):
        self.__autor = autor

    def get_pageNumber(self):
        return self.__pageNumber
    def set_pageNumber(self, pageNumber):
        if pageNumber > 0 :
            self.__autor = pageNumber
        else:
            print("erreur le nombre de page est inférieur ou égal à 0")


book1 = Livre("le diable arrive", "satan", 99)




#afficher les valeurs de l'objet créer avec get
print(f'le titre du livre est {book1.get_tittle()}')
print(f"l'auteur du livre est {book1.get_autor()}")
print(f'le nombre de pages est {book1.get_pageNumber()}')
print('\n')
# modifiér les valeurs de l'objets créer avec set
book1.set_tittle("la bataille du peuple")
book1.set_autor("Emile zola")
book1.set_pageNumber(0)
print(f'le titre du livre apres modification est {book1.get_tittle()}')
print(f"l'auteur du livre apres modification est {book1.get_autor()}")
print(f'le nombre de pages apres modification est {book1.get_pageNumber()}')
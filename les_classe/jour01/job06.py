class Animal:
    def __init__(self, age=0, prénom = ""):
        self.age = age
        self.prénom = prénom

    def vieillir(self):
        self.age +=1
        print(f"L'age de l'animal {self.age} ans")

    def nommer(self):
        self.prénom = "mamadoudou"
        print(f"L'animal se nomme {self.prénom} ")

anima_1 = Animal()
print(f"L'age de l'animal {anima_1.age} ans")
#l'age de l'animal apres appel de la methode vieillir:
print("#l'age de l'animal apres appel de la methode vieillir")
anima_1.vieillir()
print('\n')

print("#le nom de l'animal apres appel de la methode nommer")
anima_1.nommer()


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, new_rayon):
        self.rayon = new_rayon
        return self.rayon

    def afficherInfos(self):
        print(f'le nouveau rayon est {self.rayon}')
        print(f'la circonference du cercle est de {self.circonférence()}')
        print(f"l'aire du cercle est de {self.aire()}")
        print(f"le diametre du cercle est de {self.diametre()}")

    def circonférence(self):
        diamétre = self.rayon * 2
        pi = 3.14
        circonference_cercle = diamétre * pi
        return circonference_cercle

    def aire(self):
        pi = 3.14
        return pi*self.rayon**2

    def diametre(self):
        return self.rayon * 2


cercle_1 = Cercle(4)
cercle_2 = Cercle(7)

print("cercle_1:")
cercle_1.afficherInfos()

print("\ncercle_2:")
cercle_2.afficherInfos()
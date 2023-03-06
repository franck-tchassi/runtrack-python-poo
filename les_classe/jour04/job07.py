class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur



class Jeu(Carte):
    def __init__(self, valeur, couleur):
        super().__init__(valeur, couleur)
        self.paquet = []

    
class personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire: 'personnage', degats: int):
        adversaire.vie -= degats



class jeu:
    def __init__(self):
        self.niveau = None

    
    def choisirNiveau(self):
        niv = ["facile", "normal", "difficile"]
        niveau = input("choisir le niveau de jeu (facile, normal, difficile) :")
        while niveau not in niv:
            niveau = input("choisir le niveau de jeu exacte (facile, normal, difficle) :")
        self.niveau = (niveau)

        
    def lancerJeu(self):
        if self.niveau == "facile":
            joueur1= personnage("joueur", 120)
            enemi1 = personnage("demon", 90)
        elif self.niveau == "normal":
            joueur1= personnage("joueur", 90)
            enemi1 = personnage("enemi", 90)

        else:
            joueur1= personnage("joueur", 50)
            enemi1 = personnage("enemi", 100)
        print(f'le jeu commence!')
        print(f"Vous affrontez {enemi1.nom} avec {joueur1.vie} points de vie.")

        while joueur1.vie > 0 and enemi1.vie > 0:
            degats = int(input("Entrez les dégâts que vous voulez infliger : "))
            joueur1.attaquer(enemi1, degats)
            if enemi1.vie > 0:
                enemi1.attaquer(joueur1, 10)
            print(f"{joueur1.nom} : {joueur1.vie} points de vie")
            print(f"{enemi1.nom} : {enemi1.vie} points de vie")
        
        if joueur1.vie <= 0:
            print("Vous avez perdu !")
        else:
            print("Vous avez gagné !")

jeu1 = jeu()
jeu1.choisirNiveau()
jeu1.lancerJeu()
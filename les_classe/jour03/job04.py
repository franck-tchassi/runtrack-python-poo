class joueur:
    def __init__(self, nom, numéro, position):
        self.nom = nom
        self.numéro = numéro
        self.position= position
        self.nb_but_marquer = 0
        self.passe_decisif_éffectuer = 0
        self.carton_rouge_reçu = 0
        self.carton_jaune_reçu = 0

    def marquerUnBut(self):
        self.nb_but_marquer += 1

    def effectuerUnePasseDecisive(self):
        self.passe_decisif_éffectuer += 1

    def recevoirUnCartonJaune(self):
        self.carton_jaune_reçu += 1

    def recevoirUnCartonRouge(self):
        self.carton_rouge_reçu += 1

    def afficherStatistiques(self):

        print(f'nom           : {self.nom}')
        print(f'numero        :{self.numéro}') 
        print(f'position      :{self.position}')
        print(f'buts          :{self.nb_but_marquer}')
        print(f'passe decisif :{self.passe_decisif_éffectuer}')
        print(f'carton jaune  :{self.carton_jaune_reçu}') 
        print(f'carton rouge  :{self.carton_rouge_reçu}')






class EquipeDeFoot:
    def __init__(self, nom_équipe, joueur):
        self.nom_équipe = nom_équipe
        self.list_des_joueurs = []
        self.joueur = joueur
        

    def ajouterJoueur(self, joueur):
        ajout_joueurs = self.list_des_joueurs.append(joueur)
        return ajout_joueurs

    def AfficherStatistiquesJoueurs(self):
        print(f"statistique poue l'quipe:{self.nom_équipe}")
        for joueur in self.list_des_joueurs:
            self.joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom, nb_but_marquer=0, passe_decisif_éffectuer=0, carton_jaune_reçu=0, carton_rouge_reçu=0):
          for joueur in self.list_des_joueurs:
            if joueur.nom == nom:
                joueur.nb_but_marquer += nb_but_marquer
                joueur.passe_decisif_éffectuer += passe_decisif_éffectuer
                joueur.carton_jaune_reçu += carton_jaune_reçu
                joueur.carton_rouge_reçu += carton_rouge_reçu
                pass


joueur1 = joueur("tonio", 14, "milieu droite")
joueur2 = joueur("dago", 1, "gardien")

equipe1 = EquipeDeFoot("Real de Madrid", joueur1)
equipe2 = EquipeDeFoot("Barcelone", joueur2)

#ajout joueur équipe 1 (11joueurs entrant):
equipe2.ajouterJoueur("felipe")
equipe2.ajouterJoueur("bona")
equipe2.ajouterJoueur("malo")
equipe2.ajouterJoueur("toto")
equipe2.ajouterJoueur("roberto")
equipe2.ajouterJoueur("zidane")
equipe2.ajouterJoueur("acel")
equipe2.ajouterJoueur("babari")
equipe2.ajouterJoueur("messi")
equipe2.ajouterJoueur("ronaldo")

#ajout joueur équipe 2 (11joueurs entrant):
equipe2.ajouterJoueur("enzo")
equipe2.ajouterJoueur("moule")
equipe2.ajouterJoueur("paquet")
equipe2.ajouterJoueur("poulet")
equipe2.ajouterJoueur("banane")
equipe2.ajouterJoueur("oignon")
equipe2.ajouterJoueur("tomate")
equipe2.ajouterJoueur("bibi")
equipe2.ajouterJoueur("sardine")
equipe2.ajouterJoueur("maiis")

equipe2.AfficherStatistiquesJoueurs()



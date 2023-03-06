class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = ["à faire", "terminer"]


class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache_à_ajouter):
        tache = self.taches.append(tache_à_ajouter)
        return tache

    def supprimerTache(self, tache_à_supprimé):
        supprimer = self.taches.remove(tache_à_supprimé)
        return supprimer
    
    def marquerCommeFinie(self):
        if self.taches == self.statut[1]:
            print("la tache est faite")
        else:
            print("la tache doit etre faite")

    def afficherListe(self):
        return self.taches

    def filterListe(self):
        pass


tache1 = ListeDeTaches()

tache1.ajouterTache("math")
tache1.ajouterTache("français")
print(tache1.afficherListe())
tache1.supprimerTache("math")
print(tache1.afficherListe())

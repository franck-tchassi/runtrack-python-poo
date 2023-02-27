class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        total_a_payer = self.prixHT * (1 + self.TVA / 100)
        return total_a_payer
        

    def afficher(self):
        print(f'nom: {self.nom}')
        print(f'prixHT: {self.prixHT} £')
        print(f'TVA: {self.TVA} %')
        print('\n')

    def modifier_nom(self, nouveauNom):
        self.nom = nouveauNom

    def modifier_PrixHT(self, nouveauPrixHT):
        self.prixHT = nouveauPrixHT

    def retourne_nom(self):
        return self.nom

    def retourne_PrixHT(self):
        return self.prixHT

produit_001 = Produit("chaussure", 93.99, 9.50)
produit_002 = Produit("cahier", 7.99, 9)
produit_003 = Produit("chemise", 119.23, 9.50)

produit_001.CalculerPrixTTC()
produit_002.CalculerPrixTTC()
produit_003.CalculerPrixTTC()   

produit_001.afficher()
produit_002.afficher()
produit_003.afficher()
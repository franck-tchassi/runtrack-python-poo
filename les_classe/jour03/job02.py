class CompteBancaire:
    def __init__(self, numero_compte, nom, prénom, solde, découvert):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prénom = prénom
        self.__solde = solde
        self.découvert = découvert

    def afficher(self):
        print(f'nom et prénom:    {self.__nom} {self.__prénom}')
        print(f'numero de compte: {self.__numero_compte}')
        print(f'solde du compte:  {self.__solde} £')
    
    def afficherSolde(self):
        print(f'le solde du client est de {self.__solde} £')

    def versement(self, montant_à_verser):
        self.__solde += montant_à_verser 

    def retrait(self, montant_à_retirer):
        if self.découvert == True:
            self.__solde -= montant_à_retirer
        else:
            if montant_à_retirer > self.__solde:
                print("compte insuffisant")
            else:
                self.__solde -= montant_à_retirer
                print(self.__solde)
    
    def agios(self):
        pass

    def virement(self, compte2, montants):
        pass


compte1 = CompteBancaire(235455467, "TCHASSI", "FRANCK", 1500, False)
compte2 = CompteBancaire(235455467, "sebastier", "charle", -800, False)

#compte1.afficher()
#compte1.afficherSolde()
#compte1.versement(500)
compte1.afficherSolde()
compte1.retrait(3000)
compte1.afficherSolde()


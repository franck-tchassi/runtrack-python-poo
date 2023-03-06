class commande:
    def __init__(self, Numero_commande):
        self.__Numero_commande = Numero_commande
        self.__list_plat_commander = []
        self.__statu_commande = ["en cours", "terminé", "annulé"]

    #ajouter un plat à une commande
    def ajout_commande(self, list_plat_commander): 
        self.__list_plat_commander.append(list_plat_commander)
    #afficher list des commande y compris des commante ajouter
    def affiche_commande(self):   
        return self.__list_plat_commander 
    
    #annulé une commande
    def annulé_commande(self):   
        return self.__statu_commande[2]

    #CALCUL totaux des commandes
    def __totaux_des_commandes(self):
        total_commande = 0
        for list_plat_commander in self.__list_plat_commander:
            total_commande += list_plat_commander.prix_de_commande
        return total_commande
    
    def affiche_une_commande_avec_totaux_à_payer(self):
        print(f'commande numero {self.__Numero_commande}')
        for list_plat_commander in self.__list_plat_commander:
            print(f'{self.nomPlat}: {self.prixPlat}')
        print(f'prix total des commande est de: {self.__totaux_des_commandes}')


    def calculer_TVA(self, pourcentage_tva):
        total = self.__totaux_des_commandes()
        tva = total * pourcentage_tva / 100
    
plat1 = commande(5)
plat1.ajout_commande("tapioca")
plat1.ajout_commande('pistache')

print(f'{plat1.affiche_commande()}')
plat1.annulé_commande()
print(f'{plat1.annulé_commande()}')


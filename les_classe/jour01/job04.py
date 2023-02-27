class personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print(f'je suis {self.nom} {self.prenom}')
    
#creation de 4 objets:
personne_1 = personne("jean", "DIEU")
personne_2 = personne("iness", "mohemat")
personne_3 = personne("abdel", "zozobolazo")
personne_4 = personne("patient", "langemoise")

personne_1.SePresenter() 
personne_2.SePresenter() 
personne_3.SePresenter() 
personne_4.SePresenter() 
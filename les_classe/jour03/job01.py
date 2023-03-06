class Ville:
    def __init__(self, nom_ville, nbs_habitants):
        self.__nom_ville = nom_ville
        self.__nbs_habitants = nbs_habitants
    
    def ajoute_habitants(self):
        self.__nbs_habitants += 1

    def get_nbs_habitants(self):
        return self.__nbs_habitants

class Personne():
    def __init__(self, nom_personne, age_personne, Ville):
        self.__nom_personne = nom_personne
        self.__age_personne = age_personne
        self.__Ville = Ville

    def ajouterPopulation(self):
        self.__Ville.ajoute_habitants()
  


ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marsseille", 861635)

personne1 = Personne("John", 45, ville1)
personne2 = Personne("Myrtille", 4, ville1)
personne3 = Personne("Chloé", 18, ville2)


print(f'population de la ville de paris: {ville1.get_nbs_habitants()} habitants')
print(f'population de la ville de Marsseille: {ville2.get_nbs_habitants()} habitants')
print('\n')

personne1.ajouterPopulation()
personne2.ajouterPopulation()


print(f'mise à jour population de la ville de paris: {ville1.get_nbs_habitants()} habitants')
print(f'mise à jour population de la ville de Marsseille: {ville2.get_nbs_habitants()} habitants')
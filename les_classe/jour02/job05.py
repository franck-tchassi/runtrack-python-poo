class Voiture:
    def __init__(self, marque, modèle, année, kilométrage):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque
    def set_marque(self, marque):
        self.__marque = marque

    def get_modèle(self):
        return self.__modèle
    def set_modèle(self, modèle):
        self.__modèle = modèle

    def get_année(self):
        return self.__année
    def set_année(self, année):
        self.__année = année

    def get_kilométrage(self):
        return self.__kilométrage
    def set_kilométrage(self, kilométrage):
        self.__kilométrage = kilométrage
    
    def demarrer(self):
        self.__en_marche = True
        if self.__reservoir > 5:
            return self.__verifier_plein()
        else:
            print("le reservoir n'est pas supérier à 5")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir
    
#voiture1 = Voiture("Land Rover", "le range rover sport", 3, 100000)

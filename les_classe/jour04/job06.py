class Vehicule:
    def __init__(self, marque, année, prix):
        self.marque = marque
        self.année = année
        self.prix = prix

    def informationsVehicule(self):
        print(f'-la marque = {self.marque}')
        print(f"-l'année   = {self.année}")
        print(f'-le prix   = {self.prix}£') 

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, année, prix, portes=4):
        super().__init__(marque, année, prix)
        self.portes = portes
    
    def informationsVehicule(self):
        print(f'-la marque = {self.marque}')
        print(f"-l'année   = {self.année}")
        print(f'-le prix   = {self.prix}£') 
        print(f'-le nombre de portes = {self.portes}')

    def demarrer(self):
        print("Attention, je roule")


class Moto(Vehicule):
    def __init__(self, marque, année, prix, roue=2):
        super().__init__(marque, année, prix)
        self.roue = roue
    
    def informationsVehicule(self):
        print(f'-la marque = {self.marque}')
        print(f"-l'année   = {self.année}")
        print(f'-le prix   = {self.prix}£') 
        print(f'-le nombre de roue = {self.roue}')
    
    def demarrer(self):
        print("Attention, je roule")


print("ma voiture :")
voiture = Voiture("Toyota", 2017, 25000)
voiture.informationsVehicule()
voiture.demarrer()
print('\n')

print("ma moto :")
moto = Moto("Mercedes", 2020, 15000)
moto.informationsVehicule()
moto.demarrer()
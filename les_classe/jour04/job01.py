
class Personne:     
       
    # Constructeur         
    def __init__(self):    
        self.age = 14
     
 
    def afficherAge(self): 
        print("age : ",self.age) 
    
    def bonjour(self): 
        print("Hello") 

    def modifierAge(self, age):
        self.age = age
        self.age
             
 
 
class Eleve( Personne ): 
 
    def __init__(self): 
        Personne.__init__(self) 

    def allerEnCours(self):
        print("je vais en cours") 

    def affichageAge(self):
        print(f"j'ai {self.age} ans") 
   

class Professeur:
    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer")
   
 
P= Personne()
E= Eleve()
P.modifierAge(20)
E.affichageAge()
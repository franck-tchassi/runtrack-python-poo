class Student:
    def __init__(self, nom, prénom, NumeroEtudiant):
        self.__nom = nom
        self.__prénom = prénom
        self.__NumeroEtudiant = NumeroEtudiant
        self.__nombreCredit = 0
        self.__level = self.__studentEval()

    def add_credits(self, nombreCredit):
        if nombreCredit > 0:
            self.__nombreCredit += nombreCredit
            #ajout level
            self.__level = self.__studentEval()

        else:
            print("le nombre de crédoit doit etre superieur à zéro")
    
    def get_credit(self):
        return self.__nombreCredit
    
    def get_nom(self):
        return self.__nom
    def get_prénom(self):
        return self.__prénom
    def get_NumeroEtudiant(self):
        return self.__NumeroEtudiant
    
    def __studentEval(self):
        if self.__nombreCredit >= 90:
            return "Excellent"
        elif self.__nombreCredit >= 80:
            return "Très bien"
        elif self.__nombreCredit >= 70:
            return "Bien"
        elif self.__nombreCredit >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print("Nom =",self.__nom)
        print("Prénom =",self.__prénom)
        print("id =",self.__NumeroEtudiant)
        print("Niveau =",self.__level)

    

éleve1 = Student("John", "Doe", "145")

#crédit ajouter à trois reprise
éleve1.add_credits(10)
éleve1.add_credits(10)
éleve1.add_credits(10)
#total de crédit de l'etudiant:
print(f"le nombre de crédits de {éleve1.get_nom()} {éleve1.get_prénom()} d'itentifiant {éleve1.get_NumeroEtudiant()} est de {éleve1.get_credit()} points ")
print('\n')
éleve1.studentInfo()


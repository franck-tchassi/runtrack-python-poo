class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = x
    
    def gauche(self):
        self.y -=1
        

    def droite(self):
        self.y +=1
        

    def bas(self):
        self.x -=1
        

    def haut(self):
        self.x +=1
        

    def position(self):
        return(self.x, self.y)

junior = Personnage(6, 1)
print(junior.position())
        
     
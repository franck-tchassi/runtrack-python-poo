class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #construction des méthodes:
    def afficherLesPoints(self):
        print((self.x, self.y))
    
    def afficherX_et_afficherY (self):
        print(f'X = {self.x}')
        print(f'Y = {self.y}')

    def changerX_et_changerY(self, new_x=10, new_y=15):
        self.x = new_x
        self.y = new_y
        
        print(f'la valeur de x et y est ({self.x}, {self.y})')
        

# construction des instances d'objects:

point_C = Point(-6, 4)

#affichage des points:
print("#affichage des points:")
point_C.afficherLesPoints()
print('\n')

#afficher X et afficher Y
print("#afficher X et afficher Y:")
point_C.afficherX_et_afficherY()
print('\n')

#changer valeur de x et y:
print("#changer valeur de x et y:")
point_C.changerX_et_changerY()
print('\n')

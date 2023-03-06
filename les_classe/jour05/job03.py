def longueur(chaine):
    if chaine == "":
        return 0
    else:
        return 1 + longueur(chaine[1:])

chaine = input("Entrez une chaine de caracteres : ")
resultat = longueur(chaine)
print("La longueur de", chaine, "est", resultat)

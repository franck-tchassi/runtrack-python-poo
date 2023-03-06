def max_chiffre(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        max_rest = max_chiffre(liste[1:])
        return liste[0] if liste[0] > max_rest else max_rest

liste = [4, 2, 8, 5, 1, 9, 3]
resultat = max_chiffre(liste)
print("Le plus grand chiffre de", liste, "est", resultat)
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

nombre = int(input("Entrez un nombre entier : "))
resultat = factorielle(nombre)
print("La factorielle de", nombre, "est", resultat)
def puissance(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return puissance(x*x, n//2)
    else:
        return x*puissance(x*x, (n-1)//2)

x = 2  # valeur constante
nombre = int(input("Entrez un nombre entier : "))
resultat = puissance(x, nombre)
print(x, "^", nombre, "=", resultat)
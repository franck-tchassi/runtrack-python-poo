def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Entrez un entier n : "))
resultat = fibonacci(n)
print("Le", n, "eme nombre de la suite de Fibonacci est", resultat)
# Exercice a
def a():
    nombre = int(input("Renseigner un nombre : "))
    compteur = 0

    while (nombre > compteur):
        compteur = compteur + 1
        print(f"Voici la nouvelle valeur : {compteur}")

# Exercice b
def b():
    while True:
        nombre = int(input("Renseigner un nombre : "))
        if nombre == 100:
            print(f"Vous venez de remplir la condition !")
            break;
        else:
            print(f"Vous n'avez pas remplit la condition, réessaye encore !")

# Exercice c
def c():
    inf10 = 0
    inf15 = 0
    sup15 = 0

    for valeur in range(0,10):
        nombre = int(input("Renseigner un nombre : "))
        if nombre < 10:
            inf10 = inf10 +1
        elif nombre >= 10 and nombre < 15:
            inf15 = inf15 +1
        elif nombre >= 15:
            sup15 = sup15+1
    print(f"Il y a {inf10} nombre inférieur à 10, {inf15} nombre entre 10 et 15 exclu et {sup15} nombre supérieur ou égal à 15.")

# Exercice d
def d():
    i = 0
    n = 0
    nombre = int(input("Renseigner un nombre : "))
    while nombre > i:
        i = i+1
        nombre = nombre - i
    print(f"Le nombre N est {i}")

# Partie permettant de choisir l'exercice à exécuter
choix = input("Choisissez l'exercice à exécuter : ")

if choix == "a":
    a()
if choix == "b":
    b()
if choix == "c":
    c()
if choix == "d":
    d()
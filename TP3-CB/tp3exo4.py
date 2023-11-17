nombre = int(input("Renseigner un nombre : "))
choix = input("Choisissez la boucle à utiliser (while ou for) : ")

def fonction_while(nombre):
    i = 1
    n = 1
    while i <= nombre:
        n = n * i
        i = i + 1
        print(f"Voici l'avancé du calcul : {n}")

def fonction_for(nombre):
    i = 1
    n = 1
    for x in range(1,nombre+1):
        n = n * i
        i = i + 1
        print(f"Voici l'avancé du calcul : {n}")

if choix == "while":
    fonction_while(nombre)
if choix == "for":
    fonction_for(nombre)
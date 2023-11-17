import random

n = 0
while True:
    valeur = random.randrange(0, 100)
    nombre = int(input("Renseigner un nombre : "))
    n = n + 1
    if nombre == valeur:
        print(f"Bravo ! Vous avez trouvé le nombre mystème au bout de {n} tentative !")
        break;
    else:
        print(f"Loupé ! Tu as fais {n} tentative(s) ! Encore un tour ?")
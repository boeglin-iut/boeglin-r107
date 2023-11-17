import random

valeur = random.randrange(0, 100)

n = 0
while True:
    nombre = int(input("Renseigner un nombre : "))
    n = n + 1
    if nombre == valeur:
        print(f"Bravo ! Vous avez trouvé le nombre mystème au bout de {n} tentative !")
        break;
    else:
        if nombre > valeur:
            print(f"Vous êtes au delà du nombre à deviner !")
        else:
            print(f"Vous êtes en dessous du nombre à deviner !")
        print(f"Loupé ! Tu en es à {n} tentative(s) !")
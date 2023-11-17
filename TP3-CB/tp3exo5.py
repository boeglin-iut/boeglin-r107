heure_debut = int(input("Donnez l’heure de début de la location (un entier) : "))
heure_fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

if heure_debut > heure_fin:
    print(f"Attention ! le début de la location est après la fin ...")
    exit()

heure_pleine = 0
heure_creuse = 0

while True:
    if heure_fin > 7 and heure_fin <= 17:
        if heure_fin == heure_debut:
            break
        else:
            heure_fin = heure_fin - 1
            heure_pleine = heure_pleine + 1
    else:
        if heure_fin == heure_debut:
            break
        else:
            heure_fin = heure_fin - 1
            heure_creuse = heure_creuse + 1

print(f"Vous avez loué votre vélo pendant")

if heure_creuse != 0:
    print(f"{heure_creuse} heure(s) au tarif horaire de 1.0 euro")

if heure_pleine != 0:
    print(f"{heure_pleine} heure(s) au tarif horaire de 2.0 euros")

prix = (heure_pleine*2) + heure_creuse
print(f"Le montant total à payer est de {prix}€.")
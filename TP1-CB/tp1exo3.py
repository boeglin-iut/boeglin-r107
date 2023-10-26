jour=int(input("Indiquer le jour actuel : "))
heure=int(input("Indiquer l'heure actuelle : "))
minute=int(input("Indiquer la minute actuelle : "))

temps=(jour*24*60) + (heure*60) + minute
print(f"Voici le nombre de minute passé ce mois-ci pour {jour} jour(s), {heure} heure(s) et {minute} minute(s) :", temps)
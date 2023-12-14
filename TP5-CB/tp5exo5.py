heure = int(input("Entrez le nombre d'heures travaillées : "))
salaireHoraire = float(input("Entrez le salaire horaire : "))
salaire = 0

if heure <= 160:
    salaire = heure * salaireHoraire
elif heure <= 200:
    salaire = 160 * salaireHoraire + (heure - 160) * salaireHoraire * 1.25
else:
    salaire = 160 * salaireHoraire + 40 * salaireHoraire * 1.25 + (heure - 200) * salaireHoraire * 1.5

print(f"Le salaire est de {salaire} €")
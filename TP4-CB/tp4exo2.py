nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for e in range (nombreEtudiants):
    note = float(input(f"Note etudiant {e} : "))
    if note >= 0 and note <= 20:
        notes.append(note)
        moyenne = moyenne + note
    else:
        print(f"Merci de rentrer une note valide !")

moyenne = moyenne / nombreEtudiants
print(f"Moyenne de la classe : {moyenne}")
print(f"Numéro de l'Etudiant | note | ecart a la moyenne")

for e in range (nombreEtudiants):
    print(f"{e} | {notes[e]} | {notes[e] - moyenne}")
nombreNote = int(input("Donnez le nombre de note à renseigner : "))
moyenne = 0.0
coef = 0.0
noteEliminatoire = False
notes = []

for n in range (nombreNote):
    s1 = str(input(f"Veuillez entrer la note du module {n} et le coefficiant correspondant : "))
    s2 = s1.split(" ")
    s3 = float(s2[0])
    s4 = float(s2[1])
    moyenne += s3*s4
    coef += s4
    if s3 < 8:
        noteEliminatoire = True

print(f"Voici la moyenne de l'étudiant : {moyenne/coef}")

if((moyenne/coef) >= 10):
    if(noteEliminatoire == False):
        print(f"L'étudiant est admis !")
    else:
        print(f"L'étudiant n'est pas admis !")
else:
    print(f"L'étudiant n'est pas admis !")
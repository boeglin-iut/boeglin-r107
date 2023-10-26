nom = input("Renseigner le nom : ")
prenom = input("Renseigner le prénom : ")
math = int(input("Renseigner la note de maths : "))
anglais = int(input("Renseigner la note d'anglais : "))
info = int(input("Renseigner la note d'informatique : "))
promotion = input("Renseigner la promotion : ")

moy = (math+anglais+info)/3

print(f"L'étudiant {prenom} {nom} de la promotion {promotion} a une moyenne de {moy}")
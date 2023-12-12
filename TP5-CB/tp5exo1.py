nom1 = str(input("Nom du 1er étudiant : "))
prenom1 = str(input("Prénom du 1er étudiant : "))
nom2 = str(input("Nom du 2ème étudiant : "))
prenom2 = str(input("Prénom du 2ème étudiant : "))

if(nom1.lower() < nom2.lower()):
    print(f"NOM Prénom du 1er étudiant : {nom1.upper()} {prenom1.capitalize()}")
    print(f"NOM Prénom du 2ème étudiant : {nom2.upper()} {prenom2.capitalize()}")
else:
    print(f"NOM Prénom du 1er étudiant : {nom2.upper()} {prenom2.capitalize()}")
    print(f"NOM Prénom du 2ème étudiant : {nom1.upper()} {prenom1.capitalize()}")
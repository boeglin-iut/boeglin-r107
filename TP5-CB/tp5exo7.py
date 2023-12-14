import os.path
import datetime

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

if os.path.isfile(fichier1):
    print(f"La taille du fichier {fichier1} est de {os.path.getsize(fichier1)} octets.")
    print(f"Le fichier {fichier1} a été modifié le {datetime.datetime.fromtimestamp(os.path.getmtime(fichier1))}")
else:
    print(f"le fichier {fichier1} n'existe pas.")

if os.path.isfile(fichier2):
    print(f"La taille du fichier {fichier2} est de {os.path.getsize(fichier2)} octets.")
    print(f"Le fichier {fichier2} a été modifié le {datetime.datetime.fromtimestamp(os.path.getmtime(fichier2))}")
else:
    print(f"le fichier {fichier2} n'existe pas.")
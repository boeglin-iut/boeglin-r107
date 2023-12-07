nMax=int(input(f"Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))
while nMax < 1 or nMax > 10:
    print(f"Merci de renseigner une taille entre 1 et 10 !")
    nMax = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

somme = 0
v1 = []
v2 = []

print(f"Saisie du premier vecteur : ")
for n in range (nMax):
    v1.append(int(input(f"v1[{n}] = ")))

print(f"Saisie du second vecteur : ")
for n in range (nMax):
    v2.append(int(input(f"v2[{n}] = ")))

for n in range (nMax):
    somme = somme + (v1[n] * v2[n])

print(f"Le produit scalaire de v1 par v2 vaut {somme}")
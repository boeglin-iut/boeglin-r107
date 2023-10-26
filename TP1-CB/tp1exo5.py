import random

first=int(input("Renseigner le 1er nombre : "))
second=int(input("Renseigner le 2ème nombre : "))
repeat=int(input("Renseigner le nombre de répétition : "))

for i in range(repeat):
    result = random.randrange(first, second)
    print(f"Voici le nombre aléatoire généré : {result}")
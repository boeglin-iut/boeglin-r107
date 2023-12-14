string = str(input("Entrez une chaine de caractères : "))

length = 0
nombreVoyelle = 0
repetition = 0

string.lower()

for i in string:
    length += 1
    if i in "aeiouy":
        nombreVoyelle += 1
    if i == "w":
        if string[length:length+4] == "agon":
            repetition += 1

print(f"La taille de la chaine est de {length} caractères.")
print(f"Le pourcentage de voyelles est de {nombreVoyelle / length * 100} %.")

if repetition != 0:
    print(f"La chaine 'wagon' apparait {repetition} fois.")
else:
    print(f"La chaine 'wagon' n'apparait pas dans la chaine.")
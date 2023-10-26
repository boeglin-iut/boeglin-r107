a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

temp_a=a
temp_b=b
temp_c=c

b=temp_a
c=temp_b
a=temp_c

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)
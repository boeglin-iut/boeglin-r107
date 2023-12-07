dic = {"firstname": "Corentin", "name": "BOEGLIN", "promo": "RT1", "group": "RT121"}

print(f"Votre nom est {dic["name"]}, prénom est {dic["firstname"]}, vous faites partie de la promo {dic["promo"]} et votre groupe est {dic["group"]}")

print("Les clés du dictionnaire sont :")
for i in dic.keys():
    print("-", i)

print("Les valeurs du dictionnaire sont :")
for i in dic.values():
    print("-", i)

print("Les tuplets du dictionnaire sont :")
for i in dic.items():
    print("-", i)

binome = {"firstname": "Titi", "name": "TOTO", "promo": "RT2", "group": "RT211"}

print(f"Les étudiants formants le binôme sont :")
print(f"L'étudiant {dic["name"]} {dic["firstname"]} du groupe {dic["group"]}")
print(f"L'étudiant {binome["name"]} {binome["firstname"]} du groupe {binome["group"]}")
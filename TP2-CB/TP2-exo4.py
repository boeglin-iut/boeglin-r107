BASE=4
fromage=800.0
eau=2
ail=2
pain=400

nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage * nbConvives / BASE} gr de fromage")
print(f"- {eau * nbConvives / BASE} dl d'eau")
print(f"- {ail * nbConvives / BASE} gousse(s) d'ail")
print(f"- {pain * nbConvives / BASE} gr de pain")
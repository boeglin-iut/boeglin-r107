nombre=float(input(f"Vous cherchez la table de multiplication de quel nombre ? "))
temp = 0

while temp < 10:
    print(f"{nombre} * {temp} = {round(nombre*temp, 1)}")
    temp = temp + 1
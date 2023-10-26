temps=int(input("Indiquer le nombre de minute(s) écoulé(s) : "))

jour = temps // (24*60)
temps = temps - (jour*24*60)
heure = temps // 60
temps = temps - heure*60
minute = temps

print(f"Il y a {jour} jour(s), {heure} heure(s) et {minute} minute(s).")
date=input(f"Renseigner une date sous la forme jjmmaaaa : ")

def bonneDate():
    print(f"La date renseigné est bien sous la forme jjmmaaaa !")

def mauvaiseDate(min, max, type):
    print(f"La date renseigné n'est pas sous la forme jjmmaaaa ! Merci de renseigner la valeur {type} avec une valeur comprise entre {min} et {max}")

if len(date) != 8:
    mauvaiseDate(0, 9999, "de l'année")
    exit(0)

jour=int(date[0:2])
mois=int(date[2:4])
annee=int(date[4:8])

if mois < 1 or mois > 12:
                mauvaiseDate(1, 12, "du mois")
else:
    if mois == 2:
        if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
            if jour < 1 or jour > 29:
                mauvaiseDate(1, 29, "du jour")
            else:
                bonneDate()
        else:
            if jour < 1 or jour > 28:
                mauvaiseDate(1, 28, "du jour")
            else:
                bonneDate()
    else:
        if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
            if jour < 1 or jour > 31:
                mauvaiseDate(1, 31, "du jour")
            else:
                bonneDate()
        else:
            if jour < 1 or jour > 30:
                mauvaiseDate(1, 30, "du jour")
            else:
                bonneDate()
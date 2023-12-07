binome = ("login1", "login2")
print(f"{binome[0]} est en binome avec {binome[1]}")

binome[1] = input(f"Renseigner le nouveau binome : ")
print(f"{binome[0]} est en binome avec {binome[1]}")

del binome[1]
print("L’étudiant", binome[0], "est en binome avec l’étudiant", binome[1])

binome = binome + ("login3")
print(f"{binome[0]} est en binome avec {binome[1]} et {binome[2]}")

# les tuplets ne peuvent pas subir de modification à part l'ajout d'éléments
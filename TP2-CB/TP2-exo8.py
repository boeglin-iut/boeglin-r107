x=float(input("Entrez un nombre décimal : "))

if x > 2 or x == 2 and x < 3:
    print("x appartient à I")
elif x > 0 and x < 1 or x == 1:
    print("x appartient à I")
elif x > -10 or x == 10 and x < -2 or x == 2:
    print("x appartient à I")
else:
    print("x n'appartient pas à I")
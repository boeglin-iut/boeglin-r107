L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
nombre = None
repetition = 0

for i in L1:
    temp = L1.count(i)
    if temp > repetition:
        repetition = temp
        nombre = i

print(f"Le nombre le plus frequent dans la liste est le : {nombre} ({repetition} x)")
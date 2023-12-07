n = [5, 2, 4, 8, 1, 3]

for i in range(len(n)):
    for x in range(i+1, len(n)):
        if n[i] > n[x]:
            n[i], n[x] = n[x], n[i]
            print(n)

# question 2 : la liste déclaré est directement trié, sans passer par des boucles et des conditions
# question 3 : comme la question 2, la table est directement trié
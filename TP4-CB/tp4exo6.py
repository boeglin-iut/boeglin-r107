n = [5, 2, 4, 8, 1, 3]

for i in range(len(n)):
    for x in range(i+1, len(n)):
        if n[i] > n[x]:
            n[i], n[x] = n[x], n[i]
            print(n)

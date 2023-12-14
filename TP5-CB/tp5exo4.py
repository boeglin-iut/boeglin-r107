somme = int(input(f"Entrez la somme : "))
sommeInit = somme

billet100 = somme // 100
somme = somme % 100

billet50 = somme // 50
somme = somme % 50

billet10 = somme // 10
somme = somme % 10

piece2 = somme // 2
somme = somme % 2

piece1 = somme // 1
somme = somme % 1

print(f"{sommeInit} euro(s), c'est donc {billet100} billets de 100€, {billet50} billets de 50€, {billet10} billets de 10€, {piece2} pièces de 2€, {piece1} pièce de 1€")
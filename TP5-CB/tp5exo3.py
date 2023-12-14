phrase = input("Entrez un mot ou une phrase : ")

phrase = phrase.lower()

for p in phrase:
    if not p.isalpha():
        phrase = phrase.replace(p, "")

if phrase == phrase[::-1]:
    print("La phrase est un palindrome.")
else:
    print("La phrase n'est pas un palindrome.")
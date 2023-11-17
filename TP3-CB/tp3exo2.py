import time

nombre = int(input("Renseigner un nombre : "))

while nombre >= 0:
    print(nombre)
    nombre = nombre - 1
    time.sleep(1)

for n in range(0,nombre):
    nombre = nombre - 1
    print(nombre)
    time.sleep(1)
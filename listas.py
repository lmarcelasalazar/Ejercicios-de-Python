listas = ["renault", "chevrolet", "mazda"]
for i in listas:
    print(i, end="")

for i in range (len(listas)):
    print(listas[i], end="")

for i in range (len(listas)-2):
    print(listas[i], end="")


auxiliar = listas[:2]
print(auxiliar)
listas.insert(i, "audi")
print(listas)
auxiliar=listas[1:]
print(auxiliar)
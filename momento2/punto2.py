def subtotal(producto,cantidad):
    subtotal=producto + cantidad
    return subtotal

cesta={}
centinela='si'
for i in range (11):
    while centinela=='si':
        clave=input("Producto a comprar: ")
        valor=int(input(clave+': '))
        cesta[clave]=valor
    print(cesta)
    centinela=input("Desea continuar? si/no: ")
print(cesta)


total = 0
for null,valor in cesta.items():
    total += valor
print("el precio de los productos es: ", total)
print("el subtotal es: ", subtotal)

    
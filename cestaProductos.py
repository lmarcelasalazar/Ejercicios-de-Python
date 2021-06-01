cesta={}
centinela='si'
while centinela=='si':
    total=0
    clave=input("Introduzca el producto a comprar: ")
    valor=int(input(clave+':'))
    cesta[clave]=valor
    print(cesta)
    total= (valor + centinela)
    print(total)
    centinela=input("si desea continuar /si no: ")
print(cesta)
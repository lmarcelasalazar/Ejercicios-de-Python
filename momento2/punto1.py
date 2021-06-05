centinela="si"
cont=0
salario=0
comision=0
bono=0
while cont<5:
     identificacion=int(input("Ingresar identificacion: "))
     nombre=input("Ingresar nombre: ")
     while centinela=="si":
          if salario>900000:
               salario=int(input("Ingresar salario: "))
          elif comision >0:
               comision=int(input("Ingresar comision: "))
          elif bono >0:
               bono=int(input("Ingresar bonificacion: "))
     total=salario+comision
     print("Desea continuar si/no: ")
cont=cont+1
print("Salario: ",salario)
print("Comision: ",comision)
print("Bonificacion: ",bono)

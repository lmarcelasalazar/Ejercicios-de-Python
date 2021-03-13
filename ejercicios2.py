#centinela="si"
#contador=0
#contador2=0
#while (centinela=="si"):
 #   genero=input("Ingrese su genero: ")
  #  if genero=="m":
   #     contador = contador + 1
    #else:
     #   contador2=contador2+1
      #  centinela=input("ingrese si desea continuar si/no: ")
    #contador_suma=contador+contador2
#print("el numero de mujeres que ingreso es: ",contador)
#print("el numero de hombres que ingreso es: ",contador2)
#print("el total de personas que ingresaron es: ",contador_suma)


centinela="si"
contador=0
contador2=0
contador3=0
analista=870000
arquitecto=790000
desarrollador=2300000
while (centinela=="si"):
    cargo=input("Ingrese el cargo: ")
    if cargo=="analista":
        contador = contador + 1
    elif cargo=="arquitecto":
        contador2 = contador2 + 1
    else:
        contador3 = contador3 + 1
        centinela=input("ingrese si desea continuar si/no: ")
        contador_suma=contador+contador2+contador3
        contador_inversion=analista+arquitecto+desarrollador
print("el numero de analistas es: ",contador)
print("el numero de arquitectos es: ",contador2)
print("el numero de desarrolladores es: ",contador3)
print("el total de personas es: ",contador_suma)
print("el total de la inversion es: ",contador_inversion)

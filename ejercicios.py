###--------------Punto #1-------------
#tPrestamo= int(input("Tiempo de Prestamo: "));
#vlrCuota = tPrestamo * 0.136; 
#print("El valor de la cuota es: ", vlrCuota);

####-------------Punto #2-------------
#nombre=input("Ingrese su nombre: ");
#edad=int(input("Ingrese su edad: "));
#tel=int(input("Ingrese su telefono: "));
#print("Nombre: ",nombre);
#print("Edad: ",edad);
#print("Telefono: ",tel);

####-------------Punto #3-------------
print("Ingrese el prestamo: ")
valor_prestamo=int(input())
interes_mensual = int(((valor_prestamo/17)*0.018))
print("La cuota mensual",interes_mensual)
cuota_mensual = int(valor_prestamo/12) + interes_mensual
print("")
total_pagar_anual=((cuota_mensual*12) | cuota_mensual)
print("El valor anual es: ",total_pagar_anual)
total_pagar_dos=int(cuota_mensual*2)
print("total pagar en dos meses",total_pagar_dos)
total_pagar_nueve=int((cuota_mensual*9))
print("Total pagar en nueve meses",total_pagar_nueve)
interes_mensual=int((cuota_mensual*12))
print("Total pagar intereses",interes_mensual)

#vPrestamo=input(float("Ingrese valor del prestamo"))
#cmensual=(vPrestamo/12)*0.018
#print("Cuota Mensual")
#tPagarA=((cmensual*12)+cmensual))
#print("Valor Anual: ",tPagarA)
#servicio=(input("Ingrese el servicio: "))
#if servicio is "sencillo":
 #   pagar_servicio=(12000*0.19)+12000
#else:
 #   pagar_servicio=(15000*0.19)+15000
#print("el servicio que selecciono",servicio)
#print("el valor a pagar por el servicio es: ",pagar_servicio)

#producto=input("ingrese producto: ")
#if producto="lacteos":
   # cantidad=int(input("ingrese cantidad de productos: "))
  #  valor_pagar_sin_iva=cantidad*12000
 #   valor_pagar_iva=(valor_pagar_sin_iva*0.19)+valor_pagar_sin_iva
#else:
   # cantidad=int(input("ingrese cantidad de productos: "))
  #  valor_pagar_sin_iva=cantidad*15000
 #   valor_pagar_iva=(valor_pagar_sin_iva*0.19)+valor_pagar_sin_iva
#print("el producto seleccionado es: ",producto)
#print("valor a pagar sin iva: ",valor_pagar_sin_iva)
#print("valor a pagar con iva: ",valor_pagar_iva)

#nota1=float(input("Ingrese nota 1"))
#nota2=float(input("Ingrese nota 2"))
#nota3=float(input("Ingrese nota 3"))
#nota4=float(input("Ingrese nota 4"))
#nota5=float(input("Ingrese nota 5"))

#promedio_nota=(nota1*0.10)+(nota2*0.2)+(nota3*0.35)+(nota4*0.15)+(nota5*0.2)
#if(promedio_nota>=3.5):
 #   print("Ha ganado la materia")
#else:
 #   print("Perdio la materia",promedio_nota)

#tipo_vehiculo = input("Ingrese el tipo de vehiculo: ")
#tipo_lavado = input("Ingrese tipo de lavado: ")
#if(tipo_vehiculo=="Taxi") and (tipo_lavado=="Sencillo"):
 #    print("El valor a pagar por el servicio:",12300)
#elif (tipo_vehiculo=="Particular") and (tipo_lavado=="Sencillo"):
 #    print("El valor a pagar por el servicio:",15000)
#elif(tipo_vehiculo=="Camion") and (tipo_lavado=="Sencillo"):
 #    print("El valor a pagar por el servicio:",23000)
#elif(tipo_vehiculo=="Taxi") and (tipo_lavado=="Full"):
 #    print("El valor a pagar por el servicio:",25000)
#elif(tipo_vehiculo=="Particular") and (tipo_lavado=="Sencillo"):
 #    print("El valor a pagar por el servicio:",27000)
#else:
 #    print("El valor a pagar por el servicio:",28000)

#elif(tipo_lavado=="Full"):
#if(tipo_vehiculo=="Taxi"):
 #       print("El valor a pagar por el servicio:",25000)
#elif(tipo_vehiculo=="Particular"):
 #       print("El valor a pagar por el servicio:",27000)
#else:
#print("El valor a pagar por el servicio:",28000)
#print("No ha seleccionado ningun vehiculo")
class reserva_hotel:
    def __init__(self,cr,fecha,valor,habit,dias,nombre,cantidad):
        self.Codigo_Reserva=cr
        self.Fecha_Reserva=fecha
        self.valor_reserva=valor
        self.habitacion=habit
        self.Dias_Reserva=dias
        self.Nombre_Reserva=nombre
        self.Cantidad_Persona=cantidad
        self.datos=()
    
    #Asignando en procedimiento el valor de la habitacion
    def valor_dia_habitacion(self):
        set_valor_reserva = 300000
        print(set_valor_reserva)
    #se va adicionar en la lista el numero de la reserva en el hotel
    def insertar_reserva(self,dato):
        self.datos.append(dato)
    #mostrar los valores de la lista(reserva)
    def mostrar_datos(self):
        print(self.datos)
    #el valor a pagar por la cantidad personas y por la cantidad de dias
    def calcular_dias(self):
        valor=self.valor_dia_habitacion()
        return get_cantidad_reserva(self.get_dias*valor)

def set_codigo_reserva(self,codigo):
    self.Codigo_reserva=codigo

def get_codigo_reserva(self):
    return self.Codigo_reserva

def set_fecha_reserva(self,fecha):
    self.Fecha_Reserva=fecha

def get_fecha_reserva(self):
    return self.Fecha_Reserva

def set_valor_reserva(self,valor):
    self.Valor_Reserva=valor

def get_valor_reserva(self):
    return self.Valor_Reserva

def set_habitacion(self,habit):
    self.Habitacion=habit

def get_haitacion(self):
    return self.Habitacion

def set_dias(self,dias):
    self.Dias_Reserva=dias

def get_dias(self):
    return self.Dias_Reserva

def set_nombre_reserva(self,nombre):
    self.Nombre_Reserva=nombre

def get_nombre_reserva(self):
    return self.Nombre_Reserva

def set_cantidad_reserva(self,cantidad):
    self.Cantidad_Persona=cantidad

def get_cantidad_reserva(self):
    return self.Cantidad_Persona


obj_reserva=reserva_hotel(0,'',0,0,0,'',0)
obj_reserva.valor_dia_habitacion()
set_codigo_reserva=int(input("ingrese el codigo de la reserva: "))
obj_reserva.insertar_reserva(set_codigo_reserva)
set_fecha_reserva=input("ingrese la fecha de la reserva: ")
obj_reserva.insertar_reserva(set_fecha_reserva)
set_dias=int(input("ingrese los dias de la reserva: "))
obj_reserva.insertar_reserva(set_dias)
set_habitacion=int(input("ingresar el numero de la habitacion: "))
obj_reserva.insertar_reserva(set_habitacion)
set_cantidad_reserva=int(input("Ingrese cantidad personas: "))
obj_reserva.insertar_reserva(set_cantidad_reserva)
obj_reserva.mostrar_datos()
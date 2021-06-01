class inmueble:
    
    def __init__(self,referencia,mtc,prec,ubi,tipo):
        self.Referencia = referencia
        self.Metro_cuadrado = mtc
        self.Precio = prec
        self.Ubicacion = ubi
        self.Tipo = tipo
        self.datos=[]

    def insertar_valores(self,valor):
        self.datos=[]
        self.datos.append(valor)
        return self.datos
    def mostrar_valores(self):
        return self.datos
    
def get_Referencia(self):
    return self.Referencia
    
def set_Referencia(self,referencia):
    self.Referencia = referencia

def get_Metro_cuadrado(self):
    return self.Metro_cuadrado
    
def set_Metro_cuadrado(self,mtc):
    self.Metro_cuadrado = mtc

def get_Precio(self):
    return self.Precio
    
def set_Precio(self,precio):
    self.Precio = precio

def get_Ubicacion(self):
    return self.Ubicacion
    
def set_Ubicacion(self,ubi):
    self.Ubicacion = ubi

def get_Tipo(self):
    return self.Tipo
    
def set_Tipo(self,tipo):
    self.Tipo = tipo


obj1=inmueble("",0,0,"","")
centinela="si"
while centinela=="si":
    set_Referencia=int(input("Ingrese la referencia: "))
    obj1.insertar_valores(set_Referencia)
    centinela=input("desea continuar si/no: ")
obj1.mostrar_valores()



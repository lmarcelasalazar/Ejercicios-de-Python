class Matricula:
    
    def __init__(self,matricula,nombre,direccion,telefono,curso):
        self.Codigo_Matricula = matricula
        self.Nombre_Completo = nombre
        self.Direccion = direccion
        self.Telefono = telefono
        self.Curso = curso
        self.datos=[]

    def insertar_valores(self,valor):
        self.datos=[]
        self.datos.append(valor)
        return self.datos
    def mostrar_valores(self):
        return self.datos
    
def get_Codigo_Matricula(self):
    return self.Codigo_Matricula
    
def set_Codigo_Matricula(self,matricula):
    self.Codigo_Matricula = matricula

def get_Nombre_Completo(self):
    return self.Nombre_Completo
    
def set_Nombre_Completo(self,nombre):
    self.Nombre_Completo = nombre

def get_Direccion(self):
    return self.Direccion
    
def set_Direccion(self,direccion):
    self.Direccion = direccion

def get_Telefono(self):
    return self.Telefono
    
def set_Telefono(self,telefono):
    self.Telefono = telefono

def get_Curso(self):
    return self.Curso
    
def set_Curso(self,curso):
    self.Curso = curso


obj1=Matricula(0,"","",0,"")
centinela="si"
while centinela=="si":
    set_Codigo_Matricula=int(input("Ingrese el codigo de matricula: "))
    obj1.insertar_valores(set_Codigo_Matricula)
    set_Nombre_Completo=input("Ingrese el nombre: ")
    obj1.insertar_valores(set_Nombre_Completo)
    set_Direccion=input("Ingrese su direccion: ")
    obj1.insertar_valores(set_Direccion)
    set_Telefono=int(input("Ingrese su telefono: "))
    obj1.insertar_valores(set_Telefono)
    set_Curso=input("Ingrese su curso: ")
    obj1.insertar_valores(set_Curso)
    centinela=input("desea continuar si/no: ")
obj1.mostrar_valores()
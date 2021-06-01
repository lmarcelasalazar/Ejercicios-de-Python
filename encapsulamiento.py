class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.edad

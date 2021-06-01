class persona:

    def __init__(self, identificacion,nombre,apellido,edad):
        self.identificacion=identificacion
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

#Modificar los valores
persona.nombre="Juan"
persona.edad=28

#Acceder a los valores
print(persona.nombre)
print(persona.edad)

#objeto acudiente solo esta utilizando 2 atributos para mostrar
acudiente = persona(10495866,'juan','perez',23)
print(acudiente.nombre)
print(acudiente.edad)
print(id(acudiente))

#objeto empleado utiliza todos atributos de la clase
empleado = persona(10495866,'sara','gomez',23)
print(empleado.nombre)
print(empleado.edad)
print(empleado.identificacion)
print(id(empleado))
        
class Persona :
    nombre = ""
    apellido = ""
    edad = 0

    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def presentacion(self):
        return "Hola soy {} {} tengo {} anios.".format(self.nombre,self.apellido,self.edad) 
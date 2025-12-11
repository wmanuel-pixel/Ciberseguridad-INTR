class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre #publico
        self.__edad = edad #protegido solo accesible desde la clse mkisma.
        self._ocupacion="estudiante" #protegido solo accesible desde la misma terminal

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor > 0:
            self.__edad=valor
        else:
            raise ValueError ("la edad no puede ser negativa o es  invalida")  
    
persona1=persona("wilson",29) 
print(persona1.edad)
persona1.edad=32
print(persona1.edad)
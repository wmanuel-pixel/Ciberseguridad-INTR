class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre #publico
        self.__edad = edad #protegido solo accesible desde la clse mkisma.
        self._ocupacion="estudiante" #protegido solo accesible desde la misma terminal
    def get_edad(self):
        return self.__edad
    def set_edad(self, nueva_edad):
        if nueva_edad >=0:
            self.__edad=nueva_edad
        else:
            print("edad invalida")


#atributo publico
pesona1=persona("wilson",29)
print(pesona1.nombre)

#atributo protegido
print(pesona1._ocupacion)
#atrbuto privado
pesona1.set_edad(32)
print(pesona1.get_edad())


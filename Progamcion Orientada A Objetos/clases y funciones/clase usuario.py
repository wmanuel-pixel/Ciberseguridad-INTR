class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Usuario: {self.nombre}, Edad: {self.edad} años")


user1 = Usuario("wilson", 29)
user1.mostrar_datos()
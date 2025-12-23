class Objeto:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def mostrar_info(self):
        return f"Objeto: {self.nombre}, Valor: {self.valor}"
# Ejemplo de uso
obj = Objeto("Ejemplo", 42) 
print(obj.mostrar_info())
# Salida: Objeto: Ejemplo, Valor: 42


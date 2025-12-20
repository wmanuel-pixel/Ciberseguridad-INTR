#Crea una clase base **Empleado** con atributos nombre y salario. Crea clases hijas como Gerente y Técnico, cada una con un método calcular_bono() diferente.

class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def obtener_detalles(self):
        return f"Empleado: {self.nombre}, Salario Base: ${self.salario_base}"

class Gerente(Empleado):
    def calcular_bono(self):
        # Un gerente recibe 20% de bono
        return self.salario_base * 0.20

class Tecnico(Empleado):
    def calcular_bono(self):
        # Un técnico recibe un bono fijo por productividad
        return 150.0

# Ejemplo de uso
g = Gerente("keydel", 3000)
t = Tecnico("wilson", 1500)

print(f"{g.nombre} tiene un bono de: ${g.calcular_bono()}")
print(f"{t.nombre} tiene un bono de: ${t.calcular_bono()}")
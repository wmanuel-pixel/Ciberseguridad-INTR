class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

# Pedir datos
base = float(input("Base: "))
altura = float(input("Altura: "))

# Crear rectángulo y calcular área
r = Rectangulo(base, altura)
area = r.calcular_area()

# Mostrar resultado
print(f"Área: {area}")
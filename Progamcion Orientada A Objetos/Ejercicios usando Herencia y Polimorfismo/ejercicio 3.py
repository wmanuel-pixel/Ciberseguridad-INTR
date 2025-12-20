#Crea una clase base **Figura** con un método area(). Implementa clases hijas como Círculo y Cuadrado que calculen el área según corresponda.

import math
from abc import ABC, abstractmethod

# 1. Definición de la Clase Base (Abstracta)
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

# 2. Implementación de Círculo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        # Fórmula: $Area = \pi \cdot r^2$
        return math.pi * (self.radio ** 2)

# 3. Implementación de Cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        # Fórmula: $Area = l^2$
        return self.lado ** 2

# --- Lógica de Interacción con el Usuario ---

def menu():
    print("\n--- CALCULADORA DE ÁREAS ---")
    print("1. Calcular área de un Círculo")
    print("2. Calcular área de un Cuadrado")
    print("3. Salir")
    return input("Seleccione una opción (1-3): ")

while True:
    opcion = menu()

    try:
        if opcion == "1":
            r = float(input("Ingrese el radio del círculo: "))
            figura = Circulo(r)
            print(f">> El área del círculo es: {figura.area():.2f}")
        
        elif opcion == "2":
            l = float(input("Ingrese la medida del lado del cuadrado: "))
            figura = Cuadrado(l)
            print(f">> El área del cuadrado es: {figura.area():.2f}")
        
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
            
    except ValueError:
        print("Error: Por favor, ingrese solo valores numéricos.")
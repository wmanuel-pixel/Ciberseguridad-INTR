#Crea una clase **Dispositivo** con un método encender(). Crea clases hijas como Laptop y Teléfono que sobreescriban el comportamiento del método.

class Dispositivo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print(f"Cargando energía en el dispositivo {self.marca}...")

class Laptop(Dispositivo):
    def encender(self):
        super().encender() # Ejecuta la carga de energía del padre
        print("Laptop: Iniciando Sistema Operativo y verificando periféricos.")

class Telefono(Dispositivo):
    def encender(self):
        super().encender()
        print("Teléfono: Buscando señal de red móvil y desbloqueando pantalla.")

# Ejemplo
mi_pc = Laptop("Dell")
mi_movil = Telefono("Samsung")

mi_pc.encender()
print("-" * 20)
mi_movil.encender()
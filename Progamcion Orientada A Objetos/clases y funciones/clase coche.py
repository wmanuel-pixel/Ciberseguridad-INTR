class Coche:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad
        self.color = ""
        self.llantas_modificadas = False
        self.tamano_llantas = 0
        self.bompers = False
        self.nitro = False
        self.musica = False
    
    def acelerar(self, cantidad):
        self.velocidad += cantidad
        return self.velocidad

# Marcas
marcas = ["Honda", "Toyota", "Mazda", "Kia", "Hyundai", "Nissan"]

# Colores
colores = ["Rojo", "Azul", "Negro", "Blanco", "Gris", "Verde", 
           "Amarillo", "Naranja", "Morado", "Rosa", "Café", 
           "Plateado", "Dorado", "Turquesa", "Vino"]

print("Marcas de coche:")
for i, marca in enumerate(marcas, 1):
    print(f"{i}. {marca}")

opcion = int(input("Selecciona número: "))
coche = Coche(marcas[opcion-1])

# Color
print("\nColores disponibles:")
for i, color in enumerate(colores, 1):
    print(f"{i}. {color}")
opcion_color = int(input("Selecciona color (0 para omitir): "))
if opcion_color > 0:
    coche.color = colores[opcion_color-1]

# Llantas modificadas
llantas = input("\n¿Llantas modificadas? (s/n): ").lower()
if llantas == 's':
    coche.llantas_modificadas = True
    tamano = int(input("Tamaño llantas (20-22): "))
    coche.tamano_llantas = tamano if 20 <= tamano <= 22 else 20

# Extras
extras = ["Bompers", "Nitro", "Sistema de música"]
for extra in extras:
    respuesta = input(f"\n¿Añadir {extra}? (s/n): ").lower()
    if extra == "Bompers" and respuesta == 's':
        coche.bompers = True
    elif extra == "Nitro" and respuesta == 's':
        coche.nitro = True
    elif extra == "Sistema de música" and respuesta == 's':
        coche.musica = True

# Aceleración
cantidad = int(input("\n¿Cuánto acelerar? (km/h): "))
velocidad_final = coche.acelerar(cantidad)

# Descripción final
print("\n" + "="*40)
print("DESCRIPCIÓN FINAL DEL COCHE")
print("="*40)
print(f"Marca: {coche.marca}")
print(f"Color: {coche.color if coche.color else 'Sin especificar'}")
print(f"Llantas modificadas: {'Sí' if coche.llantas_modificadas else 'No'}")
if coche.llantas_modificadas:
    print(f"Tamaño llantas: {coche.tamano_llantas}")
print(f"Bompers: {'Sí' if coche.bompers else 'No'}")
print(f"Nitro: {'Sí' if coche.nitro else 'No'}")
print(f"Sistema de música: {'Sí' if coche.musica else 'No'}")
print(f"Velocidad: {velocidad_final} km/h")
print("="*40)
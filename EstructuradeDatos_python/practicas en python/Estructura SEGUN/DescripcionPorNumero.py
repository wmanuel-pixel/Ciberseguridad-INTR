#
# 
opcion = input("Ingrese un número del 1 al 3: ")

print("\n--- Resultado ---")
# La entrada se toma como string (texto) y se compara con strings
match opcion:
    case "1":
        print("¡Hola! bienvenido a tu curso de Redes y Telecomunicaciones.")
    case "2":
        print("Bienvenido a Tu Curso De Ciberseguridad Informatica.")
    case "3":
        print("¡Flicidades eres tecnico progrador de INFOTEP.")
    case _:
        print("Opción **fuera de rango**. Intenta con 1, 2 o 3.")

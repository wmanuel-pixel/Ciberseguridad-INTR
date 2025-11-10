# Programa para validar edades entre 0 y 120 años
edad = None
continuar = True
ultimo_valido = None

print("--- Verificador de Rango de Edad (0-120) ---")

while continuar:
    try:
        entrada = input("\nIngrese una edad (0-120) o un número negativo para salir: ").strip()
        if entrada == "":
            print("Error: entrada vacía. Intente de nuevo.")
            continue

        edad = int(entrada)

        if edad < 0:
            continuar = False
            print("\nHa elegido salir del programa.")
        elif 0 <= edad <= 120:
            ultimo_valido = edad
            print(f"Edad válida: {edad} años")
            if edad >= 18:
                print("Esta persona es mayor de edad.")
            else:
                print("Esta persona es menor de edad.")
        else:
            print(f"Error: {edad} está fuera del rango permitido (0-120)")

    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")

# Mensaje de finalización
print("\n--- Proceso Terminado ---")
if ultimo_valido is not None:
    print(f"Última edad válida ingresada: {ultimo_valido}")
else:
    print("No se ingresó ninguna edad válida.")
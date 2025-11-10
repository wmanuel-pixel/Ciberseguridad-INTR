# Nombrar los días de la semana según un número ingresado por el usuario.
numero_dia = int(input("Ingrese un número de día (1=Lunes, 7=Domingo): "))

print("\n--- Resultado ---")
match numero_dia:
    case 1:
        print("El día es **Lunes**.")
    case 2:
        print("El día es **Martes**.")
    case 3:
        print("El día es **Miércoles**.")
    case 4:
        print("El día es **Jueves**.")
    case 5:
        print("El día es **Viernes**.")
    case 6:
        print("El día es **Sábado**.")
    case 7:
        print("El día es **Domingo**.")
    case _:
        print("Error: Número de día **inválido**. Debe ser entre 1 y 7.")

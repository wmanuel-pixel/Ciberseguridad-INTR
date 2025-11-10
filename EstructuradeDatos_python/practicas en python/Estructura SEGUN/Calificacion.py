# Calificación de rendimiento basado en la letra ingresada.
calificacion = input("Ingrese la calificación (A, B, C, D o F): ").upper()

print("\n--- Resultado ---")
match calificacion:
    case "A":
        print("Rendimiento: **Excelente**.")
    case "B":
        print("Rendimiento: **Bueno**.")
    case "C":
        print("Rendimiento: **Satisfactorio**.")
    case "D":
        print("Rendimiento: **Necesita mejorar**.")
    case "F":
        print("Rendimiento: **Reprobado**.")
    case _:
        print("Error: Calificación **no reconocida**.")

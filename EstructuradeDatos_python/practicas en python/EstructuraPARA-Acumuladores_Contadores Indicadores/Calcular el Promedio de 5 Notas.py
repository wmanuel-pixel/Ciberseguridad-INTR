# 
NUMERO_NOTAS = 5
suma_notas = 0.0 # Acumulador para la suma de las notas

print(f"--- Cálculo de Promedio de {NUMERO_NOTAS} Notas ---")

# El ciclo se repite 5 veces (i tomará valores 0, 1, 2, 3, 4)
for i in range(NUMERO_NOTAS):
    while True:
        try:
            # i + 1 se usa solo para el mensaje de la nota actual (1, 2, 3, 4, 5)
            nota = float(input(f"Ingrese la nota #{i + 1}: "))
            if 0 <= nota <= 100:
                suma_notas += nota  # Acumulamos la nota
                break
            else:
                print("Nota fuera de rango (0-100). Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

# Cálculo final del promedio
promedio = suma_notas / NUMERO_NOTAS

print("\n--- Resultado ---")
print(f"La suma total de las notas es: {suma_notas:.2f}")
print(f"El promedio es: {promedio:.2f}")
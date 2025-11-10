# 
# Inicializamos la variable de la suma acumulada
suma_total = 0

print("--- Acumulador (Hasta superar 100) ---")

# El bucle continúa mientras la suma no supere el límite de 100
while suma_total <= 100:
    try:
        numero = float(input(f"Suma actual: {suma_total}. Ingrese un número a sumar: "))
        suma_total += numero
        print(f"Nuevo total acumulado: {suma_total}")
        
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")
        
print("\n--- Proceso Terminado ---")
print(f"La suma ({suma_total}) **superó el límite de 100** y el bucle ha terminado.")
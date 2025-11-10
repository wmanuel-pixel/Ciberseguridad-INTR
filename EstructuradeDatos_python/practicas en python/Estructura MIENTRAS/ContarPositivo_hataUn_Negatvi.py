# 
# Inicializamos el contador de positivos.
contador_positivos = 0
numero_actual = 0 # Inicializado en 0 para entrar al bucle

print("--- Contador de Positivos (Ingresa un negativo para terminar) ---")

while numero_actual >= 0:
    # Solicitamos el número dentro del ciclo
    numero_actual = int(input("Ingrese un número: "))
    
    # Solo contamos si el número es POSITIVO
    if numero_actual >= 0:
        contador_positivos += 1

print("\n--- Resultado ---")
# Restamos 1 al contador porque el último número (el negativo) no debe contarse como positivo.
# Si el usuario ingresa un negativo primero, el resultado será 0 (0-1 = -1, pero max(0, -1) = 0)
total_positivos = max(0, contador_positivos - 1)
print(f"Se ingresaron {total_positivos} números positivos.")
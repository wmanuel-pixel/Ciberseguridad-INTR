# leer números hasta que se ingrese un número negativo.

contador_positivos = 0

print("--- Contador de Positivos (Ingresa un negativo para terminar) ---")

while True:
    try:
        numero = float(input("Ingrese un número: "))
        
        # Condición HASTA QUE: Si el número es negativo (< 0), terminamos (BREAK)
        if numero < 0:
            break
            
        # Si el número es positivo (>= 0), lo contamos
        if numero >= 0:
            contador_positivos += 1
            
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")

print("\n--- Resultado Final ---")
print(f"Se ingresaron {contador_positivos} números no negativos.")
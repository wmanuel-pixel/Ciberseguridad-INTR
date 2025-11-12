# 
suma_total = 0
contador_numeros = 0

print("--- Sumador (Ingresa 0 para finalizar) ---")

while True:
    try:
        numero = float(input("Ingrese un número: "))
        
        # Condición HASTA QUE: Si el número es 0, terminamos (BREAK)
        if numero == 0:
            break
            
        # Si no es 0, sumamos y contamos
        suma_total += numero
        contador_numeros += 1
        print(f"Suma actual: {suma_total}")
        
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")
        
print("\n--- Resultado Final ---")
print(f"Total de números ingresados (sin contar el 0): **{contador_numeros}**")
print(f"Suma final acumulada: **{suma_total}**")
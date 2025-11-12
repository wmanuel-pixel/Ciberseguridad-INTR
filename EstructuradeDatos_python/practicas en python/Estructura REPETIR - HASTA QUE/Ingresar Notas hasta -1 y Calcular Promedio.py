# 
suma_notas = 0
cantidad_notas = 0

print("--- Calculador de Promedio (Ingresa -1 para finalizar) ---")

while True:
    try:
        nota = float(input("Ingrese una nota (o -1 para terminar): "))
        
        # Condición HASTA QUE: Si la nota es -1, terminamos (BREAK)
        if nota == -1:
            break
            
        # Solo procesamos notas válidas (opcionalmente entre 0 y 100)
        if nota >= 0: 
            suma_notas += nota
            cantidad_notas += 1
        else:
             print("Nota ignorada. Solo se procesan notas positivas.")

    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")
        
print("\n--- Resultado Final ---")

if cantidad_notas > 0:
    promedio = suma_notas / cantidad_notas
    print(f"Total de notas válidas: {cantidad_notas}")
    print(f"Promedio de las notas: **{promedio:.2f}**")
else:
    print("No se ingresaron notas válidas para calcular el promedio.")
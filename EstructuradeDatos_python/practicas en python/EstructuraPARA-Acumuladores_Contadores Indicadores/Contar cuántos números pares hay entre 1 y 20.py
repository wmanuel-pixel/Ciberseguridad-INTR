# 
LIMITE = 20
contador_pares = 0 # Contador para números pares

print(f"--- Conteo de Números Pares entre 1 y {LIMITE} ---")

# Iteramos sobre todos los números del 1 al 20
for i in range(1, LIMITE + 1):
    # Condición de Par: el residuo de la división entre 2 es 0
    if i % 2 == 0:
        contador_pares += 1 # Contamos el número par
        print(f"Par encontrado: {i}")

print("\n--- Resultado ---")
print(f"Hay un total de {contador_pares} números pares entre 1 y 20.")
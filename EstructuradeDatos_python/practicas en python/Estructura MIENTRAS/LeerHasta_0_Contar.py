# 
# Inicializamos el contador y la variable para el número ingresado.
contador_numeros = 0
numero_ingresado = -1 # Se inicializa diferente de 0 para entrar en el bucle

print("--- Contador de Números (Ingresa 0 para terminar) ---")

while numero_ingresado != 0:
    # Solicitamos el número DENTRO del bucle
    numero_ingresado = int(input("Ingrese un número: "))
    
    # Verificamos si es diferente de 0 para contarlo
    if numero_ingresado != 0:
        contador_numeros += 1

print("\n--- Resultado ---")
print(f"Se ingresaron **{contador_numeros} números** antes de terminar.")

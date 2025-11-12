# 
LIMITE_CUADRADOS = 10

print(f"--- Cuadrados de los Números del 1 al {LIMITE_CUADRADOS} ---")

# Iteramos del 1 al 10
for i in range(1, LIMITE_CUADRADOS + 1):
    cuadrado = i ** 2
    print(f"El cuadrado de {i:2} es {cuadrado:3}")

# sumar los números del 1 al 50 usando un acumulador.

LIMITE_SUPERIOR = 50
suma_total = 0 # Acumulador

print(f"--- Suma de Números del 1 al {LIMITE_SUPERIOR} ---")

# El ciclo va de 1 (incluido) a 51 (excluido), para incluir el 50
for i in range(1, LIMITE_SUPERIOR + 1):
    suma_total += i # Acumulación

print("\n--- Resultado ---")
print(f"La suma de los números del 1 al 50 es: **{suma_total}**")

# Nota: Para verificar, la fórmula de la suma de Gauss es: n * (n+1) / 2
# suma_gauss = 50 * 51 / 2 = 1275
# Calcular el Factorial de un Número.

try:
    numero_original = int(input("Ingrese un número entero positivo para calcular su factorial: "))
except ValueError:
    print("Entrada inválida.")
else:
    if numero_original < 0:
        print("El factorial solo se define para números no negativos.")
    else:
        # 0! y 1! es 1
        if numero_original == 0 or numero_original == 1:
            factorial = 1
        else:
            # Inicializamos para el ciclo
            factorial = 1
            contador = 1
            
            while True:
                factorial *= contador
                contador += 1
                
                # Condición HASTA QUE: El contador supera el número original
                if contador > numero_original:
                    break

        print(f"El factorial de {numero_original} es: {factorial}")
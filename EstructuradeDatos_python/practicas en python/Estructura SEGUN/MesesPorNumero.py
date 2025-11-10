# 
numero_mes = int(input("Ingrese un número de mes (1 al 12): "))

print("\n--- Resultado ---")
match numero_mes:
    case 1:
        print("El mes es **Enero**.")
    case 2:
        print("El mes es **Febrero**.")
    case 3:
        print("El mes es **Marzo**.")
    case 4:
        print("El mes es **Abril**.")
    case 5:
        print("El mes es **Mayo**.")
    case 6:
        print("El mes es **Junio**.")
    case 7:
        print("El mes es **Julio**.")
    case 8:
        print("El mes es **Agosto**.")
    case 9:
        print("El mes es **Septiembre**.")
    case 10:
        print("El mes es **Octubre**.")
    case 11:
        print("El mes es **Noviembre**.")
    case 12:
        print("El mes es **Diciembre**.")
    case _: # El caso '_" actúa como el "DE OTRO MODO" o "SINO"
        print("Error: Número de mes **inválido**. Debe ser entre 1 y 12.")
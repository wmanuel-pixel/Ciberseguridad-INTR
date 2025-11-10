# 
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

resultado = None

match operacion:
    case "+":
        resultado = num1 + num2
        print(f"\nSuma: {num1} + {num2} = {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"\nResta: {num1} - {num2} = {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"\nMultiplicación: {num1} * {num2} = {resultado}")
    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nDivisión: {num1} / {num2} = {resultado}")
        else:
            print("\nError: **División por cero no permitida**.")
    case _:
        print("\nError: **Operación inválida**.")
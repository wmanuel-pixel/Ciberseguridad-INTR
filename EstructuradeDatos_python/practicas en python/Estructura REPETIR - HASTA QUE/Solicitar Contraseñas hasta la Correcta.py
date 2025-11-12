# 
CLAVE_CORRECTA = '~!@#$%^&*()'
clave_ingresada = ''

print("--- Verificación de Contraseña ---")

while True:
    clave_ingresada = input("Ingrese la contraseña: ")
    
    # Condición HASTA QUE: Si la clave es correcta, terminamos (BREAK)
    if clave_ingresada == CLAVE_CORRECTA:
        print("\n¡**Acceso concedido**! Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta. Intente de nuevo.")
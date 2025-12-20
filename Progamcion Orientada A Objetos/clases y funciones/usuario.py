class CuentaBancaria:
    def __init__(self, titular, balance=0):
        self.titular = titular
        self.balance = balance

usuarios = {
    "wilson": {"id": "0000", "fecha_nac": "20-09-1996", "tok": "wil00"},
    "karla": {"id": "1111", "fecha_nac": "09-01-2002", "tok": "kar11"},
    "carina": {"id": "2222", "fecha_nac": "14-02-2002", "tok": "car22"},
    "carolina": {"id": "3333", "fecha_nac": "01-08-2002", "tok": "car33"}
}

print("=== BANCO DIGITAL ===")

# Verificar usuario
nombre = input("Nombre: ").lower()

if nombre in usuarios:
    id_usuario = input("ID: ")
    
    if id_usuario == usuarios[nombre]["id"]:
        # Crear cuenta con balance inicial de 1000
        cuenta = CuentaBancaria(nombre, 1000)
        print(f"\nBienvenido {nombre.capitalize()}!")
        print(f"Balance inicial: ${cuenta.balance}")
        
        # Primera opción de depósito/retiro
        print("\n=== OPERACIÓN INICIAL ===")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Solo ver balance")
        
        opcion = input("Seleccione opción (1-3): ")
        
        if opcion == "1":
            try:
                monto = float(input("Monto a depositar: $"))
                cuenta.balance += monto
                print(f"Depositado: ${monto}")
                print(f"Nuevo balance: ${cuenta.balance}")
            except:
                print("Error: monto inválido")
                
        elif opcion == "2":
            print("\n=== VERIFICACIÓN PARA RETIRO ===")
            fecha = input("Fecha de nacimiento (dd-mm-aaaa): ")
            tok = input("Toki: ")
            
            if fecha == usuarios[nombre]["fecha_nac"] and tok == usuarios[nombre]["tok"]:
                try:
                    monto = float(input("Monto a retirar: $"))
                    if monto <= cuenta.balance:
                        cuenta.balance -= monto
                        print(f"Retirado: ${monto}")
                        print(f"Nuevo balance: ${cuenta.balance}")
                    else:
                        print("Error: fondos insuficientes")
                except:
                    print("Error: monto inválido")
            else:
                print("Error: verificación fallida")
        
        elif opcion == "3":
            print(f"Balance actual: ${cuenta.balance}")
        
        # Opción final antes de salir
        print("\n=== ¿OPERACIÓN FINAL? ===")
        print("1. Hacer depósito final")
        print("2. Hacer retiro final")
        print("3. Salir sin más operaciones")
        
        final_opcion = input("Seleccione opción (1-3): ")
        
        if final_opcion == "1":
            try:
                monto = float(input("Monto a depositar: $"))
                cuenta.balance += monto
                print(f"Depositado: ${monto}")
            except:
                print("Error: monto inválido")
                
        elif final_opcion == "2":
            print("\n=== VERIFICACIÓN FINAL ===")
            fecha = input("Fecha de nacimiento (dd-mm-aaaa): ")
            tok = input("Toki: ")
            
            if fecha == usuarios[nombre]["fecha_nac"] and tok == usuarios[nombre]["tok"]:
                try:
                    monto = float(input("Monto a retirar: $"))
                    if monto <= cuenta.balance:
                        cuenta.balance -= monto
                        print(f"Retirado: ${monto}")
                    else:
                        print("Error: fondos insuficientes")
                except:
                    print("Error: monto inválido")
            else:
                print("Error: verificación fallida")
        
        print(f"\n=== RESUMEN FINAL ===")
        print(f"Titular: {nombre.capitalize()}")
        print(f"Balance final: ${cuenta.balance}")
        print("¡Gracias por usar Banco Digital!")
        
    else:
        print("Error: ID incorrecto")
else:
    print("Error: Usuario no encontrado")
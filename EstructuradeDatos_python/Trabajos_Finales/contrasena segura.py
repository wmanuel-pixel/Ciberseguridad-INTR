import string
import hashlib

# --- Almacenamiento ---
# Usaremos un diccionario para mapear usuario -> contraseña (hashed)
# Evita listas paralelas y facilita búsquedas por nombre de usuario
usuarios = {}

# Contraseñas específicas obligatorias para ciertos usuarios (en texto aquí
# pero las guardaremos hashed). Estos usuarios están pre-registrados.
predefinidos = {
    "Karla01": "@k@rl@$$1234",
    "wilson01": "@wils@n$$1234",
    "Keydel01": "@Keydel$$1234",
}

# Registrar los usuarios predefinidos (hasheando las contraseñas)
for u, pw in predefinidos.items():
    usuarios[u] = hashlib.sha256(pw.encode("utf-8")).hexdigest()

# --- Contraseñas especiales obligatorias para ciertos usuarios ---
# Si el usuario está en este diccionario, solo se aceptará exactamente
# la contraseña especificada aquí (comprobación literal).
SPECIAL_PASSWORDS = {
    "Karla01": "@k@rl@$$1234",
    "wilson01": "@wils@n$$1234",
    "Keydel01": "@Keydel$$1234",
}

# --- Funciones de Lógica ---

def verificar_contraseña(password):
    """Revisa si la contraseña cumple con los mínimos de seguridad."""
    
    # Mínimo 8 caracteres
    if len(password) < 8:
        return False

    # Banderas
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    # Itera sobre cada carácter para verificar los tipos
    for char in password:
        if char in string.ascii_uppercase:
            has_upper = True
        elif char in string.ascii_lowercase:
            has_lower = True
        elif char in string.digits:
            has_digit = True
        elif char in string.punctuation:
            has_symbol = True
            
    # La contraseña es fuerte solo si todas las banderas se activaron
    return has_upper and has_lower and has_digit and has_symbol


def generar_alertas(password):
    """Muestra qué criterios fallaron."""
    print("\n[ALERTA] Contraseña débil por las siguientes razones:")

    if len(password) < 8:
        print("- Longitud: Debe tener al menos 8 caracteres.")
    
    # Uso de any() para simplificar las verificaciones
    if not any(c in string.ascii_uppercase for c in password):
        print("- Faltan letras MAYÚSCULAS.")
    if not any(c in string.ascii_lowercase for c in password):
        print("- Faltan letras MINÚSCULAS.")
    if not any(c in string.digits for c in password):
        print("- Faltan DÍGITOS (números).")
    if not any(c in string.punctuation for c in password):
        print("- Faltan SÍMBOLOS (como !, @, #).")


def registrar_usuario(user, password):
    """Intenta registrar un nuevo usuario."""
    # Verificar si el usuario ya existe
    if user in usuarios:
        print(f"\n[FALLO] El usuario '{user}' ya está registrado.")
        return

    # Si el usuario es uno de los especiales, exigir la contraseña exacta
    if user in SPECIAL_PASSWORDS:
        required = SPECIAL_PASSWORDS[user]
        if password == required:
            # Aceptar incluso si la verificación general fallara (pero aún puede pasarse por verificar si se desea)
            hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
            usuarios[user] = hashed
            print(f"\n[ÉXITO] Usuario especial '{user}' registrado con éxito (contraseña obligatoria correcta).")
        else:
            print(f"\n[FALLO] Contraseña incorrecta para el usuario especial '{user}'.")
        return

    # Para usuarios normales, aplicar reglas de seguridad
    if verificar_contraseña(password):
        # Guardamos la contraseña hasheada (no en claro)
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        usuarios[user] = hashed
        print(f"\n[ÉXITO] Usuario '{user}' registrado con éxito.")
    else:
        # Si es False, genera las alertas
        print(f"\n[FALLO] No se pudo registrar a '{user}'.")
        generar_alertas(password)

# --- Registro interactivo ---
# Ahora el script pedirá al usuario un nombre y luego la contraseña.
if __name__ == "__main__":
    import getpass

    def menu():
        print("\n--- Menú ---")
        print("1) Iniciar sesión")
        print("2) Crear nuevo usuario")
        print("q) Salir")

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip().lower()

        if opcion == 'q':
            print("Saliendo...")
            break

        if opcion == '1':
            # Login
            usuario = input("Ingrese nombre de usuario: ").strip()
            if usuario not in usuarios:
                print("\nEl usuario no existe.")
                continue

            max_intentos = 3
            intentos = 0
            autenticado = False
            while intentos < max_intentos and not autenticado:
                contraseña = getpass.getpass(f"Ingrese contraseña (intento {intentos+1}/{max_intentos}): ")
                hashed = hashlib.sha256(contraseña.encode('utf-8')).hexdigest()
                if hashed == usuarios.get(usuario):
                    print(f"\n[ÉXITO] Acceso concedido. Bienvenido/a, {usuario}.")
                    autenticado = True
                else:
                    intentos += 1
                    print(f"Contraseña incorrecta. Intentos restantes: {max_intentos - intentos}")

            if not autenticado:
                print(f"\n[FALLO] Acceso denegado. Se alcanzó el número máximo de intentos ({max_intentos}).")

        elif opcion == '2':
            # Crear nuevo usuario (registro)
            nuevo_user = input("Ingrese nombre de usuario a crear: ").strip()
            if nuevo_user in usuarios:
                print(f"\n[FALLO] El usuario '{nuevo_user}' ya existe.")
                continue

            # Si el usuario es uno de los especiales ya en SPECIAL_PASSWORDS y
            # está predefinido, informar que no se puede crear (ya existe en predefinidos).
            if nuevo_user in SPECIAL_PASSWORDS:
                print(f"\n[FALLO] El nombre '{nuevo_user}' está reservado/predefinido y no puede ser creado aquí.")
                continue

            max_intentos = 3
            intentos = 0
            creado = False
            while intentos < max_intentos and not creado:
                pw = getpass.getpass(f"Ingrese contraseña para '{nuevo_user}' (intento {intentos+1}/{max_intentos}): ")
                if verificar_contraseña(pw):
                    registrar_usuario(nuevo_user, pw)
                    creado = True
                else:
                    generar_alertas(pw)
                    intentos += 1
                    if intentos < max_intentos:
                        print("Por favor, ingrese una contraseña más fuerte.")

            if not creado:
                print(f"\n[FALLO] No se creó el usuario. Se alcanzó el número máximo de intentos ({max_intentos}).")

        else:
            print("Opción no reconocida. Intente de nuevo.")

    # Estado final
    print("\n--- Estado Final ---")
    if usuarios:
        print("Usuarios en el sistema:")
        for u in usuarios:
            print(" -", u)
    else:
        print("No hay usuarios registrados.")
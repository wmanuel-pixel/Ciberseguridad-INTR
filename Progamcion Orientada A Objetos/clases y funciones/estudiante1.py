class Estudiante:
    def __init__(self, nombre, id_estudiante, materia):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.materia = materia
        self.calificaciones = []
    
    def agregar_calificacion(self, nota):
        self.calificaciones.append(nota)
    
    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def verificar_aprobacion(self):
        promedio = self.calcular_promedio()
        return promedio >= 70, promedio

# Lista de estudiantes con sus IDs
estudiantes = {
    "wilson": "W1235",
    "manuel": "M1235", 
    "keydel": "K1235",
    "karla": "KA1235",
    "carolina": "C1235",
    "carina": "CA1235",
    "scarlett": "S1235",
    "karen": "K1235"
}

# Lista de materias
materias = ["Física", "Matemática", "Lengua Española", "Historia", 
            "Biología", "Filosofía", "Inglés", "Religión"]

print("=== SISTEMA DE CALIFICACIONES ===")

# No mostrar nombres al inicio - solo pedir ID
id_ingresado = input("Ingrese su ID de estudiante: ")

# Buscar estudiante por ID
estudiante_encontrado = None
nombre_estudiante = None

for nombre, id_est in estudiantes.items():
    if id_est == id_ingresado:
        estudiante_encontrado = id_est
        nombre_estudiante = nombre
        break

if estudiante_encontrado:
    # Mostrar materias disponibles
    print(f"\nMaterias disponibles:")
    for i, materia in enumerate(materias, 1):
        print(f"{i}. {materia}")
    
    # Seleccionar materia
    while True:
        try:
            opcion_materia = int(input("\nSeleccione el número de la materia: "))
            if 1 <= opcion_materia <= len(materias):
                materia_seleccionada = materias[opcion_materia-1]
                break
            else:
                print(f"Error: seleccione un número entre 1 y {len(materias)}")
        except ValueError:
            print("Error: ingrese un número válido")
    
    # Crear estudiante
    estudiante = Estudiante(nombre_estudiante.title(), id_ingresado, materia_seleccionada)
    
    # Ingresar 3 calificaciones
    print(f"\n=== INGRESAR CALIFICACIONES PARA {materia_seleccionada.upper()} ===")
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Ingrese la nota #{i} (0-100): "))
                if 0 <= nota <= 100:
                    estudiante.agregar_calificacion(nota)
                    break
                else:
                    print("Error: la nota debe estar entre 0 y 100")
            except ValueError:
                print("Error: ingrese un número válido")
    
    # Calcular resultados
    aprobado, promedio = estudiante.verificar_aprobacion()
    
    # Mostrar resultados
    print("\n" + "="*40)
    print("RESULTADOS ACADÉMICOS")
    print("="*40)
    print(f"Estudiante: {estudiante.nombre}")
    print(f"ID: {estudiante.id_estudiante}")
    print(f"Materia: {estudiante.materia}")
    print(f"Calificaciones: {', '.join([str(n) for n in estudiante.calificaciones])}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {'APROBADO' if aprobado else 'REPROBADO'}")
    print("="*40)
    
    # Mensaje adicional
    if aprobado:
        print(" ¡Felicidades! Has aprobado la materia.")
    else:
        print(" Necesitas mejorar. Estudia más para la próxima.")
else:
    print("Error: ID no encontrado en el sistema.")
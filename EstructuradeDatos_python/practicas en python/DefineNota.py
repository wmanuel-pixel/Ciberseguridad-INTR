# Definir la nota de aprobación
nota_aprobacion = 70.0
nota = float(input("Ingrese la nota del estudiante: "))

if nota >= nota_aprobacion:
    print("El estudiante **aprueba**.")
else:
    print("El estudiante **reprueba**.")
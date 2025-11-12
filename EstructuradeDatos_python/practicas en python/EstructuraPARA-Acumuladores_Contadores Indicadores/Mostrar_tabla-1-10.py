

""" Imprime las tablas de multiplicación del 1 al 10 (del 1x1 al 10x10)."""

def imprimir_tablas(inicio=1, fin=10):
    """Imprime las tablas de multiplicar desde `inicio` hasta `fin` (inclusive).

    Parámetros:
    - inicio: primer multiplicador (por defecto 1)
    - fin: último multiplicador (por defecto 10)
    """
    for i in range(inicio, fin + 1):
        print(f"Tabla del {i}:")
        for j in range(1, 11):
            print(f"  {i} x {j:2} = {i * j}")
        print("" )  # línea en blanco entre tablas


if __name__ == "__main__":
    imprimir_tablas(1, 10)
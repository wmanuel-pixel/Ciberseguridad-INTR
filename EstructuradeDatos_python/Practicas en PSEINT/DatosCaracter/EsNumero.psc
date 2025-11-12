Algoritmo EsNumero
    Definir caracter Como Caracter
    Definir es_numero Como Logico
    
    Escribir "Ingrese un carácter:"
    Leer caracter
    
    es_numero <- (caracter >= "0" Y caracter <= "9")
    Escribir "¿Es un número? ", es_numero
FinAlgoritmo
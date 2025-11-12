Algoritmo CompararNumeros
    Definir num1, num2 Como Entero
    
    Escribir "Ingrese el primer número entero:"
    Leer num1
    
    Escribir "Ingrese el segundo número entero:"
    Leer num2
    
    Si num1 > num2 Entonces
        Escribir num1, " es mayor que ", num2
    Sino
        Si num2 > num1 Entonces
            Escribir num2, " es mayor que ", num1
        Sino
            Escribir "Los números son iguales"
        FinSi
    FinSi
FinAlgoritmo
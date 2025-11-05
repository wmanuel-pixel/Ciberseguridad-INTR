Algoritmo ValorAbsoluto
    Definir num, abs Como Real
    Escribir "Ingrese un número real:"
    Leer num
    Si num < 0 Entonces
        abs <- num * -1
    Sino
        abs <- num
    FinSi
    Escribir "El valor absoluto de ", num, " es: ", abs
FinAlgoritmo

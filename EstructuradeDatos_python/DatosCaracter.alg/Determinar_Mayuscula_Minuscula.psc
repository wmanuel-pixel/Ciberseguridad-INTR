Algoritmo Determinar_Mayuscula_Minuscula
    // Definir la variable como Caracter
    Definir caracter_ingresado Como Caracter;
    
    // Solicitar la entrada
    Escribir "Ingrese un caracter (letra):";
    Leer caracter_ingresado;
    
    // Comparar el caracter con su versión en mayúsculas
    Si caracter_ingresado = MAYUSCULAS(caracter_ingresado) Entonces
        // Se asume que si es igual a su mayúscula, es una mayúscula
        // o un caracter que no cambia (como un número, pero se espera una letra).
        // Para ser más precisos, se puede añadir una comprobación de que sea una letra.
        Escribir "El caracter ", caracter_ingresado, " es MAYÚSCULA.";
    Sino
        // Si no es igual a su mayúscula, es una minúscula
        Escribir "El caracter ", caracter_ingresado, " es MINÚSCULA.";
    FinSi
    
FinAlgoritmo
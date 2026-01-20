-- 1. Reiniciar la base de datos
DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca;
USE biblioteca;

-- 2. Crear tabla de autores
CREATE TABLE autores (
    autor_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50)
);

-- 3. Crear tabla de libros
CREATE TABLE libros (
    libro_id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    anio_publicacion INT,
    autor_id INT,
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id)
);

-- 4. Insertar los autores
INSERT INTO autores (nombre, nacionalidad) VALUES ('James Clear', 'Estadounidense');
INSERT INTO autores (nombre, nacionalidad) VALUES ('Robert Kiyosaki', 'Estadounidense');
INSERT INTO autores (nombre, nacionalidad) VALUES ('Paulo Coelho', 'Brasileño');
INSERT INTO autores (nombre, nacionalidad) VALUES ('Miguel de Cervantes', 'Español');

-- 5. Insertar todos los libros
INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES ('Hábitos Atómicos', 2018, 1);
INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES ('Padre Rico, Padre Pobre', 1997, 2);
INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES ('11 Minutos', 2003, 3);
INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES ('El Alquimista', 1988, 3);
INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES ('Don Quijote de la Mancha', 1605, 4);

-- 6. Consulta final organizada por autor
SELECT 
    libros.titulo AS 'Libro', 
    autores.nombre AS 'Autor',
    autores.nacionalidad AS 'Nacionalidad'
FROM libros
JOIN autores ON libros.autor_id = autores.autor_id
ORDER BY autores.nombre;
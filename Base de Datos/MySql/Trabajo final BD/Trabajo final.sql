-- 1. CREACIÓN DE LA BASE DE DATOS
DROP DATABASE IF EXISTS gestion_academica;
CREATE DATABASE gestion_academica;
USE gestion_academica;

-- 2. CREACIÓN DE TABLAS (Diferenciando Claves Primarias y Foráneas)

CREATE TABLE Departamentos (
    depto_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Profesores (
    profesor_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    depto_id INT,
    FOREIGN KEY (depto_id) REFERENCES Departamentos(depto_id)
);

CREATE TABLE Estudiantes (
    estudiante_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    depto_id INT,
    FOREIGN KEY (depto_id) REFERENCES Departamentos(depto_id)
);

CREATE TABLE Cursos (
    curso_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100) NOT NULL,
    creditos INT
);

CREATE TABLE Clases (
    clase_id INT AUTO_INCREMENT PRIMARY KEY,
    curso_id INT,
    profesor_id INT,
    horario VARCHAR(50),
    FOREIGN KEY (curso_id) REFERENCES Cursos(curso_id),
    FOREIGN KEY (profesor_id) REFERENCES Profesores(profesor_id)
);

CREATE TABLE Inscripciones (
    inscripcion_id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    clase_id INT,
    fecha_inscripcion DATE,
    FOREIGN KEY (estudiante_id) REFERENCES Estudiantes(estudiante_id),
    FOREIGN KEY (clase_id) REFERENCES Clases(clase_id)
);

CREATE TABLE Calificaciones (
    calificacion_id INT AUTO_INCREMENT PRIMARY KEY,
    inscripcion_id INT,
    nota DECIMAL(5,2),
    FOREIGN KEY (inscripcion_id) REFERENCES Inscripciones(inscripcion_id)
);

-- 3. INSERCIÓN DE DATOS (Manipulación de Datos)
INSERT INTO Departamentos (nombre) VALUES ('Ciencias'), ('Letras'), ('Tecnología');

INSERT INTO Profesores (nombre, apellido, depto_id) VALUES 
('CARLOS', 'GARCIAS', 1), 
('RAFAEL', 'DE LEON', 3);

INSERT INTO Estudiantes (nombre, apellido, fecha_nacimiento, depto_id) VALUES 
('Carlos', 'perez', '2000-05-15', 3),
('Nedual', 'Vargas', '1998-11-20', 3),
('Wilson', 'Manuel', '2002-01-10', 1),
('Alexandra', 'Santos', '2001-07-22', 2),
('Geudys', 'Quiroz', '1995-03-30', 1);

INSERT INTO Cursos (nombre_curso, creditos) VALUES ('Base de Datos I', 4), ('Cálculo I', 5);

INSERT INTO Clases (curso_id, profesor_id, horario) VALUES (1, 2, 'Lunes 18:00'), (2, 1, 'Martes 10:00');

INSERT INTO Inscripciones (estudiante_id, clase_id, fecha_inscripcion) VALUES (1, 1, '2026-01-20'), (2, 1, '2026-01-20');

INSERT INTO Calificaciones (inscripcion_id, nota) VALUES (1, 95.5), (2, 88.0);

-- 4. CONSULTAS, JOINS Y ESTADÍSTICAS

-- A. Consultar todos los estudiantes y su departamento (JOIN)
SELECT e.nombre, e.apellido, d.nombre AS Departamento
FROM Estudiantes e
JOIN Departamentos d ON e.depto_id = d.depto_id;

-- B. Estadística: Promedio general de notas
SELECT AVG(nota) AS Promedio_General FROM Calificaciones;

-- C. Estadística: Cantidad de estudiantes por departamento
SELECT d.nombre, COUNT(e.estudiante_id) AS Total_Estudiantes
FROM Departamentos d
LEFT JOIN Estudiantes e ON d.depto_id = e.depto_id
GROUP BY d.nombre;

-- 5. ACTUALIZACIÓN Y ELIMINACIÓN
-- Actualizar la nota de un estudiante
UPDATE Calificaciones SET nota = 100 WHERE calificacion_id = 1;

-- Eliminar un curso (Nota: Solo si no tiene clases vinculadas por integridad referencial)
DELETE FROM Cursos WHERE curso_id = 99; -- Ejemplo seguro
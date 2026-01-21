DROP DATABASE IF EXISTS control_escolar;
CREATE DATABASE control_escolar;
USE control_escolar;

CREATE TABLE departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_depto VARCHAR(50)
);

CREATE TABLE profesores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100),
    profesor_id INT,
    FOREIGN KEY (profesor_id) REFERENCES profesores(id)
);

CREATE TABLE calificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    nota DECIMAL(5,2),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
);

-- Inserciones de prueba
INSERT INTO departamentos (nombre_depto) VALUES ('Sistemas'), ('Contabilidad');
INSERT INTO profesores (nombre) VALUES ('Ing. Martínez'), ('Lic. Rodríguez');
INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, departamento_id) VALUES 
('Carlos', 'Garcia', '2000-05-15', 1),
('Nedual', 'Vargas', '1998-11-20', 1),
('Wilson', 'Manuel', '2002-01-10', 2),
('Alexandra', 'Santos', '2001-07-22', 1),
('Geudys', 'Quiroz', '1995-03-30', 2);
INSERT INTO cursos (nombre_curso, profesor_id) VALUES ('Base de Datos', 1), ('Programación', 1), ('Finanzas', 2);
INSERT INTO calificaciones (estudiante_id, nota) VALUES (1, 95), (1, 88), (2, 92), (3, 85), (4, 98), (5, 70);


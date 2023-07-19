CREATE DATABASE IF NOT EXISTS people;

USE people;

CREATE TABLE miembros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo VARCHAR(100),
    edad INT
);

INSERT INTO miembros (nombre, apellido, correo, edad)
VALUES ('Juan', 'Perez', 'juan@juan.com', 30);

SELECT * FROM miembros;

UPDATE miembros
SET edad = 60
WHERE nombre = 'Juan';

SELECT * FROM miembros;
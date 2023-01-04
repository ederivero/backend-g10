USE practicas;

CREATE TABLE usuarios(
	id      INT      AUTO_INCREMENT UNIQUE PRIMARY KEY,
    nombre  TEXT     NOT NULL,
    dni     CHAR(8)  UNIQUE
);


CREATE TABLE tareas(
	id 			INT 			AUTO_INCREMENT PRIMARY KEY,
    titulo  	VARCHAR(100)	UNIQUE,
    descripcion TEXT,
    usuario_id  INT,
    -- CREO LA RELACION ENTRE LAS TABLAS
    -- indico entre parentesis la columna de esta tabla y luego la tabla(su columna)
    FOREIGN KEY (usuario_id) ReFeRenCeS usuarios(id)
);


-- SUB LENGUAJES
-- DDL (Data Definition Language)
-- Es un lenguaje que sirve para definir estructuras de datos (Crear bd, crear tablas,
-- actualizar tablas, eliminar tablas)
-- CREATE (Crear)
-- ALTER  (Actualizar)
-- DROP   (Eliminar) elimina absolutamente TODO

-- DML (Data Manipulation Language)
-- Es un lenguaje que sirve para definir la informacion que ira dentro de las estructuras
-- Insertar datos, actualizar datos, eliminar datos y leer datos
-- INSERT (Insertar)
-- SELECT (Visualizar)
-- UPDATE (Actualizar)
-- DELETE (Eliminar)

-- En este caso como el 'id' es auto_increment no le pondremos un valor 
INSERT INTO usuarios (nombre, dni) VALUES ('Eduardo', '73500746');

-- Si queremos utilizar el valor por defecto de una columna
INSERT INTO usuarios (id, nombre, dni) VALUES (DEFAULT, 'Juana', '71589264');

-- Si queremos ingresar varios registros
INSERT INTO usuarios (id, nombre, dni) VALUES (DEFAULT, 'Roberto', '35269485'), 
                                              (DEFAULT, 'Maria', '29165148'),
                                              (DEFAULT, 'Roxana', '56236841');

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES 
				(DEFAULT, 'ir a la playa', 'ire a la playa el fin de semana', 1),
                (DEFAULT, 'ir a la piscina', 'ire a la piscina a mis clases de natacion', 2);

-- Visualizar la informacion
SELECT nombre, dni, id, id FROM usuarios;

-- Visualizar la totalidad de las columnas
SELECT * FROM usuarios;

INSERT INTO usuarios (id, nombre, dni) VALUES (DEFAULT, 'Juana', '33265946'), 
                                              (DEFAULT, 'Maria', '52698524');

-- SELECCIONA TODAS LAS COLUMNAS DE LA TABLA USUARIOS DONDE nombre SEA Juana
SELECT * FROM usuarios WHERE nombre='Juana' AND id=2;

-- Visualizar todas las tareas del usuario 1 Y/O del usuario 2
SELECT * FROM tareas WHERE usuario_id=1 OR usuario_id=2;

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES (DEFAULT, 'Ir a comer', 'Comer un sabroso pollito a la brasa', 1),
																(DEFAULT, 'Comer pizza', 'Comer una sabrosa pizza con peperoni', 1);



SELECT * FROM tareas WHERE usuario_id=1;


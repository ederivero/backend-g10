DROP TABLE categorias; -- solo se puede hacer la eliminacion siempre y cuando esa tabla no tenga otras tablas dependientes
DROP DATABASE minimarket;
-- 1. CREAR UNA BASE DE DATOS LLAMADA MINIMARKET
CREATE DATABASE minimarket;
USE minimarket;

-- 2. CREAR UNA TABLA LLAMADA CATEGORIAS:
-- id entero llave primaria y auto incrementable
-- nombre text

CREATE TABLE categorias(
	id		INT PRIMARY KEY AUTO_INCREMENT,
    nombre	TEXT
);

-- 3. CREAR UNA TABLA LLAMADA PRODUCTOS en la cual tengamos lo siguiente:
-- id entero llave primaria y auto incrementable
-- nombre text
-- imagen text
-- fecha_vencimiento date
-- precio float
-- disponible boolean defecto (verdadero)
CREATE TABLE productos(
	id 					INT PRIMARY KEY AUTO_INCREMENT,
    nombre 				TEXT,
    imagen				TEXT,
    fecha_vencimiento 	DATE,
    precio 				FLOAT,
    disponible 			BOOLEAN DEFAULT TRUE,
    categoria_id		INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);


-- Modificamos la tabla para agregar la columna categoria_id
-- ALTER TABLE productos ADD COLUMN categoria_id INT;
-- Agregamos la relacion entre productos y categorias
-- ALTER TABLE productos ADD FOREIGN KEY (categoria_id) REFERENCES categorias(id);


-- 4. CREAR UNA TABLA LLAMADA ALMACENES en la cual seria de la sgte manera:
-- id entero llave primaria y auto incrementable
-- nombre text
-- direccion text
CREATE TABLE almacenes(
	id			INT PRIMARY KEY AUTO_INCREMENT,
    nombre		TEXT,
    direccion	TEXT
);
-- Una categoria puede tener varios productos pero un producto pertenece a una sola categoria


-- Si se desea cambiar el nombre de la tabla
-- ALTER TABLE nombre_antiguo RENAME nuevo_nombre;


-- Un producto puede estar en varios almacenes y a su vez cada almacen puede tener varios productos
CREATE TABLE almacen_producto(
	id 			INT PRIMARY KEY AUTO_INCREMENT,
    almacen_id 	INT NOT NULL,
    producto_id INT NOT NULL,
    FOREIGN KEY (almacen_id) REFERENCES almacenes(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

INSERT INTO categorias (id, nombre) VALUES 	(DEFAULT, 'Frutas'), 
											(DEFAULT, 'Legumbres'), 
                                            (DEFAULT, 'Snacks'),
                                            (DEFAULT, 'Otros');

INSERT INTO productos (id, nombre, imagen, fecha_vencimiento, precio, disponible, categoria_id) VALUES (DEFAULT, 'Lechuga Carola', 'https://google.com','2022-01-10',2.90, true, 2),
																									   (DEFAULT, 'Beterraga', 'https://google.com','2022-02-14',1.90, true, 2),
                                                                                                       (DEFAULT, 'Papitas fritas', 'https://google.com','2025-01-10',2.90, true, 3),
                                                                                                       (DEFAULT, 'Platano de seda', 'https://google.com','2022-01-10',4.75, true, 1),
                                                                                                       (DEFAULT, 'Short playero', 'https://google.com','2022-12-31',39.90, true, 4),
                                                                                                       (DEFAULT, 'Mandarina', 'https://google.com','2022-05-23',2.90, true, 1);

INSERT INTO almacenes (id, nombre, direccion ) VALUES (DEFAULT, 'ALMACEN A', 'Calle los ruiseñores 1080'),
													  (DEFAULT, 'ALMACEN B', 'Calle los girasoles 570'),
                                                      (DEFAULT, 'ALMACEN C', 'Av Venezuela 3040');

INSERT INTO almacen_producto (id, almacen_id, producto_id) VALUES (DEFAULT, 1, 1),
																  (DEFAULT, 1, 2),
                                                                  (DEFAULT, 2, 2),
                                                                  (DEFAULT, 2, 3),
                                                                  (DEFAULT, 3, 4),
                                                                  (DEFAULT, 1, 5),
                                                                  (DEFAULT, 2, 6),
                                                                  (DEFAULT, 3, 5);

-- Ejercicios
-- 1. Mostrar todos los productos que tengan un precio mayor o igual que 3
SELECT * FROM productos WHERE precio >= 3;

-- 2. Mostrar todos los productos cuya fecha de vencimiento sea menor al 1 de agosto del 2022

SELECT * FROM productos WHERE fecha_vencimiento < '2022-08-01';

-- 3. Mostrar los nombres de los productos concatenados con su url de la imagen en una sola columna que 
-- se llame 'producto imagen'
SELECT concat(nombre, ' ', imagen) AS 'producto imagen' FROM productos;














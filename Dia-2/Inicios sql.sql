-- Asi se crea una base de datos
CREATE DATABASE IF NOT EXISTS practicas;

USE practicas;

-- ahora procedemos a crear nuestra primera tabla
-- Tipos de datos : https://dev.mysql.com/doc/refman/8.0/en/data-types.html
-- AUTO_INCREMENT > solamente puede haber uno por tabla
CREATE TABLE usuarios(
-- nombre datatype  [conf adicionales]
	id      INT      AUTO_INCREMENT UNIQUE PRIMARY KEY,
    nombre  TEXT     NOT NULL,
    dni     CHAR(8)  UNIQUE
);

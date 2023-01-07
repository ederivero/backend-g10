USE minimarket;

ALTER TABLE almacen_producto DROP FOREIGN KEY almacen_producto_ibfk_2;
-- OPCIONES
-- https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html
-- RESTRICT > restringe o impide la eliminacion de nuestro padre si tiene hijos
-- CASCADE > elimina el padre y elimina a sus hijos
-- SET NULL > elimina al padre y a sus hijos les cambia el valor de esa columna a NULL
-- NO ACTION > es lo mismo que RESTRICT
-- SET DEFAULT > asigna un valor por defecto en el caso que se elimine el padre
ALTER TABLE almacen_producto ADD FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE;

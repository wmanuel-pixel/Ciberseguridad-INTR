
DROP DATABASE IF EXISTS ventas;
CREATE DATABASE ventas;
USE ventas;

-- 2. Crear tabla de Clientes
CREATE TABLE clientes (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- 3. Crear tabla de Productos
CREATE TABLE productos (
    producto_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

-- 4. Crear tabla de Facturas (La tabla que une a las otras dos)
CREATE TABLE facturas (
    factura_id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    cliente_id INT,
    producto_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

-- 5. Insertar algunos Clientes
INSERT INTO clientes (nombre, email) VALUES ('Juan Pérez', 'juan@mail.com');
INSERT INTO clientes (nombre, email) VALUES ('María García', 'maria@mail.com');

-- 6. Insertar algunos Productos
INSERT INTO productos (nombre_producto, precio) VALUES ('Laptop Gamer', 1200.50);
INSERT INTO productos (nombre_producto, precio) VALUES ('Mouse Inalámbrico', 25.00);
INSERT INTO productos (nombre_producto, precio) VALUES ('Monitor 4K', 350.00);

-- 7. Insertar Ventas (Facturas)
-- Juan compra una Laptop (Cliente 1, Producto 1)
INSERT INTO facturas (fecha, cliente_id, producto_id) VALUES ('2024-05-20', 1, 1);
-- María compra un Mouse y un Monitor (Cliente 2, Productos 2 y 3)
INSERT INTO facturas (fecha, cliente_id, producto_id) VALUES ('2024-05-21', 2, 2);
INSERT INTO facturas (fecha, cliente_id, producto_id) VALUES ('2024-05-21', 2, 3);

-- 8. Consulta Final: ¿Quién compró qué y cuánto costó?
SELECT 
    f.factura_id AS 'Nº Factura',
    f.fecha AS 'Fecha',
    c.nombre AS 'Cliente',
    p.nombre_producto AS 'Producto',
    p.precio AS 'Precio Pagado'
FROM facturas f
JOIN clientes c ON f.cliente_id = c.cliente_id
JOIN productos p ON f.producto_id = p.producto_id;
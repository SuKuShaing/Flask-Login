mysql -u root -p
mysql -u fazt -p --(cuando tienes usuarios creados)

-- Crear usuarios para que usen la db

CREATE USER 'fazt'@'localhost' IDENTIFIED BY 'fazt';
-- comandos, nombre del usuario; donde se va a ocupar el usuario y su contraseña

user: fazt
pass: fazt

--Accesos del usuario
-- Más info aquí https://mariadb.com/kb/en/grant/#grant-option
GRANT ALL PRIVILEGES ON *.* TO 'fazt'@'localhost';
-- Comando, tipos de privilegios, en donde, a quién

FLUSH PRIVILEGES;
--Para activar los privilegios otorgados

DROP USER 'nombredelusuario'@'localhost';
-- comandos, nombre del usuario; desde donde se va a eliminar


-- Crear Base de datos
CREATE DATABASE flaskcontacts; --crea la base de datos

SHOW DATABASES; --muestra las bases de datos
USE flaskcontacts; --Para decirle a que bd voy a pedirle información

SHOW TABLES; --para ver todas las tablas
DESCRIBE contacts; -- para ver las características o propiedades de las columnas de nuestra base de datos



-- Crear tabla
USE flaskcontacts;
CREATE TABLE `contacts` ( -- para decirle en que base de datos voy a crear la tabla
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, --se le agrego unsigned que significa que no puede ser negativo
    
    `fullname` varchar(255) not NULL,
    `phone` varchar(255) not NULL,
    `email` varchar(255) not NULL,
    
    `created_at` timestamp not NULL default current_timestamp,
    `updated_at` timestamp not NULL default current_timestamp,

    PRIMARY KEY (id)
)

default CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;




USE flaskcontacts;
-- Insertar las líneas del metro
INSERT INTO `contacts` (fullname, phone, email) VALUES
("Línea 1", "Rosa"),



SELECT * FROM `contacts`;


UPDATE `contacts`
SET name = "Ferrería"
WHERE id = 2;


DELETE FROM `contacts`
WHERE id = 165;
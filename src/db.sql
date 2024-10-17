-- Crear Base de datos
CREATE DATABASE flask_login;

-- Crear tabla
USE flask_login;
CREATE TABLE `users` (
    `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT,
    
    `username` varchar(20) not NULL,
    `password` varchar(102) not NULL,
    `fullname` varchar(50) not NULL,
    
    `created_at` timestamp not NULL default current_timestamp,
    `updated_at` timestamp not NULL default current_timestamp,

    PRIMARY KEY (id)
)

default CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

-- Altera la tabla, ahora la contraseña puede tener hasta 255 caracteres
ALTER TABLE `users`
MODIFY `password` varchar(255) not NULL;


insert into `users` (username, password, fullname) values
    ("OGARCIA", "scrypt:32768:8:1$8coDaFiya6PZtep3$16cd1acd7483e4e8f8d23830c4cd132bbb0d98802b483558e399b94282b2eccbf632b978a34abd4565e70d6b39924ea970b4cd6f79a23594d732fa50607cb2fc", "Oscar Garcia");
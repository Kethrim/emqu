CREATE SCHEMA IF NOT EXISTS `gestion_equipos` DEFAULT CHARACTER SET utf8 ;
USE `gestion_equipos` ;

CREATE TABLE IF NOT EXISTS usuario (
    correo VARCHAR(100) PRIMARY KEY, 
    contrasenia VARCHAR(105) NOT NULL);

CREATE TABLE IF NOT EXISTS equipo (
    dir VARCHAR(15) PRIMARY KEY, 
    nombre VARCHAR(100));

CREATE TABLE IF NOT EXISTS historial (
    id_hist BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    ip VARCHAR(15) NOT NULL, 
    equipo_dir VARCHAR(15) NOT NULL, 
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    ON UPDATE CURRENT_TIMESTAMP, 
    FOREIGN KEY (equipo_dir)
    REFERENCES equipo(dir)
    ON DELETE CASCADE);
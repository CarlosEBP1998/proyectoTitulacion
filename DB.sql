CREATE DATABASE IF NOT EXISTS users;

USE users;

CREATE TABLE IF NOT EXISTS USUARIO (
    nombres varchar(50) NOT NULL,
    apellido_paterno varchar(50) NOT NULL,
    apellido_paterno varchar(50) NOT NULL,
    curp varchar(50) NOT NULL,
    nombre_Usuario varchar(50) NOT NULL,
    passw varchar(50) NOT NULL,
    
    PRIMARY KEY (curp)
);
CREATE DATABASE IF NOT EXISTS users;

USE users;

CREATE TABLE IF NOT EXISTS USUARIO (
    nombres varchar(50) NOT NULL,
    apellido_paterno varchar(50) NOT NULL,
    apellido_materno varchar(50) NOT NULL,
    curp varchar(50) NOT NULL,
    nombre_Usuario varchar(50) NOT NULL,
    passw varchar(70) NOT NULL,
    
    PRIMARY KEY (curp)
);

INSERT INTO USUARIO VALUES ('Victor', 'Perez', 'Dom', 'DPV050568HHGTRR00', 'DacademDPV', '29062023');
INSERT INTO USUARIO VALUES ('Victor Manuel', 'Granados', 'Jimenez', 'GRJV050568HHGTRR03', 'DdedsaGRJV', '$2b$05$B6CFEsOd5aE4dWZi6NI4N.d3fNVwzYQSaLFtx5p5PfzNJEOWb2mZO');
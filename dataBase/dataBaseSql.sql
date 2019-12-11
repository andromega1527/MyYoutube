-- CREATE DATABASE dataBaseMyoutube;

-- USE dataBaseMyoutube;

-- DROP TABLE if EXISTS usuario;
-- CREATE TABLE usuario(
--     email varchar(20) NOT NULL,
--     nome varchar(30) NOT NULL,
--     senha varchar(20) NOT NULL,
--     permissao varchar(10) NOT NUll,
--     PRIMARY KEY(email)
-- );

-- DROP TABLE if EXISTS video;
-- CREATE TABLE video(
--     codigo int(5) AUTO_INCREMENT,
--     nome varchar(20) NOT NULL,
--     descricao varchar(30),
--     PRIMARY KEY(codigo)
-- );

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS video;

CREATE TABLE user (
    email TEXT PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL,
    permissao TEXT NOT NUll
);

CREATE TABLE video (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
);
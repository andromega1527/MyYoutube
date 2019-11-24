CREATE DATABASE dataBaseMyoutube;

USE dataBaseMyoutube;

CREATE TABLE usuario(
    email varchar(20) NOT NULL,
    nome varchar(30) NOT NULL,
    senha varchar(20) NOT NULL,
    permissao varchar(10) NOT NUll,
    PRIMARY KEY(email)
);

CREATE TABLE videos(
    codigo int(5) AUTO_INCREMENT,
    nome varchar(20) NOT NULL,
    descricao varchar(30),
    PRIMARY KEY(codigo)
);
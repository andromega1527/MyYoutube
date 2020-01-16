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
DROP TABLE IF EXISTS playlist;

CREATE TABLE user (
    email TEXT PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL,
    permissao TEXT NOT NUll,
    videos INTEGER NULL,
    playlist INTEGER NULL
);

CREATE TABLE video (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
);

CREATE TABLE playlist (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    videos INTEGER NOT NULL
);

INSERT INTO user VALUES('andrejc2008@hotmail.com', 'André Leonam', 'sla', 'admin', NULL, NULL);
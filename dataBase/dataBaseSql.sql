DROP TABLE IF EXISTS userMyoutube;
DROP TABLE IF EXISTS video_details;
DROP TABLE IF EXISTS video;
DROP TABLE IF EXISTS playlist_details;
DROP TABLE IF EXISTS playlist;

CREATE TABLE userMyoutube (
    email TEXT PRIMARY KEY NOT NULL,
    nameUser TEXT NOT NULL,
    passwordUser TEXT NOT NULL,
    permission TEXT NOT NUll,
    playlist INTEGER
);

INSERT INTO userMyoutube VALUES('andrejc2008@hotmail.com', 'André Leonam', 'sla', 'admin', NULL);

CREATE TABLE video_details (
    code_user TEXT NOT NULL,
    code_video INTEGER NOT NULL,
    FOREIGN KEY(code_video) REFERENCES video(code),
    FOREIGN KEY(code_user) REFERENCES userMyoutube(email)
);

INSERT INTO video_details VALUES('andrejc2008@hotmail.com', 1);
INSERT INTO video_details VALUES('andrejc2008@hotmail.com', 2);
INSERT INTO video_details VALUES('andrejc2008@hotmail.com', 3);

CREATE TABLE video (
    code INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nameVideo TEXT NOT NULL,
    descriptionVideo TEXT,
    localization TEXT
);

INSERT INTO video VALUES(1, 'sla', 'sla', NULL);
INSERT INTO video VALUES(2, 'sla1', 'sla', NULL);
INSERT INTO video VALUES(3, 'sla2', 'sla', NULL);

CREATE TABLE playlist_details (
    code_usuario INTEGER PRIMARY KEY,
    code_playlist INTEGER NOT NULL,
    FOREIGN KEY(code_playlist) REFERENCES playlist(code)
);

CREATE TABLE playlist (
    code INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    videos INTEGER NOT NULL
);
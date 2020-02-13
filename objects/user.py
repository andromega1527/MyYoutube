from youtube.db import get_db
from youtube.conn import Server
from youtube.video_informs import loadVideos

class Usuario:
    __email = ''
    __name = ''
    __password = ''
    __permissao = ''
    __playlist = ''

    def __init__(self, name, email, password, permissao):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__permissao = permissao

    #Getters
    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password

    @property
    def permissao(self):
        return self.__permissao

    #Setters
    @name.setter
    def name(self, value):
        self.__name = value

    @email.setter
    def email(self, value):
        self.__email = value

    @password.setter
    def password(self, value):
        self.__password = value

    @permissao.setter
    def permissao(self, value):
        self.__permissao = value

    #Methods
    def add_video(self, filename, nameVideo, descriptionVideo, extension):
        db = get_db()
        max_code = 0

        db.execute(
            'INSERT INTO video (nameVideo, descriptionVideo, extension) \
            VALUES (?, ?, ?)', (nameVideo, descriptionVideo, extension,)
        )

        videos = db.execute(
            'SELECT code FROM video'
        ).fetchall()
        
        for i in videos:
            for j in i:
                if j > max_code:
                    max_code = j

        db.execute(
            'INSERT INTO video_details (code_user, code_video) \
            VALUES (?, ?)', (self.__email, int(max_code),)
        )

        Server().sendFile(filename, str(max_code), self.__email, extension)
        db.commit()

    def remove_video(self, video):
        pass

    def add_playlist(self, playlist):
        pass

    def remove_playlist(self, playlist):
        pass
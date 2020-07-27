from youtube.db import get_db
from youtube.server import Server

class User:
    __email = ''
    __name = ''
    __password = ''
    __permition = ''
    __playlist = ''

    def __init__(self, name, email, password, permition):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__permition = permition

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
    def permition(self):
        return self.__permition

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

    @permition.setter
    def permition(self, value):
        self.__permition = value

    #Methods
    def add_video(self, video_name, video_description, extension, file):
        db = get_db()
        max_code = 0

        db.execute(
            'INSERT INTO video (nameVideo, descriptionVideo, extension) \
            VALUES (?, ?, ?)', (video_name, video_description, extension,)
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

        Server().send_file(str(max_code), self.__email, extension, file)
        db.commit()

    def remove_video(self, link_video):
        pass

    def add_playlist(self, playlist):
        pass

    def remove_playlist(self, playlist):
        pass
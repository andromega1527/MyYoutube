class Usuario:
    __email = ''
    __name = ''
    __password = ''
    __permissao = ''
    __myVideos = []
    __playlist = ''

    def __init__(self, name, email, password, permissao, myVideos, playlist):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__permissao = permissao
        self.__myVideos = myVideos
        self.__playlist = playlist

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

    @property
    def myVideos(self):
        return self.__myVideos

    @property
    def playlist(self):
        return self.__playlist

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

    @myVideos.setter
    def myVideos(self, value):
        self.__myVideos = value

    @playlist.setter
    def playlist(self, value):
        self.__playlist = value

    #Methods
    def add_video(self, video):
        pass

    def remove_video(self, video):
        pass

    def add_playlist(self, playlist):
        pass

    def remove_playlist(self, playlist):
        pass

    def show_name(self):
        return self.__name
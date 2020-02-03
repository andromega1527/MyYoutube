class Playlist:
    __codigo = ''
    __name = ''
    __videos = []

    def __init__(self, codigo, name, videos):
        self.__codigo = codigo
        self.__name = name
        self.__videos = videos

    #Getters
    @property
    def name(self):
        return self.__name

    @property
    def videos(self):
        return self.__videos

    #Setters
    @name.setter
    def name(self, value):
        self.__name = value

    @videos.setter
    def videos(self, value):
        self.__videos = value

    #Methods
    def add_video(self, video):
        pass

    def remove_video(self, video):
        pass
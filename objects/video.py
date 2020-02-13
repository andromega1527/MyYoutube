class Video:
    __code = ''
    __title = ''
    __description = ''
    __extension = ''

    def __init__(self, code, title, description, extension):
        self.__code = code
        self.__title = title
        self.__description = description
        self.__extension = extension

    #Getters
    @property
    def code(self):
        return self.__code

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def extension(self):
        return self.__extension

    #Setters
    @title.setter
    def title(self, value):
        self.__title = value

    @description.setter
    def description(self, value):
        self.__description = value

    @extension.setter
    def extension(self, value):
        self.__extension = value

    #Methods

    # @classmethod
    # def method(cls):

    # @staticmethod
    
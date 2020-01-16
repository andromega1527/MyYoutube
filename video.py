class Video:
    __codigo = ''
    __title = ''
    __description = ''
    __local = ''

    def __init__(self, codigo, title, description, local):
        self.__codigo = codigo
        self.__title = title
        self.__description = description
        self.__local = local

    #Getters
    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    #Setters
    @title.setter
    def title(self, value):
        self.__title = value

    @description.setter
    def description(self, value):
        self.__description = value

    #Methods


    # @classmethod
    # def method(cls):

    # @staticmethod
    
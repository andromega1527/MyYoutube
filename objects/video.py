class Video:
    __code = ''
    __title = ''
    __description = ''
    __local = ''

    def __init__(self, code, title, description, local):
        self.__code = code
        self.__title = title
        self.__description = description
        self.__local = local

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
    
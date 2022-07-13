import copy

command_list = []


class Command:
    def __init__(self):
        self.__keys = []
        self.description = ''
        self.__kwargs = {}
        command_list.append(self)

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, mas):
        for k in mas:
            self.__keys.append(k.lower())

    @property
    def kwargs(self):
        # return copy(self.__kwargs)

    @kwargs.setter
    def kwargs(self, mas):
        self.__kwargs = copy
        # for k in mas:
        #     self.__kwargs[k[0]] = k[1]

    def process(self, *args):
        pass

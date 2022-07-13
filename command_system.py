import copy

command_list = []


class Command:
    def __init__(self):
        self.__keys = []
        self.__description = ''
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
        return_dict = {}
        for k in self.__kwargs:
            return_dict[k] = None
        return return_dict

    @kwargs.setter
    def kwargs(self, kwargs_):
        self.__keys = copy.deepcopy(kwargs_)

    def get_description_kwargs(self):
        desc_list = []
        for k in self.__kwargs:
            desc_list.append((k, self.__kwargs[k]))
        return desc_list

    def process(self, *args):
        pass

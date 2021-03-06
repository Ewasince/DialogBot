import copy
import importlib
import os

from settings import bot_commands_dir

command_list = []


class Command:
    def __init__(self, store: list, module_path, own_store, local=False):
        if local:
            return
        self.__keys = []
        self.description = ''
        self.own_store = own_store
        store.append(self)
        load_bot_modules(module_path)

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, mas):
        for k in mas:
            self.__keys.append(k)

    def process(self, input_, **kwargs):
        pass


def load_bot_modules(path):
    if path is None:
        return
    # path = bot_commands_dir if path == '' else f'{bot_commands_dir}\\{path}'
    dirs = os.listdir(path)
    modules = []
    for name_module in dirs:
        dir_module = f'{path}\\{name_module}'
        if os.path.isdir(dir_module):
            full_name_module = f'{dir_module}\\{name_module}.py'
            if os.path.exists(full_name_module):
                modules.append(full_name_module[:-3].replace('\\', '.'))
    for m in modules:
        importlib.import_module(m)


def process_command(message, cmd_list, **kwargs):
    input_ = message.strip()

    for c in cmd_list:  # TODO: сделать так, чтобы если команда удовлетворяла условиям, но после нее были невалидные кварги, она не срабатывала, путём выдачи None
        # TODO: скорее всего нужно будет в вызов команды добавить кварг о несрабатывании нее, чтобы можно было ипользовать встроенную функцию выполнения комманд
        for key in c.keys:
            if input_.find(key) == 0:
                input_ = input_[len(key):]
                result = c.process(input_, **kwargs)
                return result
    return None


load_bot_modules(bot_commands_dir)
pass

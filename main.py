import os

from tools import fill_args
from commands.local_command_system import command_list
import importlib
import client
from settings import local_commands_dir
import commands.bot_command_system.bot_command_system as b_cmd

is_continue = True
is_continue_bot = True


def main():
    load_modules()
    client.start()
    start_console()
    # start_console_alt()


def start_console():
    print('type \'help\' for more information')
    # command = ''
    while is_continue:
        input_ = [n.strip() for n in input('> ').split(' ')]
        command = input_.pop(0)

        flag = True
        for c in command_list:
            if command in c.keys:
                kwargs = c.kwargs
                if len(kwargs) > 0:
                    kwargs = fill_args(input_)
                c.process(input_, **kwargs)
                flag = False
                break
        if flag:
            print('unknown command \'{}\''.format(command))
        pass
    pass


def stop_console():
    global is_continue
    is_continue = False


def load_modules():
    # путь от рабочей директории, ее можно изменить в настройках приложения
    files = os.listdir(local_commands_dir)
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        path = local_commands_dir.replace('\\', '.')
        importlib.import_module(f'{path}.{m[0:-3]}')


if __name__ == '__main__':
    main()

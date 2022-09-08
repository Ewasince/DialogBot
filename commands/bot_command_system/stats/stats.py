import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.bot_command_system import command_list as parent_cl

from generator.generator import Generator
from filemanager import get_chat_path

command_list = []


def stats(input_, **kwargs):
    if input_ != '':
        return None
    event = kwargs['event']
    path = get_chat_path(event)
    gen = Generator(path)
    gen.refresh_dicts('words_len')
    words_len = gen.tables['words_len']
    words_len_list = [int(n) for n in words_len]
    words_len_list.sort()
    result = 'количество слов для каждой длины:\n'
    zero = 0
    for i in range(1, words_len_list[-1] + 1):
        value = words_len.setdefault(str(i), 0)
        if value == 0:
            zero += 1
        else:
            zero = 0
        if zero > 4:
            break
        result += f'{i}: {value}\n'

    return result


rel_module_path = os.path.relpath(os.path.dirname(__file__))
stats_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

stats_command.keys = ['stats', 's', 'статистика']
stats_command.description = 'некторая статистика по беседе'
stats_command.process = stats
stats_command.kwargs = {}

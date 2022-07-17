import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.generate.generate_word import command_list as parent_cl
import generator.generator as g

command_list = []


def second_alg(input_, **kwargs):
    g.refresh_dicts()
    result = g.generate_word_2()
    return result


rel_module_path = os.path.relpath(os.path.dirname(__file__))
second_alg_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

second_alg_command.keys = ['second', 's', '2']
second_alg_command.description = 'второй алгоритм генерации слова'
second_alg_command.process = second_alg
second_alg_command.kwargs = {}

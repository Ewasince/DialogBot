import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.generate.generate_word import command_list as parent_cl
import generator.generator as g

command_list = []


def first_alg(input_, **kwargs):
    g.refresh_dicts()
    result = g.generate_word_1()
    return result


rel_module_path = os.path.relpath(os.path.dirname(__file__))
first_alg_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

first_alg_command.keys = ['first', 'f', '1']
first_alg_command.description = 'первый алгоритм генерации слова'
first_alg_command.process = first_alg
first_alg_command.kwargs = {}

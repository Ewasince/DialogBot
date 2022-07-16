import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.generate_word.generate_word import command_list as parent_cl

command_list = []


def first_alg(input_, **kwargs):
    return 'not filled'


rel_module_path = os.path.relpath(os.path.dirname(__file__))
second_alg_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

second_alg_command.keys = ['second', 's', '2']
second_alg_command.description = 'второй алгоритм генерации слова'
second_alg_command.process = first_alg
second_alg_command.kwargs = {}

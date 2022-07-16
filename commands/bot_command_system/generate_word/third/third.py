import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.generate_word.generate_word import command_list as parent_cl

command_list = []


def third_alg(input_, **kwargs):
    return 'not filled'


rel_module_path = os.path.relpath(os.path.dirname(__file__))
third_alg_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

third_alg_command.keys = ['third', 't', '3']
third_alg_command.description = 'третий алгоритм генерации слова'
third_alg_command.process = third_alg
third_alg_command.kwargs = {}

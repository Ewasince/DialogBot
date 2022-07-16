import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.bot_command_system import command_list as parent_cl

command_list = []


def generate_word(input_, **kwargs):
    return 'not filled'


rel_module_path = os.path.relpath(os.path.dirname(__file__))
generate_word_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

generate_word_command.keys = ['generate_word', 'g', 'слово']
generate_word_command.description = 'генерирование чего-либо'
generate_word_command.process = generate_word
generate_word_command.kwargs = {}

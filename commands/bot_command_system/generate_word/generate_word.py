import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.bot_command_system import command_list as parent_cl
from commands.bot_command_system.bot_command_system import process_message
# from commands.bot_command_system.generate_word.second.second import second_alg

command_list = []


def generate_word(input_, **kwargs):
    result = process_message(input_, command_list)
    if result is None:
        for c in command_list:
            if 'second' in c.keys:
                result = command_list
                break
    return result


rel_module_path = os.path.relpath(os.path.dirname(__file__))
generate_word_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

generate_word_command.keys = ['generate_word', 'g', 'слово']
generate_word_command.description = 'генерирование чего-либо'
generate_word_command.process = generate_word
generate_word_command.kwargs = {}

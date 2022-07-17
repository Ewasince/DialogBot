import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.generate_word.generate_word import command_list as parent_cl
import generator.generator as g

command_list = []


def new_replica(input_, **kwargs):
    g.refresh_dicts()
    result = g.generate_word_2()
    return result


rel_module_path = os.path.relpath(os.path.dirname(__file__))
new_replica_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

new_replica_command.keys = ['second', 's', '2']
new_replica_command.description = 'второй алгоритм генерации слова'
new_replica_command.process = new_replica
new_replica_command.kwargs = {}

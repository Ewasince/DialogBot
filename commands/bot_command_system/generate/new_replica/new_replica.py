import os
import random

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.generate.generate_word import command_list as parent_cl
import generator.generator as g
from settings import data_chats_dir
import pickle

command_list = []


def new_replica(input_, **kwargs):
    chat_id = kwargs.setdefault('chat_id', None)
    if not chat_id:
        return 'no chat id'
    path = f'{data_chats_dir}\\{str(chat_id)}'
    filename = f'{path}\\messages'

    count = random.normalvariate()




    return result


rel_module_path = os.path.relpath(os.path.dirname(__file__))
new_replica_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

new_replica_command.keys = ['nr', 's', '2']
new_replica_command.description = 'второй алгоритм генерации слова'
new_replica_command.process = new_replica
new_replica_command.kwargs = {}

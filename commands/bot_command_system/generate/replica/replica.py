import os
import random
import pickle

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.generate.generate import command_list as parent_cl
import generator.generator as g
from settings import data_chats_dir
from commands.bot_command_system.analyze.analyze import Message
from generator.generator import ChatGenerator
import commands.bot_command_system.analyze.analyze as analyze

command_list = []


def new_replica(input_, chat_id=None, **kwargs):
    if input_ != '':
        return None
    if not chat_id:
        return 'no chat id'
    path = f'{data_chats_dir}\\{str(chat_id)}'
    filename = f'{path}\\messages'
    if not os.path.exists(filename):
        analyze.analyze_chat('', **kwargs)
    with open(filename, 'rb') as f:
        messages = pickle.load(f)
    generator = ChatGenerator(messages)
    message = generator.generate_replica()

    return message


def auto_generate(input_, chat_id, **kwargs):
    if not chat_id:
        raise Exception('no chat id')
    path = f'{data_chats_dir}\\{str(chat_id)}'
    filename = f'{path}\\properties'
    if not os.path.exists(filename):
        raise Exception(f'no data properties in {chat_id}')
    with open(filename, 'rb') as f:
        properties = pickle.load(f)
    replica = new_replica(input_, chat_id=chat_id, **kwargs)


rel_module_path = os.path.relpath(os.path.dirname(__file__))
new_replica_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

new_replica_command.keys = ['replica', 'r']
new_replica_command.description = 'генерировать новую реплику'
new_replica_command.process = new_replica
new_replica_command.kwargs = {}

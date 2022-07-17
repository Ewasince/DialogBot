import os
import pickle
import random

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.bot_command_system import command_list as parent_cl
from vkapi import get_by_conversation_id
from settings import group_id, data_chats_dir

command_list = []


def analyze_chat(input_, **kwargs):
    event = kwargs['event']
    if event is None:
        return
    chat_id = kwargs['chat_id']
    conv_message_id = event.message.conversation_message_id
    # conv_message_id = 230
    messages = dict()
    for n in range(0, conv_message_id, 100):
        ids = [str(n) for n in range(n, n + 100)]
        response = get_by_conversation_id(chat_id, ','.join(ids))
        for message_obj in response['items']:
            # message = response.items[i]
            group_id_ = -int(group_id)
            from_id = message_obj['from_id']
            if from_id == group_id_:
                continue
            conversation_message_id = message_obj['conversation_message_id']
            text = message_obj['text']
            attachments = message_obj['attachments']
            messages[conversation_message_id] = (text, attachments, from_id)
        # process_messages()
    pass

    # path = f'{data_chats_dir}\\{str(chat_id)}'
    # messages_loaded: dict
    filename = f'{data_chats_dir}\\{str(chat_id)}'
    if not os.path.exists(data_chats_dir):
        os.makedirs(data_chats_dir)
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            messages_loaded = pickle.load(f)
            messages_loaded.update(messages)
            messages = messages_loaded
    with open(filename, 'wb') as f:
        pickle.dump(messages, f)

    return random.choices(replies, k=1)[0]


def process_messages():
    pass


replies = ['проанализировал', 'готово', 'сделано', 'сделал', 'дело сделано']

rel_module_path = os.path.relpath(os.path.dirname(__file__))
analyze_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

analyze_command.keys = ['analyze', 'a', 'анализировать']
analyze_command.description = 'анализировать текущую беседу'
analyze_command.process = analyze_chat
analyze_command.kwargs = {}

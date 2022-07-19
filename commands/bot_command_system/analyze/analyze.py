import copy
import os
import pickle
import random
import datetime

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.bot_command_system import command_list as parent_cl
from vkapi import get_by_conversation_id
from settings import group_id, data_chats_dir
from generator.analyzer import Analyzer, get_words
from tools import check_path
from commands.bot_command_system.help.help import keys as help_keys

command_list = []


def analyze_chat(input_, **kwargs):
    event = kwargs['event']
    if event is None:
        return 'event is empty'
    chat_id = kwargs['chat_id']
    conv_message_id = event.message.conversation_message_id

    path = f'{data_chats_dir}\\{str(chat_id)}'
    check_path(path)
    filename = f'{path}\\messages'
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            messages_loaded = pickle.load(f)
            last_conv_id = messages_loaded[-1].conv_id + 1
    else:
        messages_loaded = list()
        last_conv_id = 0
    ids_to_load = range(last_conv_id, conv_message_id + 1, 100)

    new_messages = list()
    analyzer = Analyzer()
    for n in ids_to_load:
        ids = [str(n) for n in range(n, n + 100)]
        response = get_by_conversation_id(chat_id, ','.join(ids))
        for message_obj in response['items']:
            # # message = response.items[i]
            # from_id = message_obj['from_id']
            # if from_id == -int(group_id):
            #     continue
            # text = message_obj['text']
            # if text == '':
            #     continue
            # if is_command(text, parent_cl):
            #     continue

            from_id = message_obj['from_id']
            text = message_obj['text']
            if not analyze_message(from_id, text, analyzer):
                continue
            conversation_message_id = message_obj['conversation_message_id']
            attachments = message_obj['attachments']
            new_messages.append(Message(conversation_message_id, text, attachments, from_id))
    if len(new_messages) == 0:
        return 'нечего анализировать'
    messages_loaded.extend(new_messages)

    # for mes in new_messages:
    #     words = get_words(mes.text)
    #     analyzer.analyze(words)

    analyzer.save_dicts(path=path, fjson=False)

    with open(filename, 'wb') as f:
        pickle.dump(messages_loaded, f)
    return random.choice(replies)


def analyze_new_message(_input, **kwargs):
    event = kwargs['event']
    analyzer = Analyzer()
    message_obj = event.message
    from_id = message_obj['from_id']
    text = message_obj['text']
    if not analyze_message(from_id, text, analyzer):
        return
    chat_id = event.chat_id
    path = f'{data_chats_dir}\\{str(chat_id)}'
    analyzer.save_dicts(path=path, fjson=False)

    filename = f'{path}\\messages'
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            messages_loaded = pickle.load(f)
    else:
        messages_loaded = list()

    conversation_message_id = message_obj['conversation_message_id']
    attachments = message_obj['attachments']
    messages_loaded.append(Message(conversation_message_id, text, attachments, from_id))
    with open(filename, 'wb') as f:
        pickle.dump(messages_loaded, f)
    pass


def analyze_message(from_id, text, analyzer: Analyzer):
    if from_id == -int(group_id):
        return False
    if text == '':
        return False
    if is_command(text, parent_cl):
        return False
    words = get_words(text)
    analyzer.analyze(words) # TODO: где-то тут сделать анализ времени отправки сообщения чтобы в будущем потом
    # TODO: определить среднее количество отсылаемых сообщений в день и на основе этого определить на сколько сообщений
    #  # TODO: бот будет периодически замолка ть и появляться
    return True


class Message:
    def __init__(self, conversation_message_id, text, attachments, from_id):
        self.conv_id = conversation_message_id
        self.text = text
        self.attachments = attachments
        self.from_id = from_id


def is_command(text, commands):
    command = copy.copy(text)
    for k in help_keys:
        if command.find(k) == 0:
            command = command[len(k):]
            if command == '':
                return True
            break
    return is_inner_command(command, commands)


def is_inner_command(command: str, commands):
    command = command.strip()
    for c in commands:
        for k in c.keys:
            if command.find(k) == 0:
                command = command[len(k):]
                if command == '':
                    return True
                if is_inner_command(command, c.own_store):
                    return True
                return False
    return False


replies = ['проанализировал', 'готово', 'сделано', 'сделал', 'дело сделано']

rel_module_path = os.path.relpath(os.path.dirname(__file__))
analyze_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

analyze_command.keys = ['analyze', 'a', 'анализировать']
analyze_command.description = 'анализировать текущую беседу'
analyze_command.process = analyze_chat
analyze_command.kwargs = {}

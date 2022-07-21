import copy
import os
import pickle
import random
import datetime

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.bot_command_system import command_list as parent_cl
from vkapi import get_by_conversation_id
from settings import group_id, data_chats_dir
from generator.analyzer import Analyzer, DateAnalyzer
from filemanager import get_words, save_data, load_properties, save_class_properties
from tools import check_path
from commands.bot_command_system.help.help import keys as help_keys

command_list = []


def analyze_chat(input_, **kwargs):
    event = kwargs['event']
    if event is None:
        return 'event is empty'
    chat_id = event.chat_id
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
    properties = kwargs.setdefault('properties', None)
    if not properties:
        properties = load_properties(path)
    date_analyzer = DateAnalyzer(properties)
    analyzer = Analyzer(date_analyzer)
    for n in ids_to_load:
        ids = [str(n) for n in range(n, n + 100)]
        response = get_by_conversation_id(chat_id, ','.join(ids))
        for message_obj in response['items']:
            from_id = message_obj['from_id']
            text = message_obj['text']
            date = message_obj['date']
            if not analyze_message(analyzer, from_id, text, date):
                continue
            conversation_message_id = message_obj['conversation_message_id']
            attachments = message_obj['attachments']
            date = message_obj['date']
            new_messages.append(Message(conversation_message_id, text, attachments, from_id, date))
    if len(new_messages) == 0:
        return 'нечего анализировать'
    messages_loaded.extend(new_messages)

    save_data(analyzer, path=path, fjson=False)
    # save_class_properties(analyzer.date_analyzer, path=path)
    with open(filename, 'wb') as f:
        pickle.dump(messages_loaded, f)
    return random.choice(replies)


def analyze_new_message(_input, **kwargs):
    event = kwargs['event']
    message_obj = event.message
    from_id = message_obj['from_id']
    text = message_obj['text']
    date = message_obj['date']

    chat_id = event.chat_id
    path = f'{data_chats_dir}\\{str(chat_id)}'
    properties = load_properties(path)
    if len(properties) == 0 or message_obj['conversation_message_id'] - properties['last_id'] > 2:
        kwargs['properties'] = properties
        analyze_chat(_input, **kwargs)
        return

    date_analyzer = DateAnalyzer(properties)
    analyzer = Analyzer(date_analyzer)
    if not analyze_message(analyzer, from_id, text, date):
        return
    save_data(analyzer, path=path, fjson=False)
    # save_class_properties(analyzer.date_analyzer, path=path)

    filename = f'{path}\\messages'
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            messages_loaded = pickle.load(f)
    else:
        messages_loaded = list()

    conversation_message_id = message_obj['conversation_message_id']
    attachments = message_obj['attachments']
    date = message_obj['date']
    messages_loaded.append(Message(conversation_message_id, text, attachments, from_id, date))
    with open(filename, 'wb') as f:
        pickle.dump(messages_loaded, f)
    pass


def analyze_message(analyzer: Analyzer, from_id, text, date):
    if from_id == -int(group_id):
        return False
    if text == '':
        return False
    if is_command(text, parent_cl):
        return False
    words = get_words(text)
    analyzer.analyze(words)
    analyzer.date_analyzer.analyze_date(date)  # TODO: проверить как работает среднее значение
    return True


class Message:
    def __init__(self, conversation_message_id, text, attachments, from_id, date):
        self.conv_id = conversation_message_id
        self.text = text
        self.attachments = attachments
        self.from_id = from_id
        self.date = date


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

import threading
import logging

import vkapi
from vkapi import send_message_chat, longpoll
from vk_api.bot_longpoll import VkBotEventType
from commands.bot_command_system.bot_command_system import command_list as command_list
from commands.bot_command_system.bot_command_system import process_command
from commands.bot_command_system.analyze.analyze import analyze_new_message, analyze_chat
from commands.bot_command_system.generate.replica.replica import new_replica
from settings import bot_name, data_chats_dir
from filemanager import load_properties, save_properties, refresh_properties

list_clients = []
lock_obj = threading.Lock()
is_continue = True
logger = logging.getLogger(__name__)


def start():
    thread = threading.Thread(target=loop_connect)
    thread.start()


def loop_connect():
    for event in longpoll.listen():
        process_event(event)
        if not is_continue:
            break
    print('client stopped')


def stop():
    global is_continue
    is_continue = False


def process_event(event):
    lock_obj.acquire()
    try:
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                proceed_from_chat(event)
            elif event.from_user:
                proceed_from_ls(event)

    finally:
        lock_obj.release()


def proceed_from_chat(event) -> str:
    try:
        result = proceed_message_chat(event)
    except Exception as e:
        result = str(e)
        logger.exception(result)
        vkapi.send_message_chat(event.chat_id, result, '')
    else:
        if result is not None:
            vkapi.send_message_chat(event.chat_id, result, '')
    finally:
        chat_id = event.chat_id
        prop_path = f'{data_chats_dir}\\{str(chat_id)}'
        conv_id = event.message['conversation_message_id']
        refresh_properties(path=prop_path, last_id=conv_id)


def proceed_message_chat(event) -> str:
    chat_id = event.chat_id
    message = event.message['text']

    try:
        result = process_command(message.strip(), command_list, chat_id=chat_id, event=event)
        if result is not None:
            return result
    except Exception as e:
        logger.exception('')
        return str(e)

    action = event.message.setdefault('action', None)
    if action is not None:
        action_type = event.message.action.setdefault('type', '')
        member_id = event.message.action.setdefault('member_id', 0)
    else:
        action_type = ''
        member_id = 0

    if action_type == 'chat_invite_user':
        if member_id == -214483095:
            result = f'Привет, я— {bot_name}. Для того чтобы начать предоставьте мне доступ ко всей '
            f'переписке. Доступные команды можно узнать набрав \'help\''
            analyze_chat(message, chat_id=chat_id, event=event)
        else:
            result = f'опа, @id{member_id} вылез'
        return result
    elif action_type == 'chat_kick_user':
        result = f'потеряли молодого'
        return result

    analyze_new_message(message, event=event)
    # conversation_message_id = message_obj['conversation_message_id']
    replica = new_replica(message, chat_id=chat_id, event=event)  # TODO: сделать поочередное замолкание бота
    return replica


def proceed_from_ls(event):
    try:
        result = proceed_message_ls(event)
    except Exception as e:
        result = str(e)
        logger.exception(result)
        vkapi.send_message(event.message['from_id'], result, '')
    else:
        if result is not None:
            vkapi.send_message(event.message['from_id'], result, '')


def proceed_message_ls(event) -> str:
    return 'Мне разработчик пока не разрешает отвечать в личных сообщениях :('

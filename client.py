import random
import threading
import logging
import requests
import settings

import vkapi
from vkapi import send_message_chat, longpoll
from vk_api.bot_longpoll import VkBotEventType
from commands.bot_command_system.bot_command_system import command_list as command_list
from commands.bot_command_system.bot_command_system import process_command
from commands.bot_command_system.analyze.analyze import analyze_new_message, analyze_chat
from commands.bot_command_system.generate.replica.replica import new_replica
from settings import bot_name, data_chats_dir, console, bot_console, client
from filemanager import load_properties, save_properties, refresh_properties

list_clients = []
lock_obj = threading.Lock()
logger = logging.getLogger(__name__)
client_thread = None


def start():
    global client_thread
    client_thread = threading.Thread(target=loop_connect)
    client_thread.start()
    settings.client = True


def loop_connect():
    while settings.client:
        try:
            for event in longpoll.listen():
                process_event(event)
                if not settings.client:
                    break
        except requests.exceptions.ReadTimeout:
            pass
        except Exception as e:
            logger.exception(str(e))
    print('client stopped')


def stop():
    settings.client = False


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


def proceed_from_chat(event):
    try:
        chat_id = event.chat_id
        prop_path = f'{data_chats_dir}\\{str(chat_id)}'
        result = proceed_message_chat(event, prop_path=prop_path)

        conv_id = event.message['conversation_message_id']
        refresh_properties(path=prop_path, last_id=conv_id)
    except Exception as e:
        result = str(e)
        logger.exception(result)
        vkapi.send_message_chat(event.chat_id, result, '')
    else:
        if result is not None and result != '':
            vkapi.send_message_chat(event.chat_id, result, '')


def proceed_message_chat(event, prop_path) -> str:
    chat_id = event.chat_id
    message = event.message['text']

    # try:
    result = process_command(message.strip(), command_list, chat_id=chat_id, event=event)
    if result is not None:
        return result
    # except Exception as e:
    #     logger.exception('')
    #     return str(e)

    action = event.message.setdefault('action', None)
    if action is not None:
        action_type = event.message.action.setdefault('type', '')
        member_id = event.message.action.setdefault('member_id', 0)
    else:
        action_type = ''
        member_id = 0

    if action_type == 'chat_invite_user':
        if member_id == -214483095:
            result = f'Привет, я— {bot_name}. Для того чтобы начать предоставьте мне доступ ко всей переписке. ' \
                     f'Доступные команды можно узнать набрав \'help\' '
        else:
            result = f'опа, @id{member_id} вылез'
        return result
    elif action_type == 'chat_kick_user':
        result = f'потеряли молодого'
        return result

    analyze_new_message('', event=event)
    # conversation_message_id = message_obj['conversation_message_id']
    properties = load_properties(prop_path)
    mes_remain = properties.setdefault('mes_remain', 0)
    average_mes_day = properties['average_mes']
    if mes_remain > 0:
        mes_remain -= 1
        replica = new_replica('', chat_id=chat_id, event=event)
        if mes_remain == 0:
            mes_remain = -round(random.normalvariate(average_mes_day * 0.6, 3))
    elif mes_remain < 0:
        mes_remain += 1
        if mes_remain == 0:
            mes_remain = round(random.normalvariate(average_mes_day * 0.8, 3))
        replica = ''
    else:
        mes_remain = round(random.normalvariate(average_mes_day * 0.8, 3))
        replica = new_replica('', chat_id=chat_id, event=event)
    properties['mes_remain'] = mes_remain
    save_properties(properties, prop_path)
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

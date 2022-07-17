import threading

import vkapi
from vkapi import send_message_chat, longpoll
from vk_api.bot_longpoll import VkBotEventType
from commands.bot_command_system.bot_command_system import command_list as command_list
from commands.bot_command_system.bot_command_system import process_message
from settings import bot_name

list_clients = []
lock_obj = threading.Lock()
is_continue = True


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
                process_from_chat(event)
            elif event.from_user:
                process_from_ls(event)
    finally:
        lock_obj.release()


def process_from_chat(event):
    chat_id = event.chat_id
    message = event.message['text']

    result = process_message(message, command_list, chat_id=chat_id, event=event)
    if result is not None:
        vkapi.send_message_chat(chat_id, result)
        return

    action = event.message.setdefault('action', None)
    if action is not None:
        action_type = event.message.action.setdefault('type', '')
        member_id = event.message.action.setdefault('member_id', 0)
    else:
        action_type = ''
        member_id = 0

    if action_type == 'chat_invite_user':
        if member_id == -214483095:
            vkapi.send_message_chat(chat_id,
                                    f'Привет, я— {bot_name}. Для того чтобы начать предоставьте мне доступ ко всей '
                                    f'переписке. Доступные команды можно узнать набрав \'help\'')
        else:
            vkapi.send_message_chat(chat_id, f'опа, @id{member_id} вылез')
        return
    elif action_type == 'chat_kick_user':
        vkapi.send_message_chat(chat_id, f'потеряли молодого')
        return




def process_from_ls(event):
    user_id = event.message['from_id']
    vkapi.send_message(user_id,
                       'Мне разработчик пока не разрешает отвечать в личных сообщениях :(')

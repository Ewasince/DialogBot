import threading

import vkapi
from vkapi import send_message, longpoll
from vk_api.bot_longpoll import VkBotEventType
from generator.generator import generate_word_2
from commands.bot_command_system.bot_command_system import command_list as command_list

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
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            chat_id = event.chat_id
            message = event.message

            result = process_message(message)
            if result is not None:
                vkapi.send_message(chat_id, result)
                return

            try:
                dey = event.message.action['type']
                invite_id = event.message.action['member_id']
            except:
                dey = ''
                invite_id = -100

            if dey == 'chat_invite_user':
                vkapi.send_message(chat_id, f'опа, @id{invite_id} вылез')

            if message == 'привет':
                vkapi.send_message(chat_id, 'приветствую!')


def process_message(message):
    input_ = message.strip()

    for c in command_list:
        for key in c.keys:
            if input_.find(key) == 0:
                input_ = input_[len(key):]
                result = c.process(input_)
                return result
    return None


pass

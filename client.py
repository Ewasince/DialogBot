import threading

import vkapi
from vkapi import send_message, longpoll
from vk_api.bot_longpoll import VkBotEventType
from generator.generator import generate_word_2

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

            try:
                dey = event.message.action['type']
                invite_id = event.message.action['member_id']
            except:
                dey = ''
                invite_id = -100

            if dey == 'chat_invite_user':
                vkapi.send_message(chat_id, 'опа, ливер вылез')

            # if message ==

    # while len(self.data) > 0:
    #     data: dict = self.data.pop(0)
    #     if data['type'] == 'message_new':
    #         text = data['object']['message']['text']
    #         user_id = data['object']['message']['from_id']
    #         message = generate_word_2(**{'key_m': True})
    #         try:
    #             send_message(str(user_id), message)
    #             print('message has been sent')
    #         except Exception as e:
    #             print(e)
    #     else:
    #         pass
    # self.lock_obj.release()


pass

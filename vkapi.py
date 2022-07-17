import vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from settings import *

vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, 214483095)


def send_message_chat(chat_id, message, attachment=''):
    send_data = {'chat_id': chat_id, 'message': message, 'random_id': random.getrandbits(64)}
    vk_session.method('messages.send', send_data)


def send_message(user_id, message, attachment=''):
    send_data = {'user_id': user_id, 'message': message, 'random_id': random.getrandbits(64)}
    vk_session.method('messages.send', send_data)


def get_by_conversation_id(chat_id, list_messages_id):
    send_data = {'peer_id': 2000000000 + chat_id, 'conversation_message_ids': list_messages_id}
    return vk_session.method('messages.getByConversationMessageId', send_data)

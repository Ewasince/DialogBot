import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from settings import *

# vk_session = vk_api.VkApi(token=token)
# longpoll = VkBotLongPoll(vk_session, group_id)
longpoll = None


def send_message(chat_id, message, attachment=""):
    send_data = {'chat_id': chat_id, 'message': message, 'random_id': random.getrandbits(64)}
    vk_session.method('messages_sand', send_data)



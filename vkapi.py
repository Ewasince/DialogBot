import vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from settings import *

# api = vk.API(access_token=token, v='5.110')

vk_session = vk_api.VkApi(token=token)
# vk_session._auth_token()
# vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 214483095)
# longpoll = None


def send_message(chat_id, message, attachment=""):
    send_data = {'chat_id': chat_id, 'message': message, 'random_id': random.getrandbits(64)}
    vk_session.method('messages.send', send_data)



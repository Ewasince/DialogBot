import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from settings import *

vk_session = vk_api.VkApi(token=token)
# vk_session._auth_token()
# vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 214483095)
# longpoll = None


session = vk.AuthSession(access_token = vk_api_access_token)
api = vk.API(session, v = vk_api_version)


def send_message(chat_id, message, attachment=""):
    send_data = {'chat_id': chat_id, 'message': message, 'random_id': random.getrandbits(64)}
    vk_session.method('messages_sand', send_data)

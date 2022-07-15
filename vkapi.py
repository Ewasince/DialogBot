import vk
import random
from settings import *

api = vk.API(access_token=token, v='5.110')


def send_message(user_id, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment,
                      random_id=random.getrandbits(64))

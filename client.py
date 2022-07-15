import requests
import json
from settings import confirmation_token, token, access_token
import threading
import time
from vkapi import send_message
from generator.generator import generate_word_2

list_clients = []


class Client:
    def main(self):
        pass

    def __init__(self, url):
        self.url = url
        self.data = []
        self.lock_obj = threading.Lock()
        self.is_continue = True
        list_clients.append(self)
        pass

    def start(self):
        thread = threading.Thread(target=self.loop_connect)
        thread.start()

    def stop(self):
        self.is_continue = False

    def loop_connect(self):
        time.sleep(2)
        while self.is_continue:
            self.check_messages()
            time.sleep(1)
        print('client stopped')

    def check_messages(self):
        self.request_data()
        self.process_data()
        pass

    def request_data(self):
        request_data = {'type': 'request', 'confirmation_token': confirmation_token}
        json_str = json.dumps(request_data)
        response = requests.post(self.url, json_str)
        print('{}: {}'.format(self.url, response.status_code))
        data_dict: dict = json.loads(response.text)
        self.lock_obj.acquire()
        self.data.extend(data_dict.values())
        self.lock_obj.release()
        return data_dict

    def process_data(self):
        self.lock_obj.acquire()

        while len(self.data) > 0:
            data: dict = self.data.pop(0)
            if data['type'] == 'message_new':
                text = data['object']['message']['text']
                user_id = data['object']['message']['from_id']
                message = generate_word_2(**{'key_m': True})
                try:
                    send_message(str(user_id), message)
                    print('message has been sent')
                except Exception as e:
                    print(e)
            else:
                pass
        self.lock_obj.release()

    pass

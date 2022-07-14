import requests
import json

list_clients = []


class Client:
    def main(self):
        pass

    def __init__(self, url):
        self.url = url
        self.data = []
        list_clients.append(self)
        pass

    def loop_connect(self):
        while True:
            self.check_messages()
        pass

    def check_messages(self):
        response = requests.get(self.url)  # ???
        data: dict = json.loads(response.text)
        texts = []
        pass

    def request_data(self):
        json_str = json.dumps({'type': 'request'})
        response = requests.post(self.url, json_str)
        print('{}: {}'.format(self.url, response.status_code))
        data_dict: dict = json.loads(response.text)
        self.data.extend(data_dict.values())
        return data_dict

        # print(json.loads(response.text))

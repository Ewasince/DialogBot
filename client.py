import requests
import json


class Client:
    def main(self):
        pass

    def __init__(self, url):
        self.url = url
        self.data = {}

        pass

    def loop_connect(self):
        while True:
            self.check_messages()
        pass

    def check_messages(self):
        response = requests.get(self.url)
        data: dict = json.loads(response.text)
        texts = []
        pass

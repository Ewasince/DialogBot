import json

settings: dict
with open('settings.json') as f:
    settings = json.load(f)

token = settings['token']
confirmation_token = settings['confirmation_token']
access_token = settings['access_token']
test_filename = settings['test_filename']
server_url = 'http://ewasince.pythonanywhere.com/'

import json
import os.path


def create_settings_file():
    settings_file = dict()
    settings_file['token'] = ''
    settings_file['confirmation_token'] = ''
    settings_file['access_token'] = ''
    settings_file['test_filename'] = 'generator/test.txt'
    settings_file['group_id'] = ''
    with open('settings.json', 'w') as f:
        json.dump(settings_file, f)
        print('file successfully created')


settings: dict
filename = 'settings.json'
if not os.path.exists(filename):
    create_settings_file()
    print('settings file doesn\'t exists and has been created! please fill settings and restart program')
with open(filename) as f:
    settings = json.load(f)

token = settings['token']
confirmation_token = settings['confirmation_token']
access_token = settings['access_token']
test_filename = settings['test_filename']
group_id = settings['group_id']
server_url = 'https://ewasince.pythonanywhere.com/'
data_dir = 'data'
local_commands_dir = 'commands\\local'
bot_commands_dir = 'commands\\bot_command_system'

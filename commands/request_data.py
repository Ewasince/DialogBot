import command_system
import json
from settings import server_url
import requests


def request_data(input_, kwargs):
    json_str = json.dumps({'type': 'request'})
    response = requests.post(server_url, json_str)
    print('{}: {}'.format(server_url, response.status_code))
    print(json.loads(response.text))


request_data_command = command_system.Command()

request_data_command.keys = ['request_data', 'rd']
request_data_command.description = 'request data from server'
request_data_command.process = request_data
request_data_command.kwargs = {}

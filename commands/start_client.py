import command_system
from settings import server_url
from client import Client


def start_client(input_, **kwargs):
    client = Client(server_url)
    client.start()


start_client_command = command_system.Command()

start_client_command.keys = ['tart_client', 'stc']
start_client_command.description = 'starts client and add its to list'
start_client_command.process = start_client
start_client_command.kwargs = {}

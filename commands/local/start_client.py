from commands import local_command_system
from settings import server_url
import client


def start_client(input_, **kwargs):
    client.start()


start_client_command = local_command_system.Command()

start_client_command.keys = ['start_client', 'stc']
start_client_command.description = 'starts client and add its to list'
start_client_command.process = start_client
start_client_command.kwargs = {}

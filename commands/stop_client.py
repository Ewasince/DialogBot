import command_system
from client import list_clients


def stop_client(input_, **kwargs):
    for c in list_clients:
        c.stop()


stop_client_command = command_system.Command()

stop_client_command.keys = ['stop_client', 'spc']
stop_client_command.description = 'stop client which requesting data'
stop_client_command.process = stop_client
stop_client_command.kwargs = {}

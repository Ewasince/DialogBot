from commands import local_command_system
import client


def stop_client(input_, **kwargs):
    client.stop()


stop_client_command = local_command_system.Command()

stop_client_command.keys = ['stop_client', 'spc']
stop_client_command.description = 'stop client which requesting data'
stop_client_command.process = stop_client
stop_client_command.kwargs = {}

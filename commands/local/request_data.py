from commands import local_command_system
from client import list_clients


def request_data(input_, **kwargs):
    if len(list_clients) == 1:
        client: Client = list_clients[0]
        data = client.request_data()
        print(data)
    else:
        print('!there are {} clients in environment!'.format(len(list_clients)))


request_data_command = local_command_system.Command()

request_data_command.keys = ['request_data', 'rd']
request_data_command.description = 'request data from server'
request_data_command.process = request_data
request_data_command.kwargs = {}

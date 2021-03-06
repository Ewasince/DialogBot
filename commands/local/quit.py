from commands import local_command_system
import main
from commands.local.stop_client import stop_client


def quit_(input_, **kwargs):
    stop_client('')
    main.stop_console()
    print('exiting from app')


quit_command = local_command_system.Command()

quit_command.keys = ['quit', 'q']
quit_command.description = 'quit from the app'
quit_command.process = quit_
quit_command.kwargs = {}

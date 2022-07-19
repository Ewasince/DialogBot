from commands import local_command_system
from commands.bot_command_system.bot_command_system import command_list

quit_command = ['quit', 'q']


def bot_console(input_, **kwargs):
    commands = command_list
    while True:
        raw_import = input('bot> ')
        input_ = raw_import.strip()
        input_list = input_.split(' ')
        if input_list[0] in quit_command:
            break

        exit_loop = False
        for c in commands:
            for key in c.keys:
                if input_.find(key) == 0:
                    input_ = input_[len(key):]
                    mes = c.process(input_)
                    print(mes)
                    exit_loop = True
                    break
            if exit_loop:
                break
    print('bot console stopped')


bot_console_command = local_command_system.Command()

bot_console_command.keys = ['bot_console', 'b']
bot_console_command.description = 'open bot console'
bot_console_command.process = bot_console
bot_console_command.kwargs = {}

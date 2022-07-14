import command_system
import os
from tabulate import tabulate


def help(input_, kwargs):
    c: command_system.Command
    message = []
    for c in command_system.command_list:
        message_line = list()
        keys = c.keys  # TODO: можно ли убрать это
        message_line.append(keys.pop(0))
        # short_keys = ''
        # for k in keys:
        #     short_keys += k
        short_keys = ', '.join(keys)
        message_line.append(short_keys)
        message_line.append(c.description)
        message.append(message_line)
        kwargs = c.get_description_kwargs()
        if len(kwargs) != 0:
            for k in kwargs:
                message_line = list()
                message_line.append('')
                message_line.append(k[0])
                message_line.append(k[1])
                message.append(message_line)
    print(tabulate(message))


help_command = command_system.Command()

help_command.keys = ['help', 'h']
help_command.description = 'this command'
help_command.process = help
help_command.kwargs = {}

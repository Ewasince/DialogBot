import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.bot_command_system import command_list as parent_cl

command_list = []


def help(input_, **kwargs):
    if input_ == '':
        return_message = desc_leaves(bot_command_system.command_list)
    else:
        return_message = desc_branches(bot_command_system.command_list, input_)
    return return_message


def desc_leaves(iter_command_list):
    c: bot_command_system.Command
    return_message = ''
    for c in iter_command_list:
        if len(c.own_store) > 0:
            return_message_ = desc_leaves(c.own_store).replace('\n', '\n|')
            return_message_ = return_message_[:-1]
            return_message_ = '{}\n|{}'.format(c.keys[0], return_message_)
            return_message += return_message_
        else:
            return_message += '{}\n'.format(c.keys[0], c.description)
    return return_message


def desc_branches(commands, input_):
    input_ = input_.strip()

    c: bot_command_system.Command
    for c in commands:
        for key in c.keys:
            if input_.find(key) == 0:
                input_ = input_[len(key):]
                input_ = input_.strip()
                if len(c.own_store) > 0 and len(input_):
                    return desc_branches(c.own_store, input_)
                else:
                    return c.description
    return 'команда не найдена'


rel_module_path = os.path.relpath(os.path.dirname(__file__))
help_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

help_command.keys = ['help', 'h', 'словоблуд, помощь', 'словоблуд помощь']
help_command.description = 'генерирование чего-либо'
help_command.process = help
help_command.kwargs = {}

import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.bot_command_system import command_list as parent_cl

command_list = []


def help(input_, **kwargs):
    if input_ == '':
        return_message = desc_leaves(bot_command_system.command_list)
        return_message = '\n'.join(return_message)
    else:
        return_message = desc_branches(bot_command_system.command_list, input_)
    return return_message


def desc_leaves(iter_command_list):
    c: bot_command_system.Command
    result = list()
    for c in iter_command_list:
        desc_item = f'{c.keys[0]} - {c.description}'
        if len(c.own_store) > 0:
            result.append(desc_item)
            desc_children = desc_leaves(c.own_store)
            for line in desc_children:
                if line[0] == '|':
                    result.append(f'|{line}')
                else:
                    result.append(f'| {line}')
        else:
            result.append(desc_item)
    return result


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
                    if input_ != '':
                        return None
                    keys_str = [f'\'{k}\'' for k in c.keys]
                    result = ', '.join(keys_str)
                    result = f'{result} - {c.description}'
                    return result
    return 'команда не найдена'


rel_module_path = os.path.relpath(os.path.dirname(__file__))
help_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

keys = ['help', 'h', 'словоблуд, помощь', 'словоблуд помощь']
help_command.keys = keys
help_command.description = 'генерирование чего-либо'
help_command.process = help
help_command.kwargs = {}

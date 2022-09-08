import os

from commands.bot_command_system import bot_command_system
from commands.bot_command_system.bot_command_system import command_list as parent_cl

import settings

command_list = []


def quit_(input_, **kwargs):
    settings.bot_console = False
    return ''


rel_module_path = os.path.relpath(os.path.dirname(__file__))
quit_command = bot_command_system.Command(parent_cl, rel_module_path, command_list)

quit_command.keys = ['help', 'h', 'словоблуд, помощь', 'словоблуд помощь']
quit_command.description = 'генерирование чего-либо'
quit_command.process = quit_
quit_command.kwargs = {}

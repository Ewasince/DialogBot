from generator import generator
import command_system
from tools import alphabet
from tabulate import tabulate
from generator.generator import refresh_dicts


def show_pos_letters(input_, **kwargs):
    if refresh_dicts():
        print('no data')
        return
    print('this option not filled yet')
    pass


show_pos_letters_command = command_system.Command()

show_pos_letters_command.keys = ['show_pos_letters', 'spl']
show_pos_letters_command.description = 'show number of letters occurrences by word length'
show_pos_letters_command.process = show_pos_letters
show_pos_letters_command.kwargs = {}

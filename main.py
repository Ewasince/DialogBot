import os
import random

from tools import get_words, show_list, fill_args
from operator import itemgetter
from tabulate import tabulate
from copy import copy, deepcopy
import json, requests
from command_system import command_list
import importlib


def main():
    load_modules()
    analyzer = Analyzer()
    analyzer.console()


class Analyzer:
    def __init__(self):
        self.input_ = ['']

    def console(self):
        print('type \'help\' for more information')
        command = ''
        while command not in commands['quit']:
            self.input_ = [n.strip() for n in input('> ').split(' ')]
            command = self.input_.pop(0)

            flag = True
            for c in command_list:
                if command in c.keys:
                    kwargs = c.kwargs
                    if len(kwargs) > 0:
                        kwargs = fill_args(self.input_, kwargs)
                    c.process(self.input_, kwargs)
                    flag = False
                    break
            if flag:
                print('unknown command \'{}\''.format(command))
            pass
        pass


def load_modules():
    # путь от рабочей директории, ее можно изменить в настройках приложения
    files = os.listdir("commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


commands_raw = [['help', 'h', 'this command'],
                ['quit', 'q', 'exit the program'],
                ['analyze', 'a', 'analyze text for generating words'],
                ['test', 't', 'test command. its performance configures from program code'],
                ['analyze_words', 'aw', 'analyze the frequency and length of words'],
                ['generate_word_1', 'gw1', '1st algorithm for generating words'],
                ['generate_word_2', 'gw2', '2nd algorithm for generating words'],
                ['show_syllables', 'ss', 'show table with analyzed syllables'],
                ['show_letters', 'sl', 'show frequency of letters on current positions'],
                ['show_pos_letters', 'spl', 'same as \'show letters\' but divided by word length'],
                ['send_table', 'st', 'send table of syllables to server']]
arguments_raw = {'analyze_words': ['-w', 'show all words frequency'],
                 'show_syllables': ['-p', 'show relative probability'],
                 'analyze': ['-d', 'analyze all files in directory'],
                 'generate_word_2': ['-m', 'use another formula to calculate coefficient']}
commands = dict()
for i in commands_raw:
    commands[i[0]] = tuple(i[:-1])
for i in arguments_raw:
    list_arg = arguments_raw[i]
    list_arg.insert(0, '')
    arguments_raw[i] = tuple(list_arg)
# test_file = 'chehov.txt'


if __name__ == '__main__':
    main()

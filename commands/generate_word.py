from generator.generator import *
import command_system


def generate(input_, **kwargs):
    count = 1
    if len(input_) > 1:
        count = input_[0]

    if kwargs.setdefault('key_1', False):
        generate_func = generate_word_1
    elif kwargs.setdefault('key_2', False):
        generate_func = generate_word_2
    elif kwargs.setdefault('key_3', False):
        generate_func = generate_word_3
    else:
        generate_func = generate_word_2

    for i in range(count):
        word = generate_func(**kwargs)
        print(word)


generate_word_command = command_system.Command()

generate_word_command.keys = ['generate_word', 'gw']
generate_word_command.description = 'generate new word(s)'
generate_word_command.process = generate
generate_word_command.kwargs = {'-1': 'use first algorithm', '-2': 'use second algorithm'}

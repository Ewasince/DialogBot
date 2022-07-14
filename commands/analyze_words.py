import os
import json

import command_system
from tools import show_list, get_words
from main import test_file


def analyze_words(input_, kwargs):
    pathname = test_file if input_[0] == 't' else input_[0]

    len_dict = dict()
    if kwargs['-d']:
        try:
            list_files = os.listdir(pathname)
        except Exception as e:
            print(e)
            return
        for fname in list_files:
            filename = '{}\\{}'.format(pathname, fname)
            analyze_freq_file(filename, len_dict)
    else:
        analyze_freq_file(pathname, len_dict)

    last_values = dict()
    with open('data\\len_freq.json', 'rw') as f:
        last_values: dict = json.load(f)
        for v in len_dict:
            last_values[v] += last_values.setdefault(v, 0) + len_dict[v]
        json.dump(last_values, f)

    show_list(last_values, num_row=0, reversed=False)


def analyze_freq_file(filename, len_dict):
    text = get_words(filename)
    for word in text:
        word_len = len(word)
        len_dict[word_len] = len_dict.setdefault(word_len, 0) + 1
    # amount_words = len(text)
    # for length in len_dict:
    #     len_dict[length] = len_dict[length] / amount_words
    # show_list(len_dict, num_row=0, reversed=False)
    print('{} finished'.format(filename))


# def analyze_amount_words_file(filename):
#     words = dict()
#     for word in text:
#         words[word] = words.setdefault(word, 0) + 1
#
#     items = words.items()
#     items = sorted(items, key=itemgetter(num_row), reverse=reversed)
#     new_words = list()
#
#     for n, k in enumerate(items):
#         new_words.append((k, items(k)))
#         if n > 10:
#             break
#     show_list(new_words)
#     print('')


analyze_words_command = command_system.Command()

analyze_words_command.keys = ['analyze_words', 'aw']
analyze_words_command.description = 'analyze number of words occurrences command'
analyze_words_command.process = analyze_words
analyze_words_command.kwargs = {'-d': 'analyze file from directory'}

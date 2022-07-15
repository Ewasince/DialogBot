import os, json

import command_system
from tools import show_list, get_words, save_dict
from settings import test_filename
from generator.analyzer import Analyzer


def analyze_words(input_, **kwargs):
    pathname = test_filename if input_[0] == 't' else input_[0]

    analyzer = Analyzer()

    if os.path.isdir(pathname):
        try:
            list_files = os.listdir(pathname)
        except Exception as e:
            print(e)
            return
        for fname in list_files:
            filename = '{}\\{}'.format(pathname, fname)
            text = get_words(filename)
            analyzer.analyze_words_len(filename)
    else:
        text = get_words(pathname)
        analyzer.analyze_words_len(pathname)

    new_values = save_dict('words_len', analyzer.words_len)
    show_list(new_values, num_row=0, reversed=False)


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
analyze_words_command.kwargs = {}

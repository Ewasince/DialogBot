import os
from settings import test_filename
import command_system
from tools import show_list, get_words, check_path, save_dict
from generator.analyzer import Analyzer

data_dir = 'data'


def analyze(input_, **kwargs):
    pathname = test_filename if input_[0] == 't' else input_[0]

    analyzer = Analyzer()

    if os.path.isdir(pathname):
        for fname in os.listdir(pathname):
            filename = '{}\\{}'.format(pathname, fname)
            analyzer.analyze(filename)
    else:
        analyzer.analyze(pathname)

    last_values_1 = save_dict('syll_freq', analyzer.syll_freq)
    last_values_2 = save_dict('letters_pos', analyzer.letter_pos)
    last_values_3 = save_dict('letters_pos_by_word', analyzer.letter_pos_by_word)
    last_values_4 = save_dict('words_len', analyzer.words_len)

    if kwargs.setdefault('key_a', False):
        show_list(last_values_1, num_row=0, reversed=False)
        show_list(last_values_2, num_row=0, reversed=False)
        show_list(last_values_3, num_row=0, reversed=False)
        show_list(last_values_4, num_row=0, reversed=False)


analyze_command = command_system.Command()

analyze_command.keys = ['analyze', 'a']
analyze_command.description = 'analyze text for generating new content'
analyze_command.process = analyze
analyze_command.kwargs = {'-d': 'analyze file from directory', '-a': 'show all results'}

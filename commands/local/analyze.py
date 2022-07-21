import os
from settings import test_filename
from commands import local_command_system
from tools import show_list
from generator.analyzer import Analyzer
from filemanager import get_words_file, save_data

data_dir = 'data'


def analyze(input_, **kwargs):
    pathname = test_filename if input_[0] == 't' else input_[0]

    analyzer = Analyzer()

    if os.path.isdir(pathname):
        for fname in os.listdir(pathname):
            filename = '{}\\{}'.format(pathname, fname)
            text = get_words_file(filename)
            analyzer.analyze(text)
            print('{} finished'.format(filename))
    else:
        text = get_words_file(pathname)
        analyzer.analyze(text)
        print('{} finished'.format(pathname))

    dicts = save_data(analyzer, fjson=True)

    if kwargs.setdefault('key_a', False):
        for d in dicts:
            show_list(d, num_row=0, reversed=False)


analyze_command = local_command_system.Command()

analyze_command.keys = ['analyze', 'a']
analyze_command.description = 'analyze text for generating new content'
analyze_command.process = analyze
analyze_command.kwargs = {'-d': 'analyze file from directory', '-a': 'show all results'}

import command_system
from tools import show_list, get_words
from main import test_file


def analyze_words(input, kwargs):
    filename = test_file if input[1] == 't' else input[1]

    # args = {'-w': False}
    # fill_args(self.input, args)

    if kwargs.setdefault('-w', False):
        words = dict()
        for word in text:
            words[word] = words.setdefault(word, 0) + 1
        show_list(words)
        print('')


def analyze_words_file(filename):
    len_dict = dict()
    text = get_words(filename)
    for word in text:
        word_len = len(word)
        len_dict[word_len] = len_dict.setdefault(word_len, 0) + 1
    # amount_words = len(text)
    # for length in len_dict:
    #     len_dict[length] = len_dict[length] / amount_words
    show_list(len_dict, num_row=0, reversed=False)


hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello

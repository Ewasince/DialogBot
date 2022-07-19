import json
import os
import pickle

from settings import data_dir
from tools import check_path, service_chars


class Analyzer:
    def __init__(self):
        self.dicts = {}
        self.syll_freq = {}
        self.dicts['syll_freq'] = self.syll_freq
        self.letter_pos = {}
        self.dicts['letter_pos'] = self.letter_pos
        self.letter_pos_by_word = {}
        self.dicts['letter_pos_by_word'] = self.letter_pos_by_word
        self.words_len = {}
        self.dicts['words_len'] = self.words_len

    def analyze(self, text):
        for word in text:
            n = 0
            while n <= len(word):
                letter = word[n] if n < len(word) else ' '

                self.analyze_syllables(n, word)

                self.analyze_letters_pos(n, letter)

                self.analyze_letters_pos_by_word(n, word, letter)

                n += 1

        self.analyze_words_len(text)

    def analyze_file(self, filename):
        text = get_words_file(filename)
        self.analyze(text)

    def analyze_syllables(self, n, word):
        if n == 0:
            syll = ' ' + word[n]
            self.syll_freq[syll] = self.syll_freq.setdefault(syll, 0) + 1
        elif n == len(word):
            syll = word[n - 1] + ' '
            self.syll_freq[syll] = self.syll_freq.setdefault(syll, 0) + 1
        else:
            syll = word[n - 1] + word[n]
            self.syll_freq[syll] = self.syll_freq.setdefault(syll, 0) + 1

    def analyze_letters_pos(self, n, letter):
        # установка средней вероятности появления букв на определённых позициях
        pos_dict = self.letter_pos.setdefault(str(n), dict())
        pos_dict[letter] = pos_dict.setdefault(letter, 0) + 1

    def analyze_letters_pos_by_word(self, n, word, letter):
        if n == len(word):
            return
            # то же что и analyze_letters_pos, только отдельно для каждой длины слов
        len_dict = self.letter_pos_by_word.setdefault(str(len(word)), dict())
        pos_dict = len_dict.setdefault(str(n), dict())
        pos_dict[letter] = pos_dict.setdefault(letter, 0) + 1

    def analyze_words_len(self, text):
        for word in text:
            word_len = str(len(word))
            self.words_len[word_len] = self.words_len.setdefault(word_len, 0) + 1
        # amount_words = len(text)
        # for length in len_dict:
        #     len_dict[length] = len_dict[length] / amount_words
        # show_list(len_dict, num_row=0, reversed=False)
        # print('{} finished'.format(filename))

    def save_dicts(self, path=data_dir, fjson=False) -> list:
        dicts = []
        for d in self.dicts:
            dicts.append(save_dict(d, self.dicts[d], path=path, fjson=fjson))
        return dicts


def save_dict(filename, dictionary, path=data_dir, fjson=False):
    check_path(path)
    filename = '{}\\{}'.format(path, filename)
    if fjson:
        filename += '.json'
        save_class = json
        read_mode = 'r'
        write_mode = 'w'
    else:
        save_class = pickle
        read_mode = 'rb'
        write_mode = 'wb'
    if os.path.exists(filename):
        with open(filename, read_mode) as f:
            last_values: dict = save_class.load(f)
    else:
        last_values = {}
    with open(filename, write_mode) as f:
        try:
            merge_dicts(last_values, dictionary)
            save_class.dump(last_values, f)
            print('{} successfully saved'.format(filename))
        except Exception() as e:
            print(e)
    return last_values


def merge_dicts(base_dict: dict, second_dict: dict):
    for k in second_dict:
        first_item = base_dict.setdefault(k, 0)
        second_item = second_dict[k]
        type1 = type(first_item).__name__
        type2 = type(second_item).__name__
        if type1 == 'dict' and type2 == 'dict':
            base_dict[k] = merge_dicts(first_item, second_item)
        elif type1 != type2:
            base_dict[k] = first_item if type1 == 'dict' else second_item
        elif type1 == 'int' and type2 == 'int':
            base_dict[k] = base_dict.setdefault(k, 0) + second_dict[k]
        else:
            raise Exception('different types in dicts')
    return base_dict


def get_words_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text_raw = f.read()
        text = get_words(text_raw)
        return text
    except UnicodeDecodeError as e:
        print('wrong encoding. please turn file into "utf-8": {}'.format(e))
    except Exception as e:
        print(e)


def get_words(text_raw):
    text = list()
    for row in text_raw.split('\n'):
        for word in row.split(' '):
            word = word.lower().strip(service_chars)
            if len(word) > 0:
                text.append(word)
    return text

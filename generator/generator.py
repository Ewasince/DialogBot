import json
import os.path
import random
from settings import data_dir
from tools import check_path
from commands.bot_command_system.analyze.analyze import Message

tables = dict()
tables_time = {'syll_freq': 0, 'letters_pos': 0, 'letters_pos_by_word': 0, 'words_len': 0}
for n in tables_time:
    tables[n] = dict()


def generate_word_1(**kwargs):
    if refresh_dicts():
        return 'no data'
    syll_freq = tables['syll_freq']
    word = ''
    num = 0
    flag = True
    while flag:
        keys = syll_freq.keys()
        if num == 0:
            keys_ = [n for n in keys if n[0] == ' ']
        else:
            keys_ = [n for n in keys if n[0] == word[num - 1]]
        values = list()
        weights = list()
        for i in keys_:
            values.append(i[1])
            weights.append(syll_freq[i])
        letter = random.choices(values, weights=weights)
        word += letter[0]

        if word[-1] == ' ': flag = False
        num += 1
    return word[:-1]
    pass


def generate_word_2(**kwargs):
    if refresh_dicts():
        return 'no data'
    syll_freq = tables['syll_freq']
    letters_pos = tables['letters_pos']
    word = ''
    num = 0
    flag = True
    while flag:
        keys = get_suitable_keys(syll_freq, word, num)
        values = list()
        weights = list()
        for i in keys:
            next_letter = i[1]
            values.append(next_letter)
            w1 = syll_freq[i]
            letters_freq = letters_pos.setdefault(str(num), dict())
            w2 = letters_freq.setdefault(next_letter, 0)

            if kwargs.setdefault('key_m', False):
                def calc_weight(x1, x2):
                    return (x1 ** 2 + x2 ** 2) ** 0.5
            else:
                def calc_weight(x1, x2):
                    return x1 * x2

            weight = calc_weight(w1, w2)
            weights.append(weight)
        # test = [(v, w) for v, w in zip(values, weights)]
        # test = sorted(test, key=lambda x: x[1], reverse=True)
        # if test[0][1] > test[1][1] * 2:
        #     pass
        letter = random.choices(values, weights=weights)
        word += letter[0]

        if word[-1] == ' ':
            flag = False
        num += 1
    return word[:-1]


def generate_word_3(**kwargs):
    if refresh_dicts():
        return 'no data'

    words_len = tables['words_len']
    syll_freq = tables['syll_freq']
    letters_pos_by_word = tables['letters_pos_by_word']
    values = list(words_len.keys())
    weights = list(words_len.values())
    word_len = int(random.choices(values, weights)[0])

    word = ''
    for num in range(word_len):
        keys = get_suitable_keys(syll_freq, word, num)
        values = list()
        weights = list()
        for i in keys:
            w1 = syll_freq[i]
            next_letter = i[1]
            values.append(next_letter)
            letters_pos = letters_pos_by_word.setdefault(str(word_len), dict())
            letters_freq = letters_pos.setdefault(str(num), dict())
            w2 = letters_freq.setdefault(next_letter, 0)

            if kwargs.setdefault('key_m', False):
                def calc_weight(x1, x2):
                    return (x1 ** 2 + x2 ** 2) ** 0.5
            else:
                def calc_weight(x1, x2):
                    return x1 * x2

            weight = calc_weight(w1, w2)
            weights.append(weight)
        # test = [(v, w) for v, w in zip(values, weights)]
        # test = sorted(test, key=lambda x: x[1], reverse=True)
        # if test[0][1] > test[1][1] * 2:
        #     pass
        letter = random.choices(values, weights=weights)
        word += letter[0]
    return word


def get_suitable_keys(syll_dict, word, num) -> list:
    keys = syll_dict.keys()
    if num == 0:
        return [n for n in keys if n[0] == ' ']
    else:
        return [n for n in keys if n[0] == word[num - 1]]


def refresh_dicts():
    check_path(data_dir)
    for name in tables_time:
        filename = '{}\\{}.json'.format(data_dir, name)
        if not os.path.exists(filename):
            return True
        last_time_modified = os.path.getmtime(filename)
        if tables_time[name] < last_time_modified:
            with open(filename) as f:
                tables[name] = json.load(f)
            tables_time[name] = last_time_modified


class Chat_generator:
    def __init__(self, messages):
        self.messages = messages

    def generate_replica(self) -> str:
        num_parts = self.get_num_parts()
        num_parts = round(num_parts)
        parts = random.choices(self.messages, k=num_parts)
        message = ''
        p: Message
        for p in parts:
            message += self.get_rnd_part(p.text)
            message += ' '
        message = message.strip()
        return message

    @staticmethod
    def get_num_parts():
        num_parts = random.lognormvariate(0.4, 0.4)
        return num_parts

    @staticmethod
    def get_rnd_part(text: str):
        text_len = len(text)
        pos1 = random.randint(0, text_len)
        pos2 = random.randint(0, text_len)
        if pos1 > pos2:
            p = pos1
            pos1 = pos2
            pos2 = p
        find_func = lambda s, p1, p2: s.find(' ', p1, p2)
        rfind_func = lambda s, p1, p2: s.rfind(' ', p1, p2)
        if bool(random.getrandbits(1)):
            find_func_ = find_func
            find_func = rfind_func
            rfind_func = find_func_
        pos1_ = find_func(text, pos1, text_len)
        pos2_ = find_func(text, pos2, text_len)
        if pos1_ == -1:
            pos1_ = rfind_func(text, 0, pos1)
        if pos2_ == -1:
            pos2_ = rfind_func(text, 0, pos2)
        pos1 = 0 if pos1_ == -1 else pos1_
        pos2 = text_len if pos2_ == -1 else pos2_
        if pos1 == pos2:
            if bool(random.getrandbits(1)):
                pos1 = 0
            else:
                pos2 = text_len

        return text[pos1:pos2]
        # mu = text_len / 2
        # sigma = text_len / 6
        # sep_pos = random.normalvariate(mu, sigma)
        # sep_pos = round(sep_pos)
        # if sep_pos < 0:
        #     sep_pos = 0
        # elif sep_pos > text_len:
        #     sep_pos = text_len
        # part = text[:sep_pos]
        # sep_pos_ = part.rfind(' ')
        # if sep_pos_ != -1:
        #     sep_pos += sep_pos_
        # return text[:sep_pos]

import os, json

from tabulate import tabulate
from operator import itemgetter
from settings import data_dir


def main():
    pass


def get_words(filename):
    try:
        text_raw = None
        with open(filename, 'r', encoding='utf-8') as f:
            text_raw = f.read()
        text = list()
        for row in text_raw.split('\n'):
            for word in row.split(' '):
                word = word.lower().strip(service_chars)
                if len(word) > 0:
                    text.append(word)
        return text
    except UnicodeDecodeError as e:
        print('wrong encoding. please turn file into "utf-8": {}'.format(e))
    except Exception as e:
        print(e)


def show_list(list_, num_row=1, reversed=True):
    items = None
    if type(list_).__name__ == 'dict':
        items = list_.items()
        # items = list(list_)
        items = sorted(items, key=itemgetter(num_row), reverse=reversed)
    else:
        items = sorted(list_, key=lambda x: x[num_row], reverse=reversed)
    if type(items[0][1]).__name__ == 'float':
        items = [(n[0], str(round(n[1] * 100, 1)) + '%') for n in items]
    print(tabulate(items))


def fill_args(input_):
    n = 0
    kwargs = {}
    while len(input_) > n:
        item = input_[n]
        if item[0] == '-':
            kwarg = 'key_' + input_.pop(n)[1:]
            value = True
            if len(input_) >= n + 1:
                if input_[n][0] != '-':
                    value = input_.pop(n)
            n -= 1
            kwargs[kwarg] = value
        n += 1
    return kwargs


def check_path(path: str):
    dirs = path.split('\\')
    for n, d in enumerate(dirs):
        cur_path = '\\'.join(dirs[0:n + 1])
        if not os.path.exists(cur_path):
            os.mkdir(cur_path)


def save_dict(filename, dictionary):
    check_path(data_dir)
    filename = '{}\\{}.json'.format(data_dir, filename)
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({}, f)
    with open(filename) as f:
        last_values: dict = json.load(f)
    with open(filename, 'w') as f:
        try:
            merge_dicts(last_values, dictionary)
            json.dump(last_values, f)
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




service_chars = ''
# set(range(0, 256)).remove(range())
for i in range(32, 65):
    service_chars += chr(i)
for i in range(91, 97):
    service_chars += chr(i)
for i in range(122, 127):
    service_chars += chr(i)
service_chars += '—»«'

alphabet = [chr(i) for i in range(1072, 1078)] + ['ё'] + [chr(i) for i in range(1078, 1104)]
alphabet.insert(0, ' ')

if __name__ == '__main__':
    main()

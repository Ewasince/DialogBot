import os

from tabulate import tabulate
from operator import itemgetter


def main():
    pass


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
    if not os.path.exists(path):
        os.makedirs(path)
    # dirs = path.split('\\')
    # for n, d in enumerate(dirs):
    #     cur_path = '\\'.join(dirs[0:n + 1])
    #     if not os.path.exists(cur_path):
    #         os.mkdir(cur_path)


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

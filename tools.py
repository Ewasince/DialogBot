from tabulate import tabulate
from operator import itemgetter


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
    except Exception as e:
        print(e)
        return None


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


def fill_args(input_, args, pos=2):
    if len(input_) > pos:
        for arg in input_[pos:]:
            for i in args:
                if arg == i:
                    args[i] = True


service_chars = ''
# set(range(0, 256)).remove(range())
for i in range(32, 65):
    service_chars += chr(i)
for i in range(91, 97):
    service_chars += chr(i)
for i in range(122, 127):
    service_chars += chr(i)
service_chars += '—»«'

if __name__ == '__main__':
    main()

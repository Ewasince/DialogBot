from tabulate import tabulate
from operator import itemgetter


def main():
    pass


def get_words(filename):
    try:
        text_raw = None
        with open(filename, 'r') as f:
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


def show_list(list, num_row=1, reversed=True):
    items = None
    if type(list).__name__ == 'dict':
        items = list.items()
        items = sorted(items, key=itemgetter(num_row), reverse=reversed)
    else:
        items = sorted(list, key=lambda x: x[num_row], reverse=reversed)
    if type(items[0][1]).__name__ == 'float':
        items = [(n[0], str(round(n[1] * 100, 1)) + '%') for n in items]
    print(tabulate(items))


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

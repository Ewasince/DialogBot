from tabulate import tabulate
from operator import itemgetter


def main():
    analyzer = Analyzer()
    analyzer.console()


class Analyzer:
    syllables = dict()
    input_ = ['']

    def console(self):
        while self.input_[0] not in commands['quit']:
            self.input_ = [n.strip() for n in input('> ').split(' ')]
            if self.input_[0] in commands['analyze_words']:
                self.analyze_words()
            elif self.input_[0] in commands['analyze']:
                self.analyze_syllables()
            elif self.input_[0] in commands['test']:
                self.input_ = (None, 'test.txt')
                self.analyze_words()
                # print('not filled')
            elif self.input_[0] in commands['generate_word_1']:
                self.generate_word_1()
            else:
                print(' '.join(self.input_))

            pass
        pass

    def generate_word_1(self):
        word = ''
        pass

    def analyze_syllables(self):
        filename = self.input_[1]
        text = get_words(filename)
        syllables = dict()
        for word in text:
            n = 0
            while n <= len(word):
                if n == 0:
                    syll = ' ' + word[n]
                    syllables[syll] = syllables.setdefault(syll, 0) + 1
                elif n == len(word):
                    syll = word[n - 1] + ' '
                    syllables[syll] = syllables.setdefault(syll, 0) + 1
                else:
                    syll = word[n - 1] + word[n]
                    syllables[syll] = syllables.setdefault(syll, 0) + 1
                n += 1
        for i in syllables:
            self.syllables[i] = syllables.setdefault(i, 0) + syllables[i]

    def analyze_words(self):
        filename = self.input_[1]
        text = get_words(filename)
        words = dict()
        for word in text:
            words[word] = words.setdefault(word, 0) + 1
        show_dict(words)
        print('')
        len_dict = dict()
        for word in text:
            word_len = len(word)
            len_dict[word_len] = len_dict.setdefault(word_len, 0) + 1
        amount_words = len(text)
        for length in len_dict:
            len_dict[length] = len_dict[length] / amount_words
        # sorted(len_dict)
        show_dict(len_dict, num_row=0, reversed=False)


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


def show_dict(dictionary, num_row=1, reversed=True):
    items = dictionary.items()
    items = sorted(items, key=itemgetter(num_row), reverse=reversed)
    if type(items[0][1]).__name__ == 'float':
        items = [(n[0], str(round(n[1] * 100, 1)) + '%') for n in items]
    print(tabulate(items))


commands_raw = [['quit', 'q'],
                ['analyze', 'a'],
                ['test', 't'],
                ['analyze_words', 'aw'],
                ['generate_word_1', 'gw1']]
commands = dict()
for i in commands_raw:
    commands[i[0]] = tuple(i)
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

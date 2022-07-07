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
                self.analyze()
            elif self.input_[0] in commands['test']:
                self.input_ = (None, 'chehov.txt')
                self.analyze()
                # print('not filled')
            else:
                print(' '.join(self.input_))

            pass
        pass

    def analyze(self):
        try:
            filename = self.input_[1]
            text_raw = None
            with open(filename, 'r') as f:
                text_raw = f.read()
            text = list()
            for i in text_raw.split('\n'):
                for j in i.split(' '):
                    text.append(j.lower().strip(service_chars))
            text = [n for n in text if len(n) > 0]
            self.syllables = dict()
            for word in text:
                n = 0
                while n <= len(word):
                    if n == 0:
                        syll = ' ' + word[n]
                        self.syllables[syll] = self.syllables.setdefault(syll, 0) + 1
                    elif n == len(word):
                        syll = word[n - 1] + ' '
                        self.syllables[syll] = self.syllables.setdefault(syll, 0) + 1
                    else:
                        syll = word[n - 1] + word[n]
                        self.syllables[syll] = self.syllables.setdefault(syll, 0) + 1
                    n += 1
        except Exception as e:
            print(e)

    def analyze_words(self):
        try:
            filename = self.input_[1]
            with open(filename, 'r') as f:
                text_raw = f.read()
                text = list()
                for i in text_raw.split('\n'):
                    for j in i.split(' '):
                        text.append(j.lower().strip(service_chars))
                words = set(text)
                words.remove('')
                words = [(n, 0) for n in words]
                words = dict(words)
                for i in text:
                    try:
                        if i == '':
                            continue
                        words[i] += 1
                    except Exception as e:
                        print(e)
                show_dict(words)
        except Exception as e:
            print(e)


def show_dict(dictionary):
    items = dictionary.items()
    items = sorted(items, key=itemgetter(1), reverse=True)
    print(tabulate(items))


commands_raw = [['quit', 'q'],
                ['analyze', 'a'],
                ['test', 't'],
                ['analyze_words', 'aw']]
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

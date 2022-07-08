import random

from tools import get_words, show_list
from operator import itemgetter
from tabulate import tabulate


def main():
    analyzer = Analyzer()
    analyzer.console()


class Analyzer:
    syllables = dict()
    syllables_pos = dict()
    syllables_amount = dict()
    input_ = ['']

    def console(self):
        print('type \'help\' for more information')
        while self.input_[0] not in commands['quit']:
            self.input_ = [n.strip() for n in input('> ').split(' ')]
            command = self.input_[0]
            if command in commands['analyze_words']:
                self.analyze_words()
            elif command in commands['analyze']:
                self.analyze_syllables()
            elif command in commands['generate_word_1']:
                self.generate_word_1()
            elif command in commands['generate_word_2']:
                self.generate_word_2()
            elif command in commands['show_syllables']:
                if len(self.syllables) > 0:
                    show_list(self.syllables)
                else:
                    print('no data')
            elif command in commands['help']:
                print(tabulate(commands_raw))
            elif command in commands['show_letters']:
                pass
            elif command in commands['show_pos_letters']:
                pass
            elif command in commands['test']:
                pass
                # self.input_ = (None, 'chehov.txt')
                # self.analyze_syllables()
                # self.generate_word_1()
                # print('not filled')
            else:
                print('unknown command \'{}\''.format(command))

            pass
        pass

    def generate_word_1(self):
        if len(self.syllables) == 0:
            print(' no data')
            return
        count = 1
        if len(self.input_) > 1:
            count = int(self.input_[1])
        for j in range(count):
            word = ''
            num = 0
            flag = True
            while flag:
                keys = self.syllables.keys()
                keys_ = list()
                if num == 0:
                    keys_ = [n for n in keys if n[0] == ' ']
                else:
                    keys_ = [n for n in keys if n[0] == word[num - 1]]
                values = list()
                weights = list()
                for i in keys_:
                    values.append(i[1])
                    weights.append(self.syllables[i])
                letter = random.choices(values, weights=weights)
                word += letter[0]

                if word[-1] == ' ': flag = False
                num += 1
            print(word[:-1])
            pass

    def generate_word_2(self):
        if len(self.syllables) == 0:
            print(' no data')
            return
        count = 1
        if len(self.input_) > 1:
            count = int(self.input_[1])
        for j in range(count):
            word = ''
            num = 0
            flag = True
            while flag:
                keys = self.syllables.keys()
                keys_ = list()
                if num == 0:
                    keys_ = [n for n in keys if n[0] == ' ']
                else:
                    keys_ = [n for n in keys if n[0] == word[num - 1]]
                values = list()
                weights = list()
                for i in keys_:
                    values.append(i[1])
                    weights.append(self.syllables[i])
                letter = random.choices(values, weights=weights)
                word += letter[0]

                if word[-1] == ' ': flag = False
                num += 1
            print(word[:-1])
            pass

    def analyze_syllables(self):
        filename = self.input_[1]
        if filename == 't': filename = 'chehov.txt'
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
                letter = word[n] if n < len(word) else ' '
                # установка средней вероятности появления букв на определённых позициях
                pos_dict = self.syllables_amount.setdefault(n, dict())
                pos_dict[word[n]] = pos_dict.setdefault(word[n], 0) + 1

                # то же что и выше, только отдельно для каждой длины слов
                len_dict = self.syllables_pos.setdefault(len(word), dict())
                pos_dict = len_dict.setdefault(n, dict())
                pos_dict[word[n]] = pos_dict.setdefault(word[n], 0) + 1

                n += 1
        for i in syllables:
            self.syllables[i] = syllables.setdefault(i, 0) + syllables[i]
        pass

    def analyze_words(self):
        filename = self.input_[1]
        text = get_words(filename)
        words = dict()
        for word in text:
            words[word] = words.setdefault(word, 0) + 1
        show_list(words)
        print('')
        len_dict = dict()
        for word in text:
            word_len = len(word)
            len_dict[word_len] = len_dict.setdefault(word_len, 0) + 1
        amount_words = len(text)
        for length in len_dict:
            len_dict[length] = len_dict[length] / amount_words
        # sorted(len_dict)
        show_list(len_dict, num_row=0, reversed=False)

    def show_letters(self):
        pass

    def show_pos_letters(self):
        pass


commands_raw = [['help', 'h', 'this command'],
                ['quit', 'q', 'exit the program'],
                ['analyze', 'a', 'analyze text for generating words'],
                ['test', 't', 'test command. its performance configures from program code'],
                ['analyze_words', 'aw', 'analyze the frequency and length of words'],
                ['generate_word_1', 'gw1', '1st algorithm for generating words'],
                ['generate_word_2', 'gw2', '2nd algorithm for generating words'],
                ['show_syllables', 'ss', 'show table with analyzed syllables'],
                ['show_letters', 'sl', 'show frequency of letters on current positions'],
                ['show_pos_letters', 'spl', 'same as \'show letters\' but divided by word length']]
commands = dict()
for i in commands_raw:
    commands[i[0]] = tuple(i[:-1])

if __name__ == '__main__':
    main()

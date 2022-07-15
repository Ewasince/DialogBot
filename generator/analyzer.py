from tools import get_words


class Analyzer:
    def __init__(self):
        self.syll_dict = {}
        self.letter_pos = {}
        self.letter_pos_by_word = {}

    def analyze(self, filename):
        text = get_words(filename)
        for word in text:
            n = 0
            while n <= len(word):
                letter = word[n] if n < len(word) else ' '

                self.analyze_syllables(n, word)

                self.analyze_letters_pos(n, letter)

                self.analyze_letters_pos_by_word(n, word, letter)

                n += 1
        print('{} finished'.format(filename))

    def analyze_syllables(self, n, word):
        if n == 0:
            syll = ' ' + word[n]
            self.syll_dict[syll] = self.syll_dict.setdefault(syll, 0) + 1
        elif n == len(word):
            syll = word[n - 1] + ' '
            self.syll_dict[syll] = self.syll_dict.setdefault(syll, 0) + 1
        else:
            syll = word[n - 1] + word[n]
            self.syll_dict[syll] = self.syll_dict.setdefault(syll, 0) + 1

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

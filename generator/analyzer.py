from tools import get_words


class Analyzer:
    def __init__(self):
        self.syll_dict = {}
        self.letter_pos = {}
        self.letter_pos_by_word = {}

    def analyze_syllables(self, filename):
        text = get_words(filename)
        for word in text:
            n = 0
            while n <= len(word):
                if n == 0:
                    syll = ' ' + word[n]
                    self.syll_dict[syll] = self.syll_dict.setdefault(syll, 0) + 1
                elif n == len(word):
                    syll = word[n - 1] + ' '
                    self.syll_dict[syll] = self.syll_dict.setdefault(syll, 0) + 1
                else:
                    syll = word[n - 1] + word[n]
                    self.syll_dict[syll] = self.syll_dict.setdefault(syll, 0) + 1
                letter = word[n] if n < len(word) else ' '

                # установка средней вероятности появления букв на определённых позициях
                pos_dict = self.letter_pos.setdefault(str(n), dict())
                pos_dict[letter] = pos_dict.setdefault(letter, 0) + 1

                if n == len(word):
                    break
                # то же что и выше, только отдельно для каждой длины слов
                len_dict = self.letter_pos_by_word.setdefault(str(len(word)), dict())
                pos_dict = len_dict.setdefault(str(n), dict())
                pos_dict[letter] = pos_dict.setdefault(letter, 0) + 1

                n += 1
        # for i in syll_dict:
        #     self.syllables[i] = self.syllables.setdefault(i, 0) + syll_dict[i]
        print('{} finished'.format(filename))

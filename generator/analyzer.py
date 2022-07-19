class Analyzer:
    def __init__(self, date_analyzer=None):
        self.dicts = {}
        self.syll_freq = {}
        self.dicts['syll_freq'] = self.syll_freq
        self.letter_pos = {}
        self.dicts['letter_pos'] = self.letter_pos
        self.letter_pos_by_word = {}
        self.dicts['letter_pos_by_word'] = self.letter_pos_by_word
        self.words_len = {}
        self.dicts['words_len'] = self.words_len
        self.date_analyzer = date_analyzer

    def analyze(self, text):
        for word in text:
            n = 0
            while n <= len(word):
                letter = word[n] if n < len(word) else ' '

                self.analyze_syllables(n, word)

                self.analyze_letters_pos(n, letter)

                self.analyze_letters_pos_by_word(n, word, letter)

                n += 1

        self.analyze_words_len(text)

    def analyze_syllables(self, n, word):
        if n == 0:
            syll = ' ' + word[n]
            self.syll_freq[syll] = self.syll_freq.setdefault(syll, 0) + 1
        elif n == len(word):
            syll = word[n - 1] + ' '
            self.syll_freq[syll] = self.syll_freq.setdefault(syll, 0) + 1
        else:
            syll = word[n - 1] + word[n]
            self.syll_freq[syll] = self.syll_freq.setdefault(syll, 0) + 1

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

    def analyze_words_len(self, text):
        for word in text:
            word_len = str(len(word))
            self.words_len[word_len] = self.words_len.setdefault(word_len, 0) + 1
        # amount_words = len(text)
        # for length in len_dict:
        #     len_dict[length] = len_dict[length] / amount_words
        # show_list(len_dict, num_row=0, reversed=False)
        # print('{} finished'.format(filename))


class Date_analyzer:
    def __init__(self, properties: dict):
        self.average_mes = properties.setdefault('average_mes', 0)
        self.amount_mes = properties.setdefault('amount_mes', 0)
        self.last_date = properties.setdefault('last_date', 0)
        self.current_day = properties.setdefault('current_day', 0)

    def analyze_date(self, date):
        date = self.day_from_stamp(date)
        if self.last_date == 0:
            self.last_date = date

        self.current_day += 1
        if date != self.last_date:
            self.last_date = date
            self.average_mes = (self.average_mes * self.amount_mes + self.current_day) / (self.amount_mes + 1)
            self.amount_mes += 1
            self.current_day = 0

    @staticmethod
    def day_from_stamp(d):
        return int(d / 86400)

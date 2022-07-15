import random

syllables = dict()
syllables_amount = dict()


def generate_word_1(**kwargs):
    if len(syllables) == 0:
        return ' no data'
    word = ''
    num = 0
    flag = True
    while flag:
        keys = syllables.keys()
        keys_ = list()
        if num == 0:
            keys_ = [n for n in keys if n[0] == ' ']
        else:
            keys_ = [n for n in keys if n[0] == word[num - 1]]
        values = list()
        weights = list()
        for i in keys_:
            values.append(i[1])
            weights.append(syllables[i])
        letter = random.choices(values, weights=weights)
        word += letter[0]

        if word[-1] == ' ': flag = False
        num += 1
    print(word[:-1])
    pass


def generate_word_2(**kwargs):
    if len(syllables) == 0:
        return 'no data'
    word = ''
    num = 0
    flag = True
    while flag:
        keys = syllables.keys()
        keys_ = list()
        if num == 0:
            keys_ = [n for n in keys if n[0] == ' ']
        else:
            keys_ = [n for n in keys if n[0] == word[num - 1]]
        values = list()
        weights = list()
        for i in keys_:
            values.append(i[1])
            next_letter = i[1]
            w1 = syllables[i]
            pos_dict = syllables_amount.setdefault(num, dict())
            w2 = pos_dict.setdefault(next_letter, 0)

            if kwargs.setdefault('key_m', False):
                def calc_weight(x1, x2):
                    return (x1 ** 2 + x2 ** 2) ** 0.5
            else:
                def calc_weight(x1, x2):
                    return x1 * x2

            weight = calc_weight(w1, w2)
            weights.append(weight)
        test = [(v, w) for v, w in zip(values, weights)]
        test = sorted(test, key=lambda x: x[1], reverse=True)
        if test[0][1] > test[1][1] * 2:
            pass
        letter = random.choices(values, weights=weights)
        word += letter[0]

        if word[-1] == ' ': flag = False
        num += 1
        return word[:-1]


def generate_word_3(**kwargs):
    pass

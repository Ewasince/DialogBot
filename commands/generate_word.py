def generate_word(input_, kwargs):
    count = 1
    if len(input_) > 1:
        count = input_[0]

    generate_func = None
    if kwargs['-1']:
        generate_func = generate_word_1
    elif kwargs['-2']:
        generate_func = generate_word_2
    else:
        generate_func = generate_word_2

    for i in range(count):
        generate_func()


def generate_word_1():
    if len(syllables) == 0:
        print(' no data')
        return
    count = 1
    if len(input_) > 1:
        count = int(input_[1])
    for j in range(count):
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


def generate_word_2():
    args = {'-m': False}
    fill_args(input_, args, pos=1)
    pos_count = 2 if args['-m'] else 1  # position of 'count' argument

    if len(syllables) == 0:
        print('no data')
        return
    count = 1  # count words to generate
    if len(input_) > pos_count:
        try:
            count = int(input_[pos_count])
        except Exception as e:
            print(e)
            pass
    for j in range(count):
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

                if args['-m']:
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
        print(word[:-1])
        pass


generate_word_command = command_system.Command()

generate_word_command.keys = ['generate_word', 'gw']
generate_word_command.description = 'generate new word(s)'
generate_word_command.process = generate
generate_word_command.kwargs = {'-1': 'use first algorithm', '-2': 'use second algorithm'}

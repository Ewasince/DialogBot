import json
import os


def analyze(input_, kwargs):
    pathname = test_file if input_[0] == 't' else input_[0]

    syll_dict, syll_dict_pos, syll_dict_pos_by_word = dict(), dict(), dict()
    if kwargs['-d']:
        try:
            list_files = os.listdir(pathname)
        except Exception as e:
            print(e)
            return
        for fname in list_files:
            filename = '{}\\{}'.format(pathname, fname)
            analyze_syllables(filename, syll_dict, syll_dict_pos, syll_dict_pos_by_word)
    else:
        analyze_syllables(pathname, syll_dict, syll_dict_pos, syll_dict_pos_by_word)

    last_values, last_values_pos, last_values_pos_by_word = dict(), dict(), dict()
    with open('data\\syll_freq.json', 'rw') as f:
        last_values: dict = json.load(f)
        for v in syll_dict:
            last_values[v] += last_values.setdefault(v, 0) + syll_dict[v]
        json.dump(last_values, f)

    with open('data\\syll_freq_pos.json', 'rw') as f:
        last_values_pos: dict = json.load(f)
        for v in syll_dict_pos:
            last_values_pos[v] += last_values_pos.setdefault(v, 0) + syll_dict_pos[v]
        json.dump(last_values_pos, f)

    with open('data\\syll_freq_pos_by_word.json', 'rw') as f:
        last_values_pos_by_word: dict = json.load(f)
        for v in syll_dict_pos_by_word:
            last_values_pos_by_word[v] += last_values_pos_by_word.setdefault(v, 0) + syll_dict_pos_by_word[v]
        json.dump(last_values_pos_by_word, f)

    if kwargs['-a']:
        show_list(last_values, num_row=0, reversed=False)
        show_list(last_values_pos, num_row=0, reversed=False)
        show_list(last_values_pos_by_word, num_row=0, reversed=False)


def analyze_syllables_(filename, syll_dict, syll_dict_pos, syll_dict_pos_by_word):
    text = get_words(filename)
    for word in text:
        n = 0
        while n <= len(word):
            if n == 0:
                syll = ' ' + word[n]
                syll_dict[syll] = syll_dict.setdefault(syll, 0) + 1
            elif n == len(word):
                syll = word[n - 1] + ' '
                syll_dict[syll] = syll_dict.setdefault(syll, 0) + 1
            else:
                syll = word[n - 1] + word[n]
                syll_dict[syll] = syll_dict.setdefault(syll, 0) + 1
            letter = word[n] if n < len(word) else ' '

            # установка средней вероятности появления букв на определённых позициях
            pos_dict = syll_dict_pos.setdefault(n, dict())
            pos_dict[letter] = pos_dict.setdefault(letter, 0) + 1

            if n == len(word):
                break
            # то же что и выше, только отдельно для каждой длины слов
            len_dict = syll_dict_pos_by_word.setdefault(len(word), dict())
            pos_dict = len_dict.setdefault(n, dict())
            pos_dict[letter] = pos_dict.setdefault(letter, 0) + 1

            n += 1
    # for i in syll_dict:
    #     self.syllables[i] = self.syllables.setdefault(i, 0) + syll_dict[i]
    print('{} finished'.format(filename))


analyze_command = command_system.Command()

analyze_command.keys = ['analyze', 'a']
analyze_command.description = 'analyze text for generating new content'
analyze_command.process = analyze
analyze_command.kwargs = {'-d': 'analyze file from directory', '-a': 'show all results'}

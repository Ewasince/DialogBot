from generator import generator
import command_system
from tools import alphabet
from tabulate import tabulate
from generator.generator import refresh_dicts


def show_letters(input_, **kwargs):
    if refresh_dicts():
        print('no data')
        return
    letters = dict()
    letters_pos = generator.tables['letters_pos']
    dict_len = len(letters_pos)
    amount_freq = dict()
    for pos in range(dict_len):
        letter_freq_dict: dict = letters_pos[pos]
        for letter in alphabet:
            frequency = letter_freq_dict.setdefault(letter, 0)
            amount_freq[pos] = amount_freq.setdefault(pos, 0) + frequency

    for pos in range(dict_len):
        letter_freq_dict: dict = letters_pos[pos]
        for letter in alphabet:
            frequency = letter_freq_dict.setdefault(letter, 0)
            letters[letter] = letters.setdefault(letter, list())
            letters[letter].append(str(round(frequency * 100 / amount_freq[pos], 1)))
            pass
    values = list(letters.values())
    for i in range(34):
        values[i].insert(0, alphabet[i])
    headers = list(range(dict_len))
    headers.insert(0, ' ')
    print(tabulate(values, headers=headers, tablefmt="pretty"))
    pass


show_letters_command = command_system.Command()

show_letters_command.keys = ['show_letters', 'sl']
show_letters_command.description = 'show number of letters occurrences'
show_letters_command.process = show_letters
show_letters_command.kwargs = {}

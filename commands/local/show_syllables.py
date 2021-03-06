from generator import generator
from commands import local_command_system
from tools import alphabet
from tabulate import tabulate
from generator.generator import local_generator


def show_syllables(input_, **kwargs):
    if local_generator.refresh_dicts():
        print('no data')
        return
    amounts = list()
    tables = generator.tables
    syll_freq = tables['syll_freq']
    if kwargs.setdefault('key_p', False):
        for ni, i in enumerate(alphabet):
            amounts.append(0)
            for nj, j in enumerate(alphabet):
                key = i + j
                value = syll_freq.setdefault(key, 0)
                amounts[ni] += value

    syllables = []
    for ni, i in enumerate(alphabet):
        syllables.append(list())
        syllables[ni].append(i)
        for nj, j in enumerate(alphabet):
            key = i + j
            value = syll_freq.setdefault(key, 0)
            if kwargs.setdefault('key_p', False):
                value = round(value * 100 / amounts[ni], 2)
            syllables[ni].append(value)
    pass
    headers = alphabet.copy()
    headers.insert(0, ' ')
    print(tabulate(syllables, headers=headers, tablefmt="pretty"))


show_syllables_command = local_command_system.Command()

show_syllables_command.keys = ['show_syllables', 'ss']
show_syllables_command.description = 'show number of syllables occurrences'
show_syllables_command.process = show_syllables
show_syllables_command.kwargs = {'-p': 'show in percents'}

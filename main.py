def main(name):
    input_ = None
    while input_ not in commands['quit']:
        input_ = [n.strip() for n in input('> ').split(' ')]
        if input_[0] in commands['analyze']:
            analyze(input_)
        else:
            print(' '.join(input_))

        pass
    pass


def analyze(input_):
    filename = input_[1]
    try:
        # with open(filename, 'r') as f:
        #     text = [n.strip() for n in f.read().split(' ')]
        #     pass
        #
        # pass
    string = ' -test.  -'
    print(string)

    except Exception as e:
        print(e)


commands_raw = [['quit', 'q'],
                ['analyze', 'a']]
commands = dict()
for i in commands_raw:
    commands[i[0]] = tuple(i)

if __name__ == '__main__':
    main('PyCharm')

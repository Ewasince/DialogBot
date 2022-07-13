def main():
    kwargs(False, None, 0)


def func(x1, x2):
    return ((x1 ** 2) + (x2 ** 2)) ** 0.5


def kwargs(*args):
    for i in args:
        if not i: print('{} yes'.format(i))


if __name__ == '__main__':
    main()

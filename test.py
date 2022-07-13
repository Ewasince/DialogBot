def main():
    kwargs(1, 'd', 3, t=1, t2=2, w=33)
    # while True:
    #     input_ = [float(n.strip()) for n in input('> ').split(' ')]
    #     x = func(input_[0], input_[1])
    #     print(x)


def func(x1, x2):
    return ((x1 ** 2) + (x2 ** 2)) ** 0.5


def kwargs(*args, **kwargs):
    test1 = args
    test2 = kwargs
    pass


if __name__ == '__main__':
    main()

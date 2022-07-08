def main():
    while True:
        input_ = [float(n.strip()) for n in input('> ').split(' ')]
        x = func(input_[0], input_[1])
        print(x)


def func(x1, x2):
    return ((x1 ** 2) + (x2 ** 2)) ** 0.5


if __name__ == '__main__':
    main()

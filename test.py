def main():
    test_ = Test_()
    test_.ustanovka()
    test_.ustanovka = ustanovka_2
    test_.ustanovka()
    test_.proverka()


# def func(x1, x2):
#     return ((x1 ** 2) + (x2 ** 2)) ** 0.5
#
#
# def kwargs(*args):
#     for i in args:
#         if not i: print('{} yes'.format(i))
def ustanovka_2():
    super().pr = 'xoxoxo'


class Test_:
    # def __init__(self):

    def proverka(self):
        ttt = self.pr
        print(ttt)
        pass

    def ustanovka(self):
        self.pr = 'nonono'
        pass


if __name__ == '__main__':
    main()

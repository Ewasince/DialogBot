import json

def main():
    token = 'vk1.a.fr4OtqfZ-6zOESOGHmTVGqvZ8AKmqIQS813EqYZvs85WOyX9G_QintKlTHwADn4ifCqE9eFh1TfX1AQnuoAZuMaWYYhnVUzXxFusmuA9u5Tu8LmF7I0-QMacZiEwvpzKTQzy4hEZdtq8CslvU6HjrqxSMjIwx9bihvqFqBT7R1HdkfvduA9_gwpLA0jl6aCb'
    confirmation_token = 'gfbv784beytivbe4ovt'
    access_token = '080deb67080deb67080deb672a08708a850080d080deb676ac089b6a9779b5921b8dd60'
    test_filename = 'generator/test.txt'
    server_url = 'http://ewasince.pythonanywhere.com/'
    settings = dict()
    settings['token'] = token
    settings['confirmation_token'] = confirmation_token
    settings['access_token'] = access_token
    settings['test_filename'] = test_filename
    with open('settings.json', 'w') as f:
        json.dump(settings, f)
        print('successfully')

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

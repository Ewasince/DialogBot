from bs4 import BeautifulSoup
import requests, os, re
from tools import check_path


# TODO: сделать метод изменения url
# TODO: сделать подсчёт ошибок

def main():
    parser = Parser_ilibrary_ru(url='https://ilibrary.ru/author/chekhov/form.8/l.all/index.html',
                                path='libraries\\chekhov\\')
    parser.start()


class Parser:
    def __init__(self, url, path=''):
        self.url: str = ''
        self.save_path: str = ''
        self.reinit(url, path=path)


    def parse(self):
        pass

    def start(self):
        print('starting parse..')
        self.parse()
        print('parsing finished')

    def reinit(self, url, path=''):
        self.url = url
        self.save_path = path
        if path == '': return
        if not os.path.exists(path):
            check_path(path)


class Parser_ilibrary_ru(Parser):
    def __init__(self, url, path=''):
        super().__init__(url, path=path)
        parts_url = self.url.split('/')
        self.url_site = '{}//{}'.format(parts_url[0], parts_url[2])
        pass

    def parse(self):
        page = requests.get(self.url)
        log_print('{} page code: {}'.format(self.url, page.status_code))
        links = []
        soup = BeautifulSoup(page.text, "html.parser")
        list_ = soup.find('div', class_='list')
        for item in list_.findAll('a'):
            if item is None:
                continue
            link = item.get('href')
            if link is not None and link != '':
                links.append(self.url_site + link)
        for link in links:
            log_print('parsing: {}'.format(link))
            self.parse_link(link)

    def parse_link(self, link):
        page = requests.get(link)
        log_print('{} page code: {}'.format(link, page.status_code))
        texts = []
        soup = BeautifulSoup(page.text, "html.parser")
        text = ''
        title = soup.find('div', class_='title').text
        title = re.sub(r'[\\\n*/|?:<>"]', ' ', title).strip()
        for item in soup.findAll('span', class_='p'):
            paragraph = item.text
            parent = item.parent
            initials = parent.get('class')
            if initials is not None and initials[0] == 'author':
                continue
            if paragraph is not None and paragraph != '':
                text += paragraph + '\n'
        if len(text) == 0:
            return
        filename = '{}{}.txt'.format(self.save_path, title)
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
                log_print('parse {} complete'.format(link))
        except Exception as e:
            log_print('fail to pase {}, due to {}'.format(link, e))
        pass


log_filename = 'log.txt'
if os.path.exists(log_filename):
    os.remove(log_filename)


def log_print(text, *args, **kwargs):
    with open(log_filename, 'a') as f:
        f.write(text + '\n')
    print(text, *args, **kwargs)


if __name__ == '__main__':
    main()

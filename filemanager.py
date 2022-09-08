import json
import os
import pickle

from settings import data_dir, data_chats_dir
from tools import check_path, service_chars
from generator.analyzer import Analyzer, DateAnalyzer


def save_class_properties(date_analyzer: DateAnalyzer, path=data_dir):
    filename = f'{path}\\properties'
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            loaded_prop = pickle.load(f)
    else:
        loaded_prop = {'amount_mes': 0, 'average_mes': 0, 'current_day': 0, 'last_date': 0, 'last_id': 0}
    loaded_prop['amount_mes'] = date_analyzer.amount_mes
    loaded_prop['average_mes'] = date_analyzer.average_mes
    loaded_prop['current_day'] = date_analyzer.current_day
    loaded_prop['last_date'] = date_analyzer.last_date
    with open(filename, 'wb') as f:
        pickle.dump(loaded_prop, f)


def save_properties(properties: dict, path=data_dir):
    filename = f'{path}\\properties'
    with open(filename, 'wb') as f:
        pickle.dump(properties, f)


def load_properties(path=data_dir) -> dict:
    filename = f'{path}\\properties'
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return {}


def refresh_properties(path=data_dir, **kwargs):
    properties = load_properties(path)
    for k in kwargs:
        properties[k] = kwargs[k]
    save_properties(properties, path)


# def save_date_properties(date_a: Date_analyzer, path=data_dir):
#     refresh_properties(path=path, average_mes=date_a.average_mes, amount_mes=date_a.amount_mes,
#                        last_date=date_a.amount_mes, current_day=date_a.current_day)


def save_dict(filename, dictionary, path=data_dir, fjson=False):
    check_path(path)
    filename = '{}\\{}'.format(path, filename)
    if fjson:
        filename += '.json'
        save_class = json
        read_mode = 'r'
        write_mode = 'w'
    else:
        save_class = pickle
        read_mode = 'rb'
        write_mode = 'wb'
    if os.path.exists(filename):
        with open(filename, read_mode) as f:
            last_values: dict = save_class.load(f)
    else:
        last_values = {}
    with open(filename, write_mode) as f:
        try:
            merge_dicts(last_values, dictionary)
            save_class.dump(last_values, f)
            print('{} successfully saved'.format(filename))
        except Exception() as e:
            print(e)
    return last_values


def merge_dicts(base_dict: dict, second_dict: dict):
    for k in second_dict:
        first_item = base_dict.setdefault(k, 0)
        second_item = second_dict[k]
        type1 = type(first_item).__name__
        type2 = type(second_item).__name__
        if type1 == 'dict' and type2 == 'dict':
            base_dict[k] = merge_dicts(first_item, second_item)
        elif type1 != type2:
            base_dict[k] = first_item if type1 == 'dict' else second_item
        elif type1 == 'int' and type2 == 'int':
            base_dict[k] = base_dict.setdefault(k, 0) + second_dict[k]
        else:
            raise Exception('different types in dicts')
    return base_dict


def get_words_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text_raw = f.read()
        text = get_words(text_raw)
        return text
    except UnicodeDecodeError as e:
        print('wrong encoding. please turn file into "utf-8": {}'.format(e))
    except Exception as e:
        print(e)


def get_words(text_raw):
    text = list()
    for row in text_raw.split('\n'):
        for word in row.split(' '):
            word = word.lower().strip(service_chars)
            if len(word) > 0:
                text.append(word)
    return text


def save_dicts(analyzer: Analyzer, path=data_dir, fjson=False) -> list:
    dicts = []
    for d in analyzer.dicts:
        dicts.append(save_dict(d, analyzer.dicts[d], path=path, fjson=fjson))
    return dicts


def save_data(analyzer: Analyzer, path=data_dir, fjson=False) -> list:
    dicts = save_dicts(analyzer, path=path, fjson=fjson)
    if analyzer.date_analyzer is not None:
        save_class_properties(analyzer.date_analyzer, path=path)
    return dicts


def analyze_file(analyzer, filename):
    text = get_words_file(filename)
    analyzer.analyze(text)


def get_chat_path(event) -> str:
    chat_id = event.chat_id
    path = f'{data_chats_dir}\\{chat_id}'
    return path

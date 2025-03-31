import json
ALPHABET = "abcdefghijklmnopqrstuvwxyz' ,"

ENCRYPTED = 'encrypted.txt'
KEY = 'key.json'
PLANE_TEXT = 'plane_text.txt'


def write_txt(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)


def read_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        file = file.read().strip()
        return file


def load_key(key_name, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        txt_key = json.load(f)
        return txt_key.get(key_name)

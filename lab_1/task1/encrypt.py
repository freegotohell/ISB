import json
from const import ALPHABET, CURRENT_INDEX

with open('plane_text.txt', 'r', encoding='utf-8') as f:
    plane_text = f.read().strip()

with open('key.json', 'r', encoding='utf-8') as f:
    key_data = json.load(f)
    key = key_data['key']


def get_new_symbol(old, keyed_symbol):
    try:
        current_index = ALPHABET.index(old.lower())
        key_index = ALPHABET.index(keyed_symbol.lower())
        if current_index + key_index >= len(ALPHABET):
            new_index = current_index + key_index - len(ALPHABET)
        else:
            new_index = current_index + key_index
        return ALPHABET[new_index]
    except ValueError:
        return old


def get_key_symbol():
    if CURRENT_INDEX + 1 >= len(key):
        CURRENT_INDEX = 0
    encrypted_s = key[CURRENT_INDEX]
    CURRENT_INDEX += 1
    return encrypted_s


encrypted = ""
for symbol in plane_text:
    encrypted += get_new_symbol(symbol, get_key_symbol())

with open('encrypted.txt', 'w', encoding='utf-8') as f:
    f.write(encrypted)


print(f"encrypted: {encrypted}")

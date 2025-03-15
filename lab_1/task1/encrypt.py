import json
from const import ALPHABET


CURRENT_INDEX = 0

with open('plane_text.txt', 'r', encoding='utf-8') as f:
    plane_text = f.read().strip()

with open('key.json', 'r', encoding='utf-8') as f:
    hash_key = json.load(f)['key']


def get_new_symbol(old, hashed_symbol):
    try:
        current_index = ALPHABET.index(old.lower())
        hash_index = ALPHABET.index(hashed_symbol.lower())
        if current_index + hash_index >= len(ALPHABET):
            new_index = current_index + hash_index - len(ALPHABET)
        else:
            new_index = current_index + hash_index
        return ALPHABET[new_index]
    except ValueError:
        return old


def get_hash_symbol():
    global CURRENT_INDEX
    if CURRENT_INDEX + 1 >= len(hash_key):
        CURRENT_INDEX = 0
    encrypted_s = hash_key[CURRENT_INDEX]
    CURRENT_INDEX += 1
    return encrypted_s


encrypted = ""
for symbol in plane_text:
    encrypted += get_new_symbol(symbol, get_hash_symbol())

with open('encrypted.txt', 'w', encoding='utf-8') as f:
    f.write(encrypted)

print(f"Result: {encrypted}")

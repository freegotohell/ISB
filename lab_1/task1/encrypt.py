import json
from const import ALPHABET

CURRENT_INDEX = 0

with open('plane_text.txt', 'r', encoding='utf-8') as f:
    phrase = f.read().strip()

with open('key.json', 'r', encoding='utf-8') as f:
    hash_key = json.load(f)['key']


def encrypt_symbol(plane_text: str) -> str:
    """
    encrypt a single character using the vigenere cipher algorithm
    cycle through the key by global index
    :param plane_text: character to encrypt
    :return: encrypted character or original if there is no such character in alphabet
    """
    global CURRENT_INDEX
    if CURRENT_INDEX + 1 >= len(hash_key):
        CURRENT_INDEX = 0
    hashed_symbol = hash_key[CURRENT_INDEX]
    CURRENT_INDEX += 1

    try:
        current_index = ALPHABET.index(plane_text.lower())
        hash_index = ALPHABET.index(hashed_symbol.lower())
        if current_index + hash_index >= len(ALPHABET):
            new_index = current_index + hash_index - len(ALPHABET)
        else:
            new_index = current_index + hash_index
        return ALPHABET[new_index]
    except ValueError:
        return plane_text


def main():
    encrypted_txt = ""
    for symbol in phrase:
        encrypted_txt += encrypt_symbol(symbol)

    with open('encrypted.txt', 'w', encoding='utf-8') as f:
        f.write(encrypted_txt)

    print(f"result: {encrypted_txt}")


if __name__ == '__main__':
    main()

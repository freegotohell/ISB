from const import *

CURRENT_INDEX = 0

text = read_txt(PLANE_TEXT)
hash_key = load_key('key', KEY)


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
    for symbol in text:
        encrypted_txt += encrypt_symbol(symbol)

    write_txt(encrypted_txt, ENCRYPTED)
    print(f"result: {encrypted_txt}")


if __name__ == '__main__':
    main()

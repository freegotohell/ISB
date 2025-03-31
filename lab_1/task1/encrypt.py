from const import *
from vigenere import Vigenere

text = read_txt(PLANE_TEXT)
hash_key = load_key('key', KEY)
vigenere = Vigenere(hash_key)


def main():
    encrypted_txt = ""
    for symbol in text:
        encrypted_txt += vigenere.encrypt_symbol(symbol, ALPHABET)
    write_txt(encrypted_txt, ENCRYPTED)
    print(f"result: {encrypted_txt}")


if __name__ == '__main__':
    main()

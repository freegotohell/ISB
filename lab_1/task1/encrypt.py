from lab_1.work_file import *
from vigenere import Vigenere


def main():
    task1 = read_json("../settings.json").get("task1")
    text = read_txt(task1["PLANE_TEXT"])
    hash_key = load_key('key', task1["KEY"])
    vigenere = Vigenere(hash_key)
    encrypted_txt = ""
    for symbol in text:
        encrypted_txt += vigenere.encrypt_symbol(symbol, task1["ALPHABET"])
    write_txt(encrypted_txt, task1["ENCRYPTED"])
    print(f"result: {encrypted_txt}")


if __name__ == '__main__':
    main()

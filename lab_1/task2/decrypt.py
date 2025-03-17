import json
from const import FREQUENCY


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        file = file.read().strip()
        cfile = file.replace("\n", "")
        return cfile


def get_frequency(text: str) -> dict:
    frequency_dict = {}
    for i in set(text):
        frequency_dict[i] = text.count(i) / len(text)
    return dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))


def main():
    filename = 'encrypted.txt'
    encrypted_text = read_file(filename)

    if encrypted_text:
        freq_dict = get_frequency(encrypted_text)

        with open('frequency.json', 'w', encoding='utf-8') as file:
            json.dump(freq_dict, file, indent=4, ensure_ascii=False)

        print(freq_dict)


if __name__ == "__main__":
    main()

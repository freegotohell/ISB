from const import *


def get_frequency(text: str) -> dict:
    frequency_dict = {}
    size = len(text)
    for i in text:
        frequency_dict[i] = frequency_dict.get(i, 0) + 1
    for i in frequency_dict:
        frequency_dict[i] = frequency_dict[i] / size
    return dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))


def get_key(dict1, dict2):
    new_dict = {}
    for i in range(len(dict1)):
        key1 = list(dict1.keys())[i]
        key2 = list(dict2.keys())[i]
        new_dict[key1] = key2
    return new_dict


def replace(text, key):
    decrypted = ""
    for i in text:
        decrypted_s = key.get(i)
        if decrypted_s is None:
            decrypted_s = ''
        decrypted += decrypted_s
    return decrypted


def main():
    encrypted_text = read_txt(ENCRYPTED)

    if encrypted_text:
        freq_dict = get_frequency(encrypted_text)
        write_json(freq_dict, FREQUENCY_FILE)

        new_dict = get_key(freq_dict, FREQUENCY)
        write_json(new_dict, KEY)

        result = replace(encrypted_text, new_dict)
        write_txt(result, DECRYPTED)

        txt_key = read_json(KEY2)
        txt_nice = replace(result, txt_key)
        write_txt(txt_nice, READABLE)
        print(txt_nice)


if __name__ == "__main__":
    main()

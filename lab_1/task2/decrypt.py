from const import *


def get_frequency(text: str) -> dict:
    """
    calculates the frequency of each character in the text
    :param text: input text
    :return: sorted dictionary where keys are characters and values are their frequencies
    """
    frequency_dict = {}
    size = len(text)
    for i in text:
        frequency_dict[i] = frequency_dict.get(i, 0) + 1
    for i in frequency_dict:
        frequency_dict[i] = frequency_dict[i] / size
    return dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))


def get_key(dict1: dict, dict2: dict) -> dict:
    """
    creates a key by mapping keys from two input dictionaries based on their order
    :param dict1: keys from this dictionary will be the keys in the output dictionary, calculated freq
    :param dict2: keys from this dictionary will be the values in the output dictionary, sample freq
    :return: dictionary where each key from dict1 is mapped to the corresponding key from dict2
    """
    new_dict = {}
    for i in range(len(dict1)):
        key1 = list(dict1.keys())[i]
        key2 = list(dict2.keys())[i]
        new_dict[key1] = key2
    return new_dict


def replace(text: str, key: dict) -> str:
    """
    replaces characters in the input text based on the provided key
    :param text: input text
    :param key: dictionary where keys are characters to be replaced and values are their replacements
    :return: new text where characters replaced according to the key, not found in the key aren't replaced
    """
    decrypted = ""
    for i in text:
        decrypted_s = key.get(i)
        if decrypted_s is None:
            decrypted_s = i
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

import json


def read_txt(filename: str) -> str:
    """
    read and return the content of a text file
    :param filename: path to the text file to be read
    :return: content of the file as a string
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file = file.read().strip()
            return file
    except FileNotFoundError:
        print(f"file {filename} not found")
    except Exception as e:
        print(f"error: {e}")


def read_json(filename: str) -> dict:
    """
    read and parse a JSON file into a dictionary
    :param filename: path to the text file to be read
    :return: parsed JSON data as a dictionary
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"file {filename} not found")
    except json.JSONDecodeError:
        print(f"file {filename} isn't correct JSON.")
    except Exception as e:
        print(f"error: {e}")


def write_json(dictionary: dict, filename: str) -> None:
    """
    write a dictionary to a file in JSON format
    :param dictionary: dictionary to be written as JSON
    :param filename: path to the output JSON file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, indent=4, ensure_ascii=False)
    except Exception as e:
        raise Exception(f"An error occurred when saving the file: {e}")

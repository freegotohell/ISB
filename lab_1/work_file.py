import json


def write_txt(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
    except Exception as e:
        raise Exception(f"An error occurred when saving the file: {e}")


def read_txt(filename: str) -> str:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file = file.read().strip()
            return file
    except FileNotFoundError:
        print(f"file {filename} not found")
    except Exception as e:
        print(f"error: {e}")


def load_key(key_name, filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            txt_key = json.load(file)
            return txt_key.get(key_name)
    except FileNotFoundError:
        print(f"file {filename} not found")
    except json.JSONDecodeError:
        print(f"file {filename} isn't correct JSON.")
    except Exception as e:
        print(f"error: {e}")


def read_json(filename: str) -> dict[str, str]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"file {filename} not found")
    except json.JSONDecodeError:
        print(f"file {filename} isn't correct JSON.")
    except Exception as e:
        print(f"error: {e}")


def write_json(dictionary, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, indent=4, ensure_ascii=False)
    except Exception as e:
        raise Exception(f"An error occurred when saving the file: {e}")


class Vigenere:
    def __init__(self, key):
        self.key = key
        self.current_index = 0

    def encrypt_symbol(self, plane_text: str, alphabet) -> str:
        """
        encrypt a single character using the vigenere cipher algorithm
        :param plane_text: character to encrypt
        :param alphabet: const alphabet
        :return: encrypted character or original if there is no such character in alphabet
        """
        hashed_symbol = self.key[self.current_index]
        self.current_index += 1
        if self.current_index + 1 > len(self.key):
            self.current_index = 0

        try:
            current_index = alphabet.index(plane_text.lower())
            hash_index = alphabet.index(hashed_symbol.lower())
            if current_index + hash_index >= len(alphabet):
                new_index = current_index + hash_index - len(alphabet)
            else:
                new_index = current_index + hash_index
            return alphabet[new_index]
        except ValueError:
            return plane_text

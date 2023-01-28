import json
import base64
import random
import string

letters = string.printable

ENCODED_DATA_KEY: str = 'to_encode'


class Tokenizer:
    def create_access_token(self) -> bytes:
        access_token: bytes = self.create_basic_token(add_random_part=True, length=150)
        return access_token

    def create_update_token(self) -> bytes:
        update_token: bytes = self.create_basic_token(add_random_part=True, length=330)
        return update_token

    def create_imprint_token(self) -> bytes:
        imprint_token: bytes = self.create_basic_token(add_random_part=True, length=5)
        return imprint_token

    @staticmethod
    def extract_encoded_data(token: bytes) -> any:
        loaded = json.loads(base64.standard_b64decode(token))
        if ENCODED_DATA_KEY in loaded:
            return json.loads(base64.standard_b64decode(token))[ENCODED_DATA_KEY]
        return {}

    @staticmethod
    def create_basic_token(to_encode: any = "", add_random_part: bool = False, length: int = 0):
        data = {}
        if to_encode != "":
            data = {
                ENCODED_DATA_KEY: to_encode,
            }
        if add_random_part:
            data[''] = ''.join(random.choice(letters) for _ in range(length))
        return base64.b64encode(json.dumps(data).encode())

    @staticmethod
    def decode_token(token: bytes) -> str:
        return token.decode('ascii')

    @staticmethod
    def encode_token(token_str: str) -> bytes:
        return token_str.encode('ascii')

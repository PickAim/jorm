import os
import base64
import hashlib

from .tokens import Tokenizer

HASH_KEY: str = 'hash'
SALT_KEY: str = 'salt'
IT_NUM_KEY: str = 'it_num'
DKLEN_KEY: str = 'dklen'


class Hasher:
    @staticmethod
    def hash(input_sequence: str, salt: bytes = os.urandom(32), iteration_num: int = 123456, dklen: int = 128) -> bytes:
        key = hashlib.pbkdf2_hmac('sha256', input_sequence.encode('utf-8'), salt, iteration_num, dklen=dklen)
        data_to_save = {
            HASH_KEY: base64.b64encode(key).decode('ascii'),
            SALT_KEY: base64.b64encode(salt).decode('ascii'),
            IT_NUM_KEY: iteration_num,
            DKLEN_KEY: dklen
        }
        return Tokenizer.create_basic_token(data_to_save)

    @staticmethod
    def verify(str_to_check: str, hashed_token: bytes) -> bool:
        encoded_data = Tokenizer.extract_encoded_data(hashed_token)
        salt: bytes = base64.standard_b64decode(encoded_data[SALT_KEY])
        iteration_num: int = encoded_data[IT_NUM_KEY]
        dklen: int = encoded_data[DKLEN_KEY]
        to_check = Tokenizer.extract_encoded_data(Hasher.hash(str_to_check, salt, iteration_num, dklen))
        return to_check[HASH_KEY] == encoded_data[HASH_KEY]

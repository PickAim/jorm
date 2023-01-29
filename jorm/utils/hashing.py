import os
import base64
import hashlib
from dataclasses import dataclass

from jorm.utils.tokens import Tokenizer


@dataclass
class Hasher:
    HASH_KEY: str = 'hash'
    SALT_KEY: str = 'salt'
    IT_NUM_KEY: str = 'it_num'
    DKLEN_KEY: str = 'dklen'
    tokenizer: Tokenizer = Tokenizer()

    def hash(self, input_sequence: str, salt: bytes = os.urandom(32),
             iteration_num: int = 123456, dklen: int = 128) -> str:
        key = hashlib.pbkdf2_hmac('sha256', input_sequence.encode('utf-8'), salt, iteration_num, dklen=dklen)
        data_to_save = {
            self.HASH_KEY: base64.b64encode(key).decode('ascii'),
            self.SALT_KEY: base64.b64encode(salt).decode('ascii'),
            self.IT_NUM_KEY: iteration_num,
            self.DKLEN_KEY: dklen
        }
        return self.tokenizer.create_basic_token(data_to_save)

    def verify(self, str_to_check: str, hashed_token: str) -> bool:
        encoded_data = self.tokenizer.extract_encoded_data(hashed_token)
        salt: bytes = base64.standard_b64decode(encoded_data[self.SALT_KEY])
        iteration_num: int = encoded_data[self.IT_NUM_KEY]
        dklen: int = encoded_data[self.DKLEN_KEY]
        to_check = self.tokenizer.extract_encoded_data(self.hash(str_to_check, salt, iteration_num, dklen))
        return to_check[self.HASH_KEY] == encoded_data[self.HASH_KEY]

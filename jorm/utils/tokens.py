import random
import string
from dataclasses import dataclass
from datetime import timedelta, datetime

from jose import jwt

letters = string.printable


@dataclass
class Tokenizer:
    SECRET_KEY = "3ARtLTXRn9urnRK9d6rzDbj5Jy5vp/iG8dlaseZliD4="
    TIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    USER_ID_KEY = "u_id"
    EXPIRES_TIME_KEY = "exp_time"
    ENCODED_DATA_KEY = "encoded_data"

    def create_access_token(self, user_id: int, expires_delta: timedelta = timedelta(minutes=5.0)) -> str:
        return self.create_session_token(user_id, expires_delta, add_random_part=True, length_of_rand_part=60)

    def create_update_token(self, user_id: int) -> str:
        return self.create_session_token(user_id, add_random_part=True, length_of_rand_part=245)

    def create_imprint_token(self, user_id: int) -> str:
        return self.create_session_token(user_id, add_random_part=True, length_of_rand_part=5)

    def create_session_token(self, user_id: int, expires_delta: timedelta = None,
                             add_random_part: bool = False, length_of_rand_part: int = 0) -> str:
        to_encode = {
            self.USER_ID_KEY: user_id,
        }
        if expires_delta is not None:
            if expires_delta:
                expires_in = datetime.now() + expires_delta
            else:
                expires_in = datetime.now() + timedelta(minutes=30)
            expires_in = expires_in.replace(microsecond=0)
            to_encode[self.EXPIRES_TIME_KEY] = str(expires_in)
        return self.create_basic_token(to_encode, add_random_part, length_of_rand_part)

    def extract_encoded_data(self, token: str) -> any:
        decoded_data = jwt.decode(token, self.SECRET_KEY)
        if self.ENCODED_DATA_KEY in decoded_data:
            return decoded_data[self.ENCODED_DATA_KEY]
        return {}

    def is_token_expired(self, token: str) -> bool:
        extracted_data = self.extract_encoded_data(token)
        if self.EXPIRES_TIME_KEY in extracted_data:
            return datetime.now() > datetime.strptime(extracted_data[self.EXPIRES_TIME_KEY], self.TIME_FORMAT)
        return False

    def create_basic_token(self, to_encode=None, add_random_part: bool = False, length_of_rand_part: int = 0) -> str:
        data = {}
        if to_encode is not None:
            data = {
                self.ENCODED_DATA_KEY: to_encode,
            }
        if add_random_part:
            data[''] = ''.join(random.choice(letters) for _ in range(length_of_rand_part))
        return jwt.encode(data, self.SECRET_KEY)

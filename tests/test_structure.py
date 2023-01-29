import datetime
import unittest
from datetime import date

from jorm.utils.tokens import Tokenizer

from jorm.market.infrastructure import Warehouse, Address, HandlerType
from jorm.market.items import ClientProduct, ProductHistoryUnit, ProductHistory
from jorm.market.service import FrequencyResult, FrequencyRequest
from jorm.utils.hashing import Hasher


class MyTestCase(unittest.TestCase):
    def test_hardcode_objects_creating(self):
        product_history = ProductHistory([ProductHistoryUnit(1, 1, date.today()),
                                          ProductHistoryUnit(3, 6, date.today())])
        client_products = [ClientProduct("Coffee", 10, 12456862, product_history, "g", "g")]
        warehouse = Warehouse("wb", 123, HandlerType.MARKETPLACE, Address(), client_products)

        self.assertEqual("wb", warehouse.__str__())
        self.assertEqual("Coffee (12456862)", warehouse.products[0].__str__())
        self.assertEqual(f"{date.today()}: cost - 1; leftover - 1;\n{date.today()}: cost - 3; leftover - 6;",
                         warehouse.products[0].history.__str__())

    def test_frequency_result(self):
        freq: dict[int, int] = {1: 4, 2: 5, 3: 6}
        freq_result = FrequencyResult(FrequencyRequest(datetime.datetime.now(), ""), freq)
        x, y = freq_result.get_graph_coordinates()
        self.assertEqual(x, [1, 2, 3])
        self.assertEqual(y, [4, 5, 6])

    def test_hasher_verify(self):
        password: str = "password"
        hasher = Hasher()
        hashed = hasher.hash(password)
        print(hashed)
        self.assertTrue(hasher.verify(password, hashed))

    def test_tokens_lifetime(self):
        tokenizer = Tokenizer()
        access_token = tokenizer.create_access_token(123, datetime.timedelta(microseconds=1))
        update_token = tokenizer.create_update_token(123)
        imprint_token = tokenizer.create_imprint_token(123)

        self.assertTrue(tokenizer.is_token_expired(access_token))
        self.assertFalse(tokenizer.is_token_expired(update_token))
        self.assertFalse(tokenizer.is_token_expired(imprint_token))


if __name__ == '__main__':
    unittest.main()

import datetime
import unittest
from datetime import date

from jorm.market.infrastructure import Warehouse, Address, HandlerType
from jorm.market.items import ClientProduct, ProductHistoryUnit, ProductHistory
from jorm.market.service import FrequencyResult, FrequencyRequest


class MyTestCase(unittest.TestCase):
    def test_hardcode_objects_creating(self):
        product_history = ProductHistory([ProductHistoryUnit(1, 1, date.today()),
                                          ProductHistoryUnit(3, 6, date.today())])
        client_products = [ClientProduct("Coffee", 10, 12456862, "g", "g", history=product_history)]
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


if __name__ == '__main__':
    unittest.main()

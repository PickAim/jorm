import datetime
import unittest
from datetime import date

from jorm.market.infrastructure import Warehouse, Address, HandlerType
from jorm.market.items import ClientProduct, ProductHistoryUnit, ProductHistory
from jorm.market.service import FrequencyResult, FrequencyRequest
from jorm.support.types import ProductSpecifyDict, StorageDict


class MyTestCase(unittest.TestCase):
    def test_hardcode_objects_creating(self):
        product_specify_dict = ProductSpecifyDict()
        product_specify_dict['s'] = 15
        product_specify_dict['l'] = 25
        product_specify_dict['p'] = 35

        storage_dict = StorageDict()
        storage_dict[123] = product_specify_dict

        self.assertEqual(75, storage_dict.get_all_leftovers())

        product_history = ProductHistory([ProductHistoryUnit(1, date.today(), storage_dict),
                                          ProductHistoryUnit(3, date.today(), storage_dict)])
        client_products = [ClientProduct("Coffee", 10, 12456862, "g", "g", history=product_history)]
        warehouse = Warehouse("wb", 123, HandlerType.MARKETPLACE, Address(), client_products)

        self.assertEqual("wb", warehouse.__str__())
        self.assertEqual("Coffee (12456862)", warehouse.products[0].__str__())
        self.assertEqual(f"{date.today()}: cost - 1; leftover - " + "{123: {'s': 15, 'l': 25, 'p': 35}};\n"
                         + f"{date.today()}: cost - 3; leftover - " + "{123: {'s': 15, 'l': 25, 'p': 35}};",
                         warehouse.products[0].history.__str__())

    def test_frequency_result(self):
        freq: dict[int, int] = {1: 4, 2: 5, 3: 6}
        freq_result = FrequencyResult(FrequencyRequest(datetime.datetime.now(), ""), freq)
        x, y = freq_result.get_graph_coordinates()
        self.assertEqual(x, [1, 2, 3])
        self.assertEqual(y, [4, 5, 6])

    def test_dict_wrong_types_insertion(self):
        product_specify_dict = ProductSpecifyDict()
        print(str(product_specify_dict))
        try:
            product_specify_dict[1254] = "s"
        except (Exception, Exception):
            self.assertTrue(True)
        storage_dict = StorageDict()
        try:
            storage_dict["s"] = 1545
        except (Exception, Exception):
            self.assertTrue(True)
            return
        self.fail()


if __name__ == '__main__':
    unittest.main()

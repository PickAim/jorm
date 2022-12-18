import unittest
from datetime import date

from market.infrastructure import Warehouse, Address
from market.items import ClientProduct, ProductHistoryUnit, ProductHistory


class MyTestCase(unittest.TestCase):
    def test_hardcode_objects_creating(self):
        warehouse = Warehouse("wb", 123, 15, Address())
        product_history = ProductHistory([ProductHistoryUnit(1, 1, date.today()),
                                          ProductHistoryUnit(3, 6, date.today())])
        client_products = [
            ClientProduct("Coffee", "g", "g", 10, 12456862, product_history)]
        warehouse.set_products(client_products)

        self.assertEqual("wb", warehouse.__str__())
        self.assertEqual("Coffee (12456862)", warehouse.get_products()[0].__str__())
        self.assertEqual(f"{date.today()}: cost - 1; leftover - 1;\n{date.today()}: cost - 3; leftover - 6;\n",
                         warehouse.get_products()[0].get_history().__str__())


if __name__ == '__main__':
    unittest.main()

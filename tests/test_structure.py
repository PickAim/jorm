import datetime
import unittest

from jorm.market.infrastructure import Warehouse, Address, HandlerType
from jorm.market.items import ProductHistoryUnit, ProductHistory, Product
from jorm.support.types import StorageDict, SpecifiedLeftover


class StructureTest(unittest.TestCase):
    def test_hardcode_objects_str_formatting(self):
        storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        saved_time = datetime.datetime.utcnow()

        product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
                                          ProductHistoryUnit(3, saved_time, storage_dict)])

        client_products = [
            Product("Coffee", 10, 12456862, 4.3, "brand", "seller", "g", "g", history=product_history)
        ]
        warehouse = Warehouse("wb", 123, HandlerType.MARKETPLACE,
                              Address(), main_coefficient=1.0, products=client_products)

        self.assertEqual("wb", warehouse.__str__())
        self.assertEqual("Coffee (12456862)", warehouse.products[0].__str__())
        self.assertEqual(f"{datetime.datetime(2021, 1, 1)}: cost - 1; leftover - "
                         + "{123: [s: 15, l: 25, p: 35]};\n"
                         + f"{saved_time}: cost - 3; leftover - "
                         + "{123: [s: 15, l: 25, p: 35]};",
                         warehouse.products[0].history.__str__())

    def test_hardcode_leftovers_calculation(self):
        storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        after_trade_storage_dict = StorageDict()
        after_trade_storage_dict[123] = [SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
                                          ProductHistoryUnit(3, datetime.datetime.utcnow(), storage_dict),
                                          ProductHistoryUnit(5, datetime.datetime.utcnow(), after_trade_storage_dict)])

        self.assertEqual(75, storage_dict.get_all_leftovers())
        self.assertEqual(60, after_trade_storage_dict.get_all_leftovers())
        self.assertEqual(15, product_history.get_last_month_trade_count(datetime.datetime.utcnow()))

    def test_downturn_calculations0(self):
        storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]
        storage_dict[321] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        after_trade_storage_dict = StorageDict()
        after_trade_storage_dict[123] = [SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]
        after_trade_storage_dict[321] = [SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
                                          ProductHistoryUnit(3, datetime.datetime.utcnow(), storage_dict),
                                          ProductHistoryUnit(5, datetime.datetime.utcnow(), after_trade_storage_dict)])

        down = product_history.get_leftovers_downturn(datetime.datetime.utcnow())
        self.assertEqual(-15, down[123]['s'].sum)
        self.assertEqual(-15, down[321]['s'].sum)

    def test_downturn_calculations1(self):
        storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]
        storage_dict[321] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        after_trade_storage_dict = StorageDict()
        after_trade_storage_dict[123] = [SpecifiedLeftover('l', 20), SpecifiedLeftover('p', 35)]
        after_trade_storage_dict[321] = [SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 30)]

        product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
                                          ProductHistoryUnit(3, datetime.datetime.utcnow(), storage_dict),
                                          ProductHistoryUnit(5, datetime.datetime.utcnow(), after_trade_storage_dict)])

        down = product_history.get_leftovers_downturn(datetime.datetime.utcnow())
        self.assertEqual(-15, down[123]['s'].sum)
        self.assertEqual(-15, down[321]['s'].sum)
        self.assertEqual(-5, down[123]['l'].sum)
        self.assertEqual(0, down[123]['p'].sum)
        self.assertEqual(0, down[321]['l'].sum)
        self.assertEqual(-5, down[321]['p'].sum)

    def test_dict_wrong_types_insertion(self):
        storage_dict = StorageDict()
        try:
            storage_dict["s"] = 1545
        except (Exception, Exception):
            self.assertTrue(True)
            return
        self.fail()

    def test_product_history_insertion(self):
        storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
                                          ProductHistoryUnit(3, datetime.datetime(2021, 5, 5), storage_dict)])
        product_history.add(ProductHistoryUnit(1000, datetime.datetime(2021, 4, 4), storage_dict))
        self.assertEqual(1000, product_history[1].cost)
        product_history.add(ProductHistoryUnit(2000, datetime.datetime(2021, 6, 6), storage_dict))
        self.assertEqual(2000, product_history[3].cost)


if __name__ == '__main__':
    unittest.main()

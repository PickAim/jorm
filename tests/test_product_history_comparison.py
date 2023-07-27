import datetime
import unittest

from jorm.market.items import ProductHistory, ProductHistoryUnit
from jorm.support.types import StorageDict, SpecifiedLeftover


class ProductHistoryComparisonTest(unittest.TestCase):

    def test_product_history_equals(self):
        storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        saved_time = datetime.datetime.utcnow()

        first_product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
                                                ProductHistoryUnit(3, saved_time, storage_dict)])
        second_product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
                                                 ProductHistoryUnit(3, saved_time, storage_dict)])
        self.assertTrue(first_product_history == second_product_history)

    def test_product_history_non_equals_by_cost(self):
        storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        saved_time = datetime.datetime.utcnow()

        first_product_history = ProductHistory([ProductHistoryUnit(2, datetime.datetime(2021, 1, 1), storage_dict),
                                                ProductHistoryUnit(6, saved_time, storage_dict)])
        second_product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
                                                 ProductHistoryUnit(3, saved_time, storage_dict)])
        self.assertFalse(first_product_history == second_product_history)

    def test_product_history_non_equals_by_date(self):
        storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15), SpecifiedLeftover('l', 25), SpecifiedLeftover('p', 35)]

        saved_time = datetime.datetime.utcnow()

        first_product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2022, 2, 2), storage_dict),
                                                ProductHistoryUnit(3, saved_time, storage_dict)])
        second_product_history = ProductHistory([ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
                                                 ProductHistoryUnit(3, saved_time, storage_dict)])
        self.assertFalse(first_product_history == second_product_history)

    def test_product_history_non_equals_by_leftover_values(self):
        storage_dict = StorageDict()
        another_storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15),
                             SpecifiedLeftover('l', 25),
                             SpecifiedLeftover('p', 35)]
        another_storage_dict[123] = [SpecifiedLeftover('s', 45),
                                     SpecifiedLeftover('l', 255),
                                     SpecifiedLeftover('p', 345)]

        saved_time = datetime.datetime.utcnow()

        first_product_history = ProductHistory([
            ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), another_storage_dict),
            ProductHistoryUnit(3, saved_time, storage_dict)
        ])
        second_product_history = ProductHistory([
            ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
            ProductHistoryUnit(3, saved_time, storage_dict)
        ])
        self.assertFalse(first_product_history == second_product_history)

    def test_product_history_non_equals_by_leftover_keys(self):
        storage_dict = StorageDict()
        another_storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15),
                             SpecifiedLeftover('l', 25),
                             SpecifiedLeftover('p', 35)]
        another_storage_dict[123] = [SpecifiedLeftover('a', 15),
                                     SpecifiedLeftover('b', 25),
                                     SpecifiedLeftover('c', 35)]

        saved_time = datetime.datetime.utcnow()

        first_product_history = ProductHistory([
            ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), another_storage_dict),
            ProductHistoryUnit(3, saved_time, storage_dict)
        ])
        second_product_history = ProductHistory([
            ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
            ProductHistoryUnit(3, saved_time, storage_dict)
        ])
        self.assertFalse(first_product_history == second_product_history)

    def test_product_history_non_equals_by_storages(self):
        storage_dict = StorageDict()
        another_storage_dict = StorageDict()
        storage_dict[123] = [SpecifiedLeftover('s', 15),
                             SpecifiedLeftover('l', 25),
                             SpecifiedLeftover('p', 35)]
        another_storage_dict[321] = [SpecifiedLeftover('s', 15),
                                     SpecifiedLeftover('l', 25),
                                     SpecifiedLeftover('p', 35)]

        saved_time = datetime.datetime.utcnow()

        first_product_history = ProductHistory([
            ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), another_storage_dict),
            ProductHistoryUnit(3, saved_time, storage_dict)
        ])
        second_product_history = ProductHistory([
            ProductHistoryUnit(1, datetime.datetime(2021, 1, 1), storage_dict),
            ProductHistoryUnit(3, saved_time, storage_dict)
        ])
        self.assertFalse(first_product_history == second_product_history)


if __name__ == '__main__':
    unittest.main()

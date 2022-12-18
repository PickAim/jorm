from datetime import date


class ProductHistoryUnit:
    def __init__(self, cost: int, leftover: int, unit_date: date):
        self.__cost: int = cost
        self.__leftover: int = leftover
        self.__unit_date: date = unit_date

    def __str__(self) -> str:
        return str(self.__unit_date) + ": cost - " + str(self.__cost) + "; leftover - " + str(self.__leftover) + ";\n"

    def get_cost(self) -> int:
        return self.__cost

    def get_leftover(self) -> int:
        return self.__leftover

    def get_date(self) -> date:
        return self.__unit_date


class ProductHistory:
    def __init__(self, history: list[ProductHistoryUnit]):
        self.__history: list[ProductHistoryUnit] = history

    def __str__(self) -> str:
        result = ""
        for unit in self.__history:
            result += unit.__str__()
        return result

    def get_costs_pairs(self) -> dict[date, int]:
        return {unit.get_date: unit.get_cost for unit in self.__history}

    def get_leftovers_pairs(self) -> dict[date, int]:
        return {unit.get_date: unit.get_leftover() for unit in self.__history}


class Product:
    def __init__(self, name: str, cost: int, article: int, history: ProductHistory):
        self.__name: str = name
        self.__cost: int = cost
        self.__article = article
        self.__history: ProductHistory = history

    def __str__(self) -> str:
        return self.__name + " (" + str(self.__article) + ")"

    def get_name(self) -> str:
        return self.__name

    def get_cost(self) -> int:
        return self.__cost

    def get_article(self) -> int:
        return self.__article

    def get_history(self) -> ProductHistory:
        return self.__history


class ClientProduct(Product):
    def __init__(self, name: str, niche_name: str, category_name: str, cost: int, article: int, history: ProductHistory):
        super().__init__(name, cost, article, history)
        self.__niche_name: str = niche_name
        self.__category_name: str = category_name

    def get_niche_name(self) -> str:
        return self.__niche_name

    def get_category_name(self) -> str:
        return self.__category_name


class MarketplaceProduct(Product):
    def __init__(self, name: str, cost: int, article, history: ProductHistory):
        super().__init__(name, cost, article, history)

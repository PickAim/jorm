from datetime import date


class Request:
    def __init__(self, request_date: date):
        self.__date: date = request_date

    def __str__(self) -> str:
        return "[" + self.__date.__str__() + "] " + self.__class__.__name__

    def get_date(self) -> date:
        return self.__date


class EconomyRequest(Request):
    def __init__(self, request_date: date, niche_name: str, prime_cost: int,
                 pack_cost: int, transit_cost: int, transit_count: int):
        super().__init__(request_date)
        self.__niche_name: str = niche_name
        self.__prime_cost: int = prime_cost
        self.__pack_cost: int = pack_cost
        self.__transit_cost: int = transit_cost
        self.__transit_count: int = transit_count

    def get_niche_name(self) -> str:
        return self.__niche_name

    def get_prime_cost(self) -> int:
        return self.__prime_cost

    def get_pack_cost(self) -> int:
        return self.__pack_cost

    def get_transit_cost(self) -> int:
        return self.__transit_cost

    def get_transit_count(self) -> int:
        return self.__transit_count


class FrequencyRequest(Request):
    def __init__(self, request_date: date, search_str: str):
        super().__init__(request_date)
        self.__search_str: str = search_str

    def get_search_str(self) -> str:
        return self.__search_str


class Result:
    def __init__(self, request: Request):
        self.request: Request = request


class EconomyResult(Result):
    def __init__(self, request: Request, commission: int, margin: int,
                 transit_price: int, storage_price: int, logistic_price: int):
        super().__init__(request)
        self.__commission: int = commission
        self.__margin: int = margin
        self.__transit_price: int = transit_price
        self.__storage_price: int = storage_price
        self.__logistic_price: int = logistic_price

    def get_commission(self) -> int:
        return self.__commission

    def get_margin(self) -> int:
        return self.__margin

    def get_transit_price(self) -> int:
        return self.__transit_price

    def get_storage_price(self) -> int:
        return self.__storage_price

    def get_logistic_price(self) -> int:
        return self.__logistic_price


class FrequencyResult(Result):
    def __init__(self, request: Request, frequencies: dict[int, int]):
        super().__init__(request)
        self.__frequencies: dict[int, int] = frequencies

    def get_graph_coordinates(self) -> tuple[list[int], list[int]]:
        x = [self.__frequencies[key] for key in self.__frequencies.keys()]
        y = [self.__frequencies[key] for key in self.__frequencies.values()]
        return x, y

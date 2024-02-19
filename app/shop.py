class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]


class TripCalculation:
    def __init__(
            self,
            name: Shop,
            total: float,
            whole_trip_cost: float,
            transactions_list: list[str]
    ) -> None:
        self.name = name
        self.whole_trip_cost = whole_trip_cost
        self.total = total
        self.transactions_list = transactions_list

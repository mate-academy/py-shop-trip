from dataclasses import dataclass


from app.shop import Shop


@dataclass
class Customer:
    def __init__(
            self,
            name: str,
            money: int,
            location: list,
            fuel_consumption: float,
            products_chart: dict
    ) -> None:
        self.name = name
        self.money = money
        self.location = location
        self.fuel_consumption = fuel_consumption
        self.product_cart = products_chart

    def fuel_to_shop(self, shop: Shop) -> float:
        return ((pow(self.location[0] - shop.location[0], 2)
                + pow((self.location[1] - shop.location[1]), 2)) ** 0.5
                * self.fuel_consumption / 100)

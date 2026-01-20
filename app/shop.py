from dataclasses import dataclass
from app.car import Car


@dataclass
class Shop:
    product_shop: dict
    product_cart: dict
    destination_location: list[int, int]

    def get_cheapest_shop(self, car: Car) -> float:
        amount = 0

        for key_cart, value_cart in self.product_cart.items():
            if key_cart in self.product_shop:
                amount += value_cart * self.product_shop[key_cart]

        cost_for_trip = car.get_cost_trip(self.destination_location)
        amount += cost_for_trip

        return round(amount, 2)

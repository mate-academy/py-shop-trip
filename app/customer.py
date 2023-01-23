from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int, int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_costs(self, shop: Shop) -> int | float | None:
        costs = 0
        for product, quantity in self.product_cart.items():
            if product not in shop.products:
                return None
            costs += shop.products[product] * quantity
        return costs

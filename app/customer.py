from app.car import Car
from app.location import Location
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: Location,
        money: float,
        car: Car
    ) -> None:
        self._name = name
        self._product_cart = product_cart
        self.location = location
        self.money = money
        self._car = car

    @property
    def name(self) -> str:
        return self._name

    @property
    def product_cart(self) -> dict:
        return self._product_cart

    @property
    def car(self) -> Car:
        return self._car

    def calculate_shoping_costs(self, shop: Shop) -> int | float:
        total = 0
        for product, amount in self._product_cart.items():
            total += shop.products.get(product) * amount
        return total

from app.car import Car
from app.shop import Shop
from app.utils import distance


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int],
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        dist = distance(self.location, shop.location)

        fuel_cost = (
            dist * 2 * self.car.fuel_consumption / 100 * fuel_price
        )

        products_cost = sum(
            shop.products[p] * q
            for p, q in self.product_cart.items()
        )

        return fuel_cost + products_cost

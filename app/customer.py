from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def get_trip_price(
            self,
            shop: Shop,
            fuel_price:
            int | float
    ) -> int | float:
        distance = (
            (
                (shop.location[0] - self.location[0]) ** 2
                + (shop.location[1] - self.location[1]) ** 2
            ) ** 0.5
        )
        fuel_cost = fuel_price * (
            self.car.fuel_consumption / 100
        ) * distance * 2

        products_price = sum(
            [
                shop.products[product] * amount
                for product, amount in self.product_cart.items()
            ]
        )
        return fuel_cost + products_price

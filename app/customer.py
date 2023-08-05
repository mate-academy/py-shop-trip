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

    def calculate_distance(self, destination_location: list[int]) -> float:
        x1, y1 = self.location
        x2, y2 = destination_location
        return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

    def calculate_product_cost(self, shop_products: dict) -> float | int:
        total_cost = 0
        for product, quantity in self.product_cart.items():
            if product in shop_products:
                total_cost += shop_products[product] * quantity
        return round(total_cost, 2)

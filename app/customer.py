import math


from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, shop: Shop) -> float:
        customer_x = self.location[0]
        customer_y = self.location[1]
        shop_x = shop.location[0]
        shop_y = shop.location[1]
        distance = math.sqrt((shop_x - customer_x) ** 2
                             + (shop_y - customer_y) ** 2)
        fuel = distance / 100 * self.car.fuel_consumption
        return fuel * 2

    def calculate_shopping(self, shop: Shop) -> float:
        total_price = 0
        for product_in_cart, quantity in self.product_cart.items():
            for product_in_shop, price in shop.products.items():
                if product_in_cart == product_in_shop:
                    total_price += quantity * price

        return total_price

    def calculate_total_cost(self, shop: Shop, fuel_price: float) -> float:
        return round(
            self.calculate_distance(shop) * fuel_price
            + self.calculate_shopping(shop),
            2,
        )

    def ride_to_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        shop.shopping(self)
        print(f"{self.name} rides home")

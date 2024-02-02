import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __repr__(self) -> str:
        return self.name

    def calculate_shop_trip(
            self,
            shop: Shop,
            fuel_price: float | int
    ) -> dict[str, int | float | Shop]:
        price_for_fuel = self._calculate_price_for_fuel(shop, fuel_price)
        price_for_products = self._calculate_price_for_products(shop)
        shop_trip_price = price_for_fuel + price_for_products
        print(f"{self.name}'s trip to the {shop.name} costs {shop_trip_price}")
        return {"shop": shop, "shop_trip_price": shop_trip_price}

    def _calculate_price_for_fuel(
            self,
            shop: Shop,
            fuel_price: float | int
    ) -> float:
        distance = math.sqrt(
            math.pow(self.location[0] - shop.location[0], 2)
            + math.pow(self.location[1] - shop.location[1], 2)
        )
        money_for_fuel = (
                (distance * self.car.fuel_consumption / 100) * 2 * fuel_price
        )
        return round(money_for_fuel, 2)

    def _calculate_price_for_products(self, shop: Shop) -> float | int:
        return sum(
            amount * shop.products.get(product)
            for product, amount in self.product_cart.items()
        )

    def ride_to_the_shop(self, shop: Shop, fuel_price: float | int) -> None:
        self.money -= self._calculate_price_for_fuel(shop, fuel_price)
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def ride_to_the_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

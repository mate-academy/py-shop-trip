import math
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
        self.car = car

    def customer_has_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def cost_of_the_trip(
            self,
            fuel_prize: float,
            customer_location: list[int],
            shop_location: list[int]) -> float:
        distance = math.sqrt(
            (shop_location[0] - customer_location[0]) ** 2
            + (shop_location[1] - customer_location[1]) ** 2)
        return round(self.car["fuel_consumption"]
                     * distance / 100 * fuel_prize, 2)

    def does_not_have_enough_money(self) -> None:
        print(f"{self.name} doesn't have enough "
              f"money to make a purchase in any shop")

    def customer_ride_to_shop(self, shop_obj: Shop) -> None:
        print(f"{self.name} rides to {shop_obj.name}")

    def bought_milk(self, product_milk: float) -> None:
        print(
            f'{self.product_cart["milk"]} milks '
            f'for {self.product_cart["milk"] * product_milk} dollars')

    def bought_bread(self, product_bread: float) -> None:
        print(
            f'{self.product_cart["bread"]} bread '
            f'for {self.product_cart["bread"] * product_bread} dollars')

    def bought_butter(self, product_butter: float) -> None:
        print(f'{self.product_cart["butter"]} butter '
              f'for {self.product_cart["butter"] * product_butter} dollars')

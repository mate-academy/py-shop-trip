import math

from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            fuel_consumption: float
    ) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.fuel_consumption = fuel_consumption

    def print_customer_name_and_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_buyer_balance_of_money(self, money: int) -> None:
        self.money = self.money - money
        print(f"{self.name} now has {self.money} dollars\n")

    def get_price_product_cart(self, shop: Shop, file_config: dict) -> int:
        distance = (
            math.sqrt(math.pow((self.location[0] - shop.location[0]), 2)
                      + math.pow((self.location[1] - shop.location[1]), 2))
        )

        price_of_all_products = sum(
            [value * shop.products[key]
                for key, value in self.product_cart.items()
                if key in shop.products]
        )

        price_fuel = (
            (distance / 100 * self.fuel_consumption) * 2
            * file_config["FUEL_PRICE"]
        )

        print(
            f"{self.name}'s trip to the {shop.name} costs "
            f"{round(sum([price_of_all_products, price_fuel]), 2)}"
        )

        return round(sum([price_of_all_products, price_fuel]), 2)

    def change_location_buyer(self, shop: Shop) -> None:
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def print_check(self, shop: Shop) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0.0
        for key, value in self.product_cart.items():
            total_cost += value * shop.products[key]
            print(
                f"{value} {key}s for "
                f"{f'{value * shop.products[key]}'.rstrip('0').rstrip('.')} "
                f"dollars"
            )
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        print(f"{self.name} rides home")

from app.shop import Shop
from math import sqrt
from datetime import datetime


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int],
        money: int | float,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def initial_amount(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def price_of_trip(
            self, fuel_price: int | float, shops: list[Shop]
    ) -> None:
        all_shops_and_prices = dict()
        for shop in shops:
            distance = sqrt(
                (
                    ((shop.location[0] - self.location[0]) ** 2)
                    + ((shop.location[1] - self.location[1]) ** 2)
                )
            )
            price_of_fuel = round(
                ((fuel_price * self.car["fuel_consumption"]
                  * distance / 100) * 2), 2
            )
            price_of_products = 0
            for product in self.product_cart:
                price_of_products += (self.product_cart[product]
                                      * shop.products[product])
            amount = price_of_fuel + price_of_products
            print(f"{self.name}'s trip to the {shop.name} costs {amount}")
            all_shops_and_prices[amount] = [amount, shop, price_of_products]

        the_best_shop = all_shops_and_prices[min(all_shops_and_prices.keys())]
        if self.money - the_best_shop[0] < 0:
            print(
                (
                    f"{self.name} doesn't have "
                    f"enough money to make a purchase in any shop"
                )
            )
        else:
            self.location = the_best_shop[1].location
            print(f"{self.name} rides to {the_best_shop[1].name}" + "\n")
            self.attending_a_shop(the_best_shop)
            self.arriving_home(the_best_shop[0])

    def attending_a_shop(
        self, shop: list[(float, int), Shop, (float, int)]
    ) -> None:
        print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {self.name}, for your purchase!\n"
              "You have bought: ")
        for product in self.product_cart:
            print(
                (
                    f"{self.product_cart[product]} "
                    f"{product}s for "
                    f"{self.product_cart[product] * shop[1].products[product]}"
                    f" dollars"
                )
            )
        print(f"Total cost is {shop[2]} dollars\n"
              "See you again!\n")

    def arriving_home(self, amount: float | int) -> None:
        self.money -= amount
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money} dollars\n")

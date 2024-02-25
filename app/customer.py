from app.car import Car
from app.shop import Shop
from datetime import datetime


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

    def __str__(self) -> str:
        return (f"Name: {self.name}, "
                f"product cart: {self.product_cart}, "
                f"location: {self.location}, "
                f"money: {self.money}, "
                f"car: {self.car}")

    def purchase_amount(self, shops: list[Shop]) -> dict:
        cheapest_store = {}
        for shop in shops:
            cheapest_store[shop] = self.car.price_for_travel(
                self.car.distance(shop.location, self.location)
            )
            for product, price in shop.products_price.items():
                if product in self.product_cart.keys():
                    cheapest_store[shop] += price * self.product_cart[product]

        return cheapest_store

    def customer_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def best_shop(self, purchase_amount: dict) -> dict:
        for shop, amount in purchase_amount.items():
            amount = round(amount, 2)
            print(f"{self.name}'s trip to the {shop.name} costs {amount}")

        for shop, amount in purchase_amount.items():
            if amount == min(value for value in purchase_amount.values()):
                return {shop: round(amount, 2)}

    def trip_to_the_stor(self, shop: dict) -> None:
        home_location = self.location

        for shop_, amount in shop.items():
            if self.money - amount < 0:
                print(
                    f"{self.name} doesn't have enough money "
                    f"to make a purchase in any shop"
                )
                return

            print(f"{self.name} rides to {shop_.name}\n")
            self.location = shop_.location
            date_now = datetime(
                2021, 1, 4, 12, 33, 41
            ).strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {date_now}\nThanks, {self.name}, "
                  f"for your purchase!\n"
                  f"You have bought:")

            total_cost = 0

            for product, number in self.product_cart.items():
                price = number * shop_.products_price[product]
                total_cost += shop_.convert_to_int(price)
                print(f"{number} {product}s for "
                      f"{shop_.convert_to_int(price)} dollars")

            print(f"Total cost is {total_cost} dollars\n"
                  f"See you again!\n")

            balance = self.money - amount
            print(f"{self.name} rides home\n"
                  f"{self.name} now has {balance} dollars\n")
            self.location = home_location

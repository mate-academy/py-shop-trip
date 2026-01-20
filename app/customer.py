import math
import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = Car(data["car"])
        self.all_shops_costs = None
        self.bought_products = None

    def distance_to(self, shop: Shop) -> float:
        return math.sqrt(
            (self.location[0] - shop.location[0])
            ** 2 + (self.location[1] - shop.location[1]) ** 2
        )

    def count_fuel_cost(self, shop: Shop, fuel_price: float) -> float:
        return (((self.distance_to(shop) / 100) * self.car.fuel_consumption)
                * fuel_price)

    def count_shop_costs(self, shop: Shop) -> float:
        return sum(
            product_quantity * price
            for product_quantity, price
            in zip(self.product_cart.values(), shop.products.values())
        )

    def total_shopping_cost(self, shop: Shop, fuel_price: float) -> float:
        return round(
            self.count_fuel_cost(shop, fuel_price) * 2
            + self.count_shop_costs(shop), 2
        )

    def drive_to(self, shop: Shop) -> None:
        self.location = shop.location

    def buy_products(self, shop_products: dict) -> None:
        self.bought_products = {
            product: {"amount": amount, "cost": amount * price}
            for product, amount, price
            in zip(
                self.product_cart.keys(),
                self.product_cart.values(),
                shop_products.values()
            )
        }

    def get_receipt(self) -> None:
        current_time = datetime.datetime.now()
        time_format = "%d/%m/%Y %H:%M:%S"
        print(f"Date: {current_time.strftime(time_format)}\n"
              f"Thanks, {self.name}, for your purchase!\n"
              f"You have bought:")
        for product, amount_and_cost in self.bought_products.items():
            if amount_and_cost["cost"] % 1 != 0:
                shopping_cost = amount_and_cost["cost"]
            else:
                shopping_cost = round(amount_and_cost["cost"])
            print(f"{amount_and_cost['amount']} {product}s "
                  f"for {shopping_cost} dollars")
        print(f"Total cost is {self.count_spent_money()} dollars\n"
              f"See you again!\n")

    def count_spent_money(self) -> float:
        return sum(cost["cost"] for cost in self.bought_products.values())

    def count_remaining_money(self, total_shopping_cost: float) -> None:
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money - total_shopping_cost} "
              f"dollars\n")

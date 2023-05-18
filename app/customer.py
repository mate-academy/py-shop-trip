import datetime

from math import sqrt

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

    def current_balance(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_distance(
            self,
            shop_detail: Shop
    ) -> float:
        distance = sqrt(
            (shop_detail.location[0] - self.location[0]) ** 2
            + (shop_detail.location[1] - self.location[1]) ** 2
        )
        return distance

    def calculate_gasoline(
            self,
            fuel_price: int,
            shop_detail: Shop
    ) -> float:
        gasoline = (
            self.calculate_distance(shop_detail)
            * (self.car["fuel_consumption"] / 100)
            * fuel_price
        )
        return gasoline

    def product_cost(self, shop: Shop) -> float:
        total_expanse = sum(
            price * int(self.product_cart.get(product))
            for product, price in shop.products.items()
        )
        return total_expanse

    def find_min_cost_shop(
            self,
            fuel_price: int,
            shop: list
    ) -> dict:
        min_coast_shop = {}
        for shop_detail in shop:
            total = round(
                self.calculate_gasoline(fuel_price, shop_detail)
                * 2 + self.product_cost(shop_detail), 2
            )
            print(
                f"{self.name}'s trip to the "
                f"{shop_detail.name} costs {total}"
            )
            min_coast_shop[total] = shop_detail.name
        return min_coast_shop

    def purchase_details(self, shop_detail: dict) -> None:
        for product, amount in self.product_cart.items():
            price = (amount * shop_detail[product])
            print(f"{amount} {product}s for {price} dollars")

        print(
            f"Total cost is {self.sum_purchase_details(shop_detail)} dollars\n"
            f"See you again!\n\n"
            f"{self.name} rides home"
        )

    def sum_purchase_details(self, shop_detail: dict) -> float:
        return sum(amount * shop_detail[product]
                   for product, amount in self.product_cart.items())

    def final_result(
            self,
            fuel_price: float,
            shop: list
    ) -> None:
        cheap_shop = self.find_min_cost_shop(fuel_price, shop)
        if min(cheap_shop.keys()) < self.money:
            print(f"{self.name} rides to "
                  f"{cheap_shop.get(min(cheap_shop.keys()))}\n")
            data = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
            print(
                f"Date: {data}\nThanks, {self.name}, "
                f"for your purchase!\nYou have bought: "
            )
            for detail in shop:
                if detail.name == cheap_shop.get(min(cheap_shop.keys())):
                    self.purchase_details(detail.products)
                    fuel = self.calculate_gasoline(fuel_price, detail)
                    sum_purchase = self.sum_purchase_details(detail.products)
                    print(
                        f"{self.name} now has "
                        f"{round(self.money - sum_purchase - fuel * 2, 2)}"
                        f" dollars\n"
                    )
        else:
            print(
                f"{self.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )

from math import sqrt
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            location: list,
            money: int,
            product_cart: dict,
            car: Car
    ) -> None:
        self.name = name
        self.location = tuple(location)
        self.money = money
        self.product_cart = product_cart
        self.car = car

    def find_distance(self, shop_location: list) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location

        distance = sqrt((x2 - x1)**2 + (y2 - y1) ** 2)
        return distance

    def make_purchase(self, shop: Shop) -> None:
        cost = 0
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")
        for item, quantity in self.product_cart.items():
            if item in shop.products:
                item_price = shop.products[item]
                item_total_price = item_price * quantity
                cost += item_total_price
                print(f"{quantity} {item}s for {item_total_price} dollars")
        print(f"Total cost is {cost} dollars")
        print("See you again!")

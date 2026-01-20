from __future__ import annotations

from app.shops import Shop


def format_money(money: int | float, char: int) -> int | float:
    return int(money) if money == int(money) else round(money, char)


class Customer:
    FUEL_PRICE = 2.4

    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]

    def spent_on_fuel(self, shop: Shop) -> float:
        distance = (
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        ) ** 0.5

        fuel_on_distance = self.car["fuel_consumption"] * distance / 100
        return fuel_on_distance * self.FUEL_PRICE

    def total_spent(self, shop: Shop) -> float:
        spent_on_road = self.spent_on_fuel(shop) * 2
        spent_in_shop = shop.total_price(self)
        return spent_on_road + spent_in_shop

    def choose_shop(self, shops: list) -> Shop | None:
        cheapest_price = 999999
        cheapest_shop = None
        print(f"{self.name} has {format_money(self.money, 2)} dollars")
        for shop in shops:
            print(f"{self.name}'s trip to the {shop.name}"
                  f" costs {format_money(self.total_spent(shop), 2)}")
            if self.total_spent(shop) < cheapest_price:
                cheapest_price = self.total_spent(shop)
                cheapest_shop = shop
        if self.money >= cheapest_price:
            self.location = cheapest_shop.location
            self.money -= cheapest_price
            print(f"{self.name} rides to {cheapest_shop.name}\n")
            return cheapest_shop
        print(f"{self.name} doesn't have enough "
              f"money to make a purchase in any shop")
        return None

    def back_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has "
              f"{format_money(self.money, 2)} dollars\n")

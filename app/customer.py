from decimal import Decimal
from typing import List

from app.car import Car, Location
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = Location(location)
        self.home_location = Location(location)
        self.money = Decimal(str(money))
        self.car = Car(car["brand"], car["fuel_consumption"])

    def arrive_at_shop(self, shop: Shop) -> str:
        self.location = shop.location
        return f"{self.name} rides to {shop.name}\n"

    def arrive_home(self) -> str:
        self.location = self.home_location
        return f"{self.name} rides home"

    def do_shopping(self, shops: List[Shop]) -> None:
        """
        I think all this prints and function calls would rather
        be put in Customer class as a method because all of this actions
        can be done within Customer instance -
        you can call it do_shopping or something.
        Having so many prints inside your main()
        makes it look messy - it's better to organize this logic
        """
        purchase_flag = False
        print(f"{self.name} has {self.money} dollars")
        min_cost = Decimal("infinity")
        shop_index = 0
        for index, shop in enumerate(shops):
            all_cost = (
                self.location.calculate_cost_distance(
                    shop.location,
                    self.car
                )
                + shop.calculate_purchase(self)
            )
            print(
                f"{self.name}'s trip to the "
                f"{shop.name} costs {all_cost}"
            )
            if all_cost < min_cost:
                min_cost = all_cost
                shop_index = index
        if min_cost <= self.money:
            purchase_flag = True
        if purchase_flag:
            print(self.arrive_at_shop(shops[shop_index]))
            print(shops[shop_index].fulfilled_purchase(self))
            print(self.arrive_home())
            print(f"{self.name} now "
                  f"has {self.money - min_cost} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money to make"
                  f" a purchase in any shop")

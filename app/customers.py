from typing import Any
from app.cars import Car
from app.shops import Shop


class Customer:

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def do_shop_trip(self, shops: list) -> Any:
        print(f"{self.name} has {self.money} dollars")
        shops_price = {shop: self.calculate_costs(shop) for shop in shops}
        cheaper_shop = min(shops_price, key=shops_price.get)

        if shops_price[cheaper_shop] <= self.money:
            print(f"{self.name} rides to {cheaper_shop}\n")
            self.money -= shops_price[cheaper_shop]
            return (cheaper_shop.print_bill(self.name, self.product_cart),
                    self.ride_home())

        else:
            print(f"{self.name} doesn't have enough money"
                  f" to make a purchase in any shop")

    def calculate_costs(self, shop: Shop) -> float:
        fuel = self.car.fuel_costs(self.location, shop.location)
        products = sum(shop.products[key] * self.product_cart[key]
                       for key in self.product_cart)
        costs = round(fuel + products, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {costs}")
        return costs

    def ride_home(self) -> None:
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money} dollars\n")

from app.car import Car
from app.shop import Shop

import datetime


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: Car,
                 ) -> None:
        self.name = name
        self.production_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.is_ride_to_shop = True

    def summary_cost(self, shop: Shop) -> float:
        transit_cost = self.car.transit_cost(customer_location=self.location,
                                             shop_location=shop.location)

        cart_cost = shop.cart_cost(self.production_cart)
        return round(transit_cost + cart_cost["cart_cost"], 2)

    def shop_choice(self, shop: Shop) -> None:
        if self.money > self.summary_cost(shop):
            print(f"{self.name} rides to {shop.name}")
        else:
            self.is_ride_to_shop = False
            print(f"{self.name} doesn't have enough money to make "
                  f"a purchase in any shop")

    def print_customer_money_information(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def print_trips(self, shop: Shop) -> None:
        print(f"{self.name}'s trip to the {shop.name} costs"
              f" {self.summary_cost(shop)}")

    def print_shop_information(self, shop: Shop) -> None:
        shop_cart_cost = shop.cart_cost(self.production_cart)
        formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {formatted_date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for product, price in list(shop_cart_cost.items())[:-1]:
            print(f"{self.production_cart[product]} {product}s "
                  f"for {price:g} dollars")

        print(f"Total cost is {shop_cart_cost['cart_cost']} dollars")
        print("See you again!")
        print(f"\n{self.name} rides home")
        print(f"{self.name} now has "
              f"{self.money - self.summary_cost(shop)} dollars\n")

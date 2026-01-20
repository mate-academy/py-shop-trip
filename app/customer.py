import datetime
import dataclasses
from math import sqrt


from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: int | float

    def distance_price(
            self, fuel_price: int | float,
            shop: Shop
    ) -> int | float:
        distance = sqrt(
            ((shop.location[0] - self.location[0]) ** 2)
            + ((shop.location[1] - self.location[1]) ** 2)
        )

        price = (self.car / 100) * distance * fuel_price
        return round(price * 2, 2)

    def product_price(self, shop: Shop) -> int | float:
        return sum(
            [self.product_cart[key] * shop.products[key]
             for key in shop.products.keys()]
        )

    def cheapest_trip(self, shops: list[Shop], fuel_price: int | str) -> None:

        cheapest_shop = [
            shops[0], round((self.product_price(shops[0])
                             + self.distance_price(fuel_price, shops[0])), 2)
        ]

        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            final_price = round(
                (self.product_price(shop)
                 + (self.distance_price(fuel_price, shop))), 2
            )

            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {final_price}")

            if cheapest_shop[1] > final_price:
                cheapest_shop[0], cheapest_shop[1] = shop, final_price
            else:
                continue

        if cheapest_shop[1] < self.money:
            self.location = cheapest_shop[0].location
            print(f"{self.name} rides to {cheapest_shop[0].name}\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
              f"\nThanks, {self.name}, for your purchase!"
              f"\nYou have bought: ")

        total_cost = 0

        for product in cheapest_shop[0].products:
            product_cost = round(
                self.product_cart[product]
                * cheapest_shop[0].products[product], 2
            )
            print(f"{self.product_cart[product]}"
                  f" {product}s for {product_cost} dollars")
            total_cost += product_cost

        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!\n\n{self.name} rides home\n"
              f"{self.name} now has {self.money - cheapest_shop[1]} dollars\n")

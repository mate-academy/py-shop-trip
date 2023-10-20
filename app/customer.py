from dataclasses import dataclass
from datetime import datetime

from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: dict

    def distance_cost(self, shop: Shop, price_per_liter: float | int) -> float:
        distance = ((shop.location[0] - self.location[0]) ** 2
                    + (shop.location[1] - self.location[1]) ** 2) ** 0.5
        fuel_consumption = self.car["fuel_consumption"]
        cost_road = distance * fuel_consumption / 100 * price_per_liter
        return cost_road * 2

    def product_cost(self, shop: Shop) -> float | int:
        return sum(
            [self.product_cart[product] * shop.products[product]
             for product in shop.products.keys()]
        )

    def trip_cost(
            self,
            shops_list: list[Shop],
            price_per_liter: float | int
    ) -> None:
        home_location = self.location
        cheapest_trip = [
            shops_list[0],
            round((self.product_cost(shops_list[0])
                   + self.distance_cost(shops_list[0], price_per_liter)), 2)
        ]
        print(f"{self.name} has {self.money} dollars")

        for shop in shops_list:
            price_trip = round(
                self.product_cost(shop)
                + self.distance_cost(shop, price_per_liter), 2
            )
            print(f"{self.name}'s trip to the {shop.name} costs {price_trip}")

            if cheapest_trip[1] > price_trip:
                cheapest_trip[0], cheapest_trip[1] = shop, price_trip

        if cheapest_trip[1] > self.money:
            print(f"{self.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            return

        print(f"{self.name} rides to {cheapest_trip[0].name}\n")
        self.location = cheapest_trip[0].location

        date = datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}\n"
              f"Thanks, {self.name}, for your purchase!\n"
              f"You have bought: ")

        purchase = 0
        for prod in cheapest_trip[0].products:
            price = cheapest_trip[0].products[prod] * self.product_cart[prod]
            print(f"{self.product_cart[prod]} {prod}s for {price} dollars")
            purchase += price

        print(f"Total cost is {purchase} dollars\n"
              f"See you again!\n\n"
              f"{self.name} rides home\n"
              f"{self.name} now has {self.money - cheapest_trip[1]} dollars\n")
        self.location = home_location

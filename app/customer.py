import math
import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            products: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

    def define_shop(self, shops: list[Shop], fuel_price: float) -> Shop | None:
        print(f"{self.name} has {self.money} dollars")

        cheapest_trip_cost = 0
        chosen_shop: Shop | None = None

        for shop in shops:
            fuel_cost = (math.dist(self.location, shop.location)
                         * self.car.fuel_consumption / 100 * fuel_price)
            products_cost = sum(
                product_value * shop.products.get(product)
                for product, product_value in self.products.items()
            )
            trip_cost = round(fuel_cost * 2 + products_cost, 2)
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")

            if not cheapest_trip_cost or trip_cost < cheapest_trip_cost:
                cheapest_trip_cost = trip_cost
                chosen_shop = shop

        if cheapest_trip_cost > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return

        self.money -= cheapest_trip_cost
        print(f"{self.name} rides to {chosen_shop.name}\n")
        return chosen_shop

    def make_purchase(self, chosen_shop: Shop) -> None:
        formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}\n"
              f"Thanks, {self.name}, for your purchase!\nYou have bought:")
        total_cost = 0

        for product, quantity in self.products.items():
            cost = chosen_shop.products.get(product) * quantity
            cost = int(cost) if int(cost) == cost else cost
            total_cost += cost
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")

    def ride_home(self) -> None:
        print(f"{self.name} rides home\n{self.name}"
              f" now has {round(self.money, 2)} dollars\n")

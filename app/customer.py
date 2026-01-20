import datetime
import math

from dataclasses import dataclass

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: Car

    def print_financial_status(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def print_date_time_intro_on_receipt(self) -> None:
        date = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")

    def print_purchase_details(self, shop_prices: dict) -> None:
        for product_name, product_count in self.product_cart.items():
            cost = product_count * shop_prices[product_name]
            print(f"{product_count} {product_name}s for {cost} dollars")

    def total_car_trip_cost(self, shop: Shop, fuel_cost: float) -> float:
        trip_to = math.dist(self.location, shop.location)
        cost_per_100_km = self.car.fuel_consumption * fuel_cost
        return 2 * cost_per_100_km * (trip_to / 100)

    def total_cost_by_shop(self, shop: Shop) -> float:
        total_cost = []
        for product_name, price in shop.products.items():
            total_cost.append(price * int(self.product_cart.get(product_name)))
        return sum(total_cost)

    def pick_the_cheapest(self, shops: list[Shop], fuel_cost: int) -> None:
        short_shops_base = {}
        for shop in shops:
            total_cost = (
                round(
                    self.total_car_trip_cost(shop, fuel_cost)
                    + self.total_cost_by_shop(shop), 2)
            )
            short_shops_base[shop.name] = total_cost
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")

        if (
                len(short_shops_base)
                and min(short_shops_base.values()) < self.money
        ):
            cheapest_shop = min(short_shops_base, key=short_shops_base.get)
            print(f"{self.name} rides to {cheapest_shop}\n")
            self.print_date_time_intro_on_receipt()

            the_cheapest_shop = (
                [shop for shop in shops
                 if shop.name == cheapest_shop][0]
            )
            self.print_purchase_details(the_cheapest_shop.products)
            print(f"Total cost is "
                  f"{self.total_cost_by_shop(the_cheapest_shop)} dollars")
            print(f"See you again!\n\n{self.name} rides home")
            self.money -= min(short_shops_base.values())
            print(f"{self.name} now has {self.money} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

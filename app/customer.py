import math
import datetime
import dataclasses
from app.car import Car
from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: Car

    def money_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def road_cost(self, shop_location: Shop, fuel_cost: float) -> float:
        distance = math.dist(self.location, shop_location.location)
        return distance * (self.car.fuel_consumption / 100) * fuel_cost

    def shop_cost(self, shopping_price: dict) -> None:
        for product, amount in self.product_cart.items():
            price = amount * shopping_price[product]
            print(f"{amount} {product} for {price} dollars")

    def product_cost(self, shop: Shop) -> float:
        total = 0
        for product, amount in shop.products.items():
            total += amount * float(self.product_cart.get(product))
        return total

    def cost_of_the_trip(self, shops: list[Shop], fuel_cost: float) -> None:
        cheapest_shop = None
        min_total_cost = float("inf")
        for shop in shops:
            spent_for_shopping = round(self.road_cost(shop, fuel_cost) * 2
                                       + self.product_cost(shop), 2)

            total_trip_cost = spent_for_shopping

            if total_trip_cost <= self.money and \
                    total_trip_cost <= min_total_cost:
                min_total_cost = total_trip_cost
                print(min_total_cost)
                cheapest_shop = shop
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {total_trip_cost:.2f}")

        if cheapest_shop:
            print(f"{self.name} rides to {cheapest_shop.name}")
            self.location = cheapest_shop.location
            current_time = (datetime.datetime(2021, 4, 1, 12, 33, 41)
                            .strftime("%m/%d/%Y %H:%M:%S"))
            print(f"\nDate: {current_time}")
            print(f"Thanks, {self.name}, for your purchase!")
            print("You have bought:")
            self.shop_cost(cheapest_shop.products)
            print(f"Total cost is "
                  f"{self.product_cost(cheapest_shop):.1f} dollars")
            print("See you again!")
            print(f"\n{self.name} rides home")
            self.money -= min_total_cost
            print(f"{self.name} now has {self.money:.2f} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

import dataclasses
import datetime
import math

from app.car import Car
from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: Car

    def start_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def cost_to_get_to_the_shop(
            self,
            shop_location: Shop,
            fuel_cost: float
    ) -> float:
        distance_to_shop = math.dist(self.location, shop_location.location)
        return distance_to_shop * (self.car.fuel_consumption / 100) * fuel_cost

    def shop_cost(self, products_price: dict) -> None:
        for product, amount in self.product_cart.items():
            price = amount * products_price[product]
            price = (
                int(price) if isinstance(price, float) and price.is_integer()
                else price
            )
            print(f"{amount} {product}s for {price} dollars")

    def products_cost(self, shop: Shop) -> float:
        total = 0
        for product, amount in shop.products.items():
            total += amount * self.product_cart.get(product)
        return total

    def cost_of_the_trip(self, shops: list[Shop], fuel_cost: float) -> None:
        cheapest_shop = None
        min_total_cost = float("inf")
        for shop in shops:
            spent_for_shopping = round(
                self.cost_to_get_to_the_shop(shop, fuel_cost) * 2
                + self.products_cost(shop), 2
            )

            if (spent_for_shopping <= self.money
                    and spent_for_shopping <= min_total_cost):
                min_total_cost = spent_for_shopping
                cheapest_shop = shop
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {spent_for_shopping}")

        if cheapest_shop:
            print(f"{self.name} rides to {cheapest_shop.name}\n")
            self.location = cheapest_shop.location
            data = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
            print(f"Date: {data}\nThanks, {self.name}, "
                  f"for your purchase!\nYou have bought: ")

            self.shop_cost(cheapest_shop.products)
            print(f"Total cost is "
                  f"{self.products_cost(cheapest_shop)} dollars")
            print("See you again!")
            print(f"\n{self.name} rides home")
            self.money -= min_total_cost
            print(f"{self.name} now has {self.money} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

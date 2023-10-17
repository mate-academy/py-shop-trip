import math
import datetime
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int,
        car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def cost_trip(self, shop: Shop, fuel_price: float) -> float:
        return math.sqrt(
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        ) * 2 * fuel_price * self.car["fuel_consumption"] / 100

    def cost_products(self, shop: Shop) -> float:
        total = 0
        for product, quantity in self.product_cart.items():
            total += shop.products[product] * quantity
        return total

    def total_trip_price(self, shops: list, fuel_price: float) -> dict:
        return {
            round(
                self.cost_trip(shop, fuel_price)
                + self.cost_products(shop), 2
            ): shop
            for shop in shops
        }

    def print_text(self, shops: list, fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        shops_price = self.total_trip_price(shops, fuel_price)
        for cost, shop in shops_price.items():
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")
        chip_shop = dict(sorted(shops_price.items()))
        chip_shop = next(iter(chip_shop.items()))
        if chip_shop[0] > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return
        print(f"{self.name} rides to {chip_shop[1].name}\n")
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")
        for name, count in self.product_cart.items():
            cost = count * chip_shop[1].products[name]
            if (cost * 10) % 10 == 0:
                cost = int(cost)
            print(f"{count} {name}s for "
                  f"{cost} "
                  f"dollars")
        print(f"Total cost is {self.cost_products(chip_shop[1])} dollars")
        print("See you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - chip_shop[0]} dollars\n")

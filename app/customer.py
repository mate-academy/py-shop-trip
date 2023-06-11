import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, customer_info: dict) -> None:
        self.name = customer_info["name"]
        self.product_cart = customer_info["product_cart"]
        self.money = customer_info["money"]
        self.car = Car(
            customer_info["car"]["brand"],
            customer_info["car"]["fuel_consumption"],
            customer_info["location"],
        )

    def cost_of_shopping(self, shop: Shop) -> float:
        total_cost = self.car.trip_cost(shop.location) * 2
        for product, quantity in self.product_cart.items():
            total_cost += quantity * shop.products[product]
        return total_cost

    def choose_shop(self, shops: list[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")

        min_shopping = None
        best_shop = None
        for shop in shops:
            shop_cost = round(self.cost_of_shopping(shop), 2)
            if min_shopping is None or shop_cost < min_shopping:
                min_shopping = shop_cost
                best_shop = shop
            print(f"{self.name}'s trip to the {shop.name} costs {shop_cost}")
        if self.money >= min_shopping:
            products_cost = round(
                min_shopping - (self.car.trip_cost(best_shop.location) * 2), 2
            )
            print(f"{self.name} rides to {best_shop.name}\n")
            self.money -= min_shopping
            date = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
            print(
                f"Date: {date}\n"
                f"Thanks, {self.name}, for your purchase!\n"
                f"You have bought: "
            )
            for product, quantity in self.product_cart.items():
                print(
                    f"{quantity} {product}s for "
                    f"{quantity * best_shop.products[product]} dollars"
                )
            print(f"Total cost is {products_cost} dollars\n See you again!\n")
            print(
                f"{self.name} rides home\n"
                f"{self.name} now has {self.money} dollars\n"
            )
        else:
            print(
                f"{self.name} "
                f"doesn't have enough money to make a purchase in any shop"
            )

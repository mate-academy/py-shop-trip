import math

from app.shop import Shop


class Customer:
    def __init__(self, dct: dict, fuel_price: float) -> None:
        self.name = dct["name"]
        self.product_cart: dict = dct["product_cart"]
        self.location: list = dct["location"]
        self.money = dct["money"]
        print(f"{self.name} has {self.money} dollars")
        self.car: dict = dct["car"]
        self.fuel_price = fuel_price

    def get_the_cheapest_one(self, shops: list[Shop]) -> Shop | None:
        nearest_shop = None
        min_cost = float("inf")
        for shop in shops:
            distance = math.sqrt(
                (shop.location[0] - self.location[0]) ** 2
                + (shop.location[1] - self.location[1]) ** 2
            )
            purchases = shop.purchases(self.product_cart)
            fuel_cost = (distance * self.car["fuel_consumption"]
                         / 100 * self.fuel_price)
            trip_cost = fuel_cost * 2 + purchases
            cost = round(trip_cost, 2)

            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {cost}"
            )

            if cost < min_cost:
                min_cost = cost
                nearest_shop = shop

        if self.money >= min_cost:
            if nearest_shop:
                print(
                    f"{self.name} rides to {nearest_shop.name}"
                )
                nearest_shop.checkout(self.name, self.product_cart)

            self.money -= min_cost
            self.money = round(self.money, 2)
            print(f"{self.name} rides home")
            print(f"{self.name} now has {self.money} dollars")
        else:
            print(
                f"{self.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )

        return nearest_shop

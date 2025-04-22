from dataclasses import dataclass
from math import inf, sqrt

from app.shop import Shop


@dataclass
class Customer:

    name: str
    product_cart: dict
    location: list
    money: float
    car: dict

    @classmethod
    def config_from_dict(cls, config: dict) -> "Customer":
        return cls(
            config["name"],
            config["product_cart"],
            config["location"],
            config["money"],
            config["car"]
        )

    def shop_travel_cost(self, shop: Shop, fuel_cost: float) -> float:
        distance = sqrt((shop.location[0] - self.location[0]) ** 2
                        + (shop.location[1] - self.location[1]) ** 2)
        return round((distance * 2 * fuel_cost
                      * self.car["fuel_consumption"] / 100), 2)

    def visit_shop(self, shop: Shop, fuel_cost: float) -> None:

        home_location = self.location
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location
        print("")
        shop.take_client(self)
        print("")
        print(f"{self.name} rides home")
        self.location = home_location
        self.money -= self.shop_travel_cost(shop, fuel_cost)
        print(f"{self.name} now has {self.money} dollars\n")

    def check_shops(
            self,
            fuel_cost: float,
            shops: list[Shop]
    ) -> None:

        print(f"{self.name} has {self.money} dollars")

        cheapest_price = inf
        cheapest_shop = None
        for shop in shops:
            trip_cost = (self.shop_travel_cost(shop, fuel_cost)
                         + shop.shopping_cost(self.product_cart))
            if trip_cost < cheapest_price:
                cheapest_price = trip_cost
                cheapest_shop = shop

            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")

        if cheapest_price <= self.money:
            self.visit_shop(cheapest_shop, fuel_cost)
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

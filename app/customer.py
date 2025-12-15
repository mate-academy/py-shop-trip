from app.car import Car
from app.utils import clean_round


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def store_selection(self, shops: list) -> None:
        print(f"{self.name} has {self.money} dollars")
        cheapest_trip = {
            "shop": None,
            "product_cost": 0,
            "total_cost": float("inf")
        }

        for shop in shops:
            product_cost = sum(
                shop.product_cart_cost(self.product_cart).values()
            )
            distance_to_shop = (
                (self.location[0] - shop.location[0]) ** 2
                + (self.location[1] - shop.location[1]) ** 2
            ) ** 0.5
            fuel_cost = self.car.fuel_consumption_cost(distance_to_shop * 2)
            total_cost = product_cost + fuel_cost
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")

            if total_cost < cheapest_trip["total_cost"]:
                cheapest_trip["shop"] = shop
                cheapest_trip["product_cost"] = product_cost
                cheapest_trip["total_cost"] = total_cost

        if self.money >= cheapest_trip["total_cost"] and cheapest_trip["shop"]:
            print(f"{self.name} rides to {cheapest_trip['shop'].name}\n")
            home_location = self.location
            self.location = cheapest_trip["shop"].location
            cheapest_trip["shop"].purchase(self)
            self.money -= cheapest_trip["total_cost"]
            self.location = home_location
            print(
                f"{self.name} rides home\n"
                f"{self.name} now has {clean_round(self.money)} dollars\n"
            )
        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

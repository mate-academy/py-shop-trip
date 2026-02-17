import math
from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def get_distance(self, shop_location: list) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def choose_shop(self, shops: list, fuel_price: float) -> None:
        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            distance = self.get_distance(shop_location=shop.location)
            fuel_needed = self.car.get_fuel_needed(distance)

            cost_road = (fuel_needed * fuel_price) * 2
            cost_prod = shop.calculate_cost(self.product_cart)

            total_trip_cost = cost_road + cost_prod

            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {total_trip_cost:.2f}")

            if total_trip_cost < min_trip_cost:
                min_trip_cost = total_trip_cost
                cheapest_shop = shop

        if cheapest_shop is None or self.money < min_trip_cost:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            print(f"{self.name} rides to {cheapest_shop.name}")

            self.location = cheapest_shop.location

            cheapest_shop.print_receipt(self.name, self.product_cart)

            print(f"{self.name} rides home")

            self.money -= min_trip_cost
            print(f"{self.name} now has {self.money:.2f} dollars")
            print()

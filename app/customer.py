from app.car import Car
from app.shop import Shop
from math import sqrt


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: Car,
            fuel_price: float
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.fuel_price = fuel_price

    def calculate_cost_trip(self, shop: Shop) -> float:
        distance = sqrt(
            (shop.location[0] - self.location[0])**2
            + (shop.location[1] - self.location[1])**2
        )
        return round(
            self.car.calculate_cost_trip(distance, self.fuel_price) * 2, 2
        )

    def choose_shop(self, shops: list) -> None:
        if not shops:
            print("No shops to choose.")
            return

        print(f"{self.name} has {round(self.money, 2)} dollars")

        shop_trip_costs = []
        for shop in shops:
            trip_cost = self.calculate_cost_trip(shop)
            cart_cost = shop.calculate_cost_product_cart(self.product_cart)
            total_cost = round(trip_cost + cart_cost, 2)
            shop_trip_costs.append((shop, total_cost, trip_cost))
            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {round(total_cost, 2)}"
            )

        best_shop, lowest_total, _ = shop_trip_costs[0]
        for shop, total_cost, _ in shop_trip_costs[1:]:
            if total_cost < lowest_total:
                best_shop, lowest_total = shop, total_cost

        if self.money < lowest_total:
            print(
                f"{self.name} doesn't have enough money to make "
                f"a purchase in any shop"
            )
            return

        home_location = self.location.copy()
        self.location = best_shop.location

        print(f"{self.name} rides to {best_shop.name}\n")
        best_shop.print_receipt(self.name, self.product_cart)

        self.money -= lowest_total
        self.location = home_location

        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

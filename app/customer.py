from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, customer_data: dict) -> None:
        self.name = customer_data["name"]
        self.product_cart = customer_data["product_cart"]
        self.location = customer_data["location"]
        self.money = customer_data["money"]
        self.car = Car(customer_data["car"])

    def find_travel_cost(self, location: list, fuel_price: float) -> float:
        distance = (
            2 * (
                (self.location[0] - location[0]) ** 2
                + (self.location[1] - location[1]) ** 2
            ) ** 0.5
        )
        return distance * fuel_price * self.car.fuel_consumption / 100

    def shop_selection(self, shops_dict: dict, fuel_price: float) -> tuple:
        print(f"{self.name} has {self.money} dollars")
        trip_costs = []
        for shop in shops_dict.values():
            travel_cost = (
                self.find_travel_cost(shop.location, fuel_price)
            )
            shopping_cost = shop.find_shopping_cost(self.product_cart)
            total_cost = round(travel_cost + shopping_cost, 2)
            print(
                f"{self.name}'s trip "
                f"to the {shop.name} costs {total_cost}"
            )
            trip_costs.append((total_cost, shop))
        trip_costs.sort()
        return trip_costs[0]

    def not_enough_money(self) -> None:
        print(
            f"{self.name} doesn't have enough money "
            f"to make a purchase in any shop"
        )

    def shopping_trip(self, cheapest_shop: Shop, lowest_price: float) -> None:
        print(f"{self.name} rides to {cheapest_shop.name}\n")
        self.location = cheapest_shop.location
        cheapest_shop.print_receipt(self.name, self.product_cart)
        print(f"{self.name} rides home")
        self.money = self.money - lowest_price
        print(f"{self.name} now has {self.money} dollars")

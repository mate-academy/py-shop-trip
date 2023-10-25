from car import Car
from calculate_distance import calculate_distance


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

    def calculate_trip_cost(
            self,
            shop_location: list,
            fuel_price: float
    ) -> float:
        distance = calculate_distance(self.location, shop_location)
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price)
        return fuel_cost

    def update_location(self, new_location: list) -> None:
        self.location = new_location

    def make_purchase(
            self,
            shop_name: str,
            shop_products: dict,
            shop_prices: dict
    ) -> None:
        for item, quantity in self.product_cart.items():
            if item in shop_products:
                cost = quantity * shop_prices[item]
                self.money -= cost
                self.product_cart[item] -= quantity

    def update_money(self, trip_cost: float, purchase_cost: float) -> None:
        self.money -= trip_cost - purchase_cost

    def get_remaining_money(self) -> float:
        return self.money

    def get_current_location(self) -> list:
        return self.location

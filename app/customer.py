from .car import Car


class Customer:
    def __init__(self, name: str,
                 location: list,
                 money: int,
                 car: "Car",
                 home_location: list,
                 product_cart: dict) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.car = car
        self.home_location = home_location
        self.product_cart = product_cart

    def go_to_shop(self, shop: float, fuel_price: float) -> float:
        distance = ((shop.location[0] - self.location[0])**2
                    + (shop.location[1] - self.location[1])**2) ** 0.5
        cost = self.car.calculate_fuel_cost(distance, fuel_price)
        self.location = shop.location
        return cost

    def go_home(self, shop: float, fuel_price: float) -> float:
        distance = ((shop.location[0] - self.home_location[0])
                    ** 2 + (shop.location[1] - self.home_location[1])
                    ** 2) ** 0.5
        cost = self.car.calculate_fuel_cost(distance, fuel_price)
        self.location = self.home_location
        return cost

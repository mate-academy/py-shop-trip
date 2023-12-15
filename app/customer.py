from app.car import Car


class Customer:

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list[int],
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def find_distance(self, current_location: list[int]) -> float:
        x1, y1 = self.location
        x2, y2 = current_location
        distance = ((x2 - x1)**2 + (y2 - y1) ** 2) ** 0.5
        return distance

    def rides_home(self, total_cost: float, current_location: list) -> list:
        print(f"{self.name} rides home")
        current_location = self.location
        print(f"{self.name} now has {self.money - total_cost} dollars\n")
        return current_location

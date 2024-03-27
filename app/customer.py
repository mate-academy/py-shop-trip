from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int, int],
            money: int,
            car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def show_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def show_cost_to_shop(
            self,
            shop: Shop,
            fuel_price: float | int) -> int | float:
        get_car = Car(
            self.car["brand"],
            self.location,
            self.car["fuel_consumption"],
            fuel_price)
        return get_car.get_cost_trip(shop["location"])

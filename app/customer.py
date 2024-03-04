from app.car import Car
from app.data_loading import configs


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        self.best_shop = None
        self.fuel_price = configs["FUEL_PRICE"]
        self.car = car


customers = []

for customer in configs["customers"]:
    customer = Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(**customer["car"])
    )
    customers.append(customer)

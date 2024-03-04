from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            fuel_price: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        self.best_shop = None
        self.fuel_price = fuel_price
        self.car = car


def create_customers(configs: dict) -> list[Customer]:
    customers = []
    fuel_price = configs["FUEL_PRICE"]
    for customer in configs["customers"]:
        customer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            fuel_price,
            Car(**customer["car"])
        )
        customers.append(customer)

    return customers

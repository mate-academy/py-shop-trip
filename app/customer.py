from app.car import Car


class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer.get("name")
        self.product_cart = customer.get("product_cart")
        self.location = customer.get("location")
        self.money = customer.get("money")
        self.car = Car(customer)

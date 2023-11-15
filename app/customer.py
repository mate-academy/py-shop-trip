from app.car import Car


class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer.get("name")
        self.product_cart = customer.get("product_cart")
        self.location = customer.get("location")
        self.money = customer.get("money")
        self.car = Car(customer)

    def __str__(self) -> str:
        return (f"Customer name: {self.name}\n"
                f"Customer money: {self.money}\n"
                f"Customer location: {self.location}\n"
                f"Customer car: {self.car}\n"
                f"Customer product cart: {self.product_cart}")

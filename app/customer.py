class Customer:
    def __init__(self, customer: dict) -> None:
        self.customer = customer
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]

    def can_afford(self, some_money: float | int) -> bool:
        return self.money >= some_money

    def get_location(self) -> list:
        return self.location

    def get_product_cart(self) -> dict:
        return self.product_cart

    def set_location(self, new_location: list) -> None:
        self.location = new_location

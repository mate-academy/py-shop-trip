class Customer:
    def __init__(self, customers: dict) -> None:
        self.name = customers["name"]
        self.product_cart = customers["product_cart"]
        self.location = customers["location"]
        self.money = customers["money"]
        self.car = customers["car"]

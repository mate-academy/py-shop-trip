class Customer:
    def __init__(self, customers: dict):
        self.name = customers["name"]
        self.location = customers["location"]
        self.products = customers["product_cart"]
        self.money = customers["money"]
        self.car = customers["car"]["fuel_consumption"]

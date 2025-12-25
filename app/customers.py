class Customer:
    def __init__(self, customers: dict):
        self.name = customers["name"]
        self.product_cart = customers["product_cart"]
        self.location = customers["location"]
        self.money = customers["money"]
        self.car = customers["car"]

    def show_money(self) -> None:
        print(f"{self.money}")

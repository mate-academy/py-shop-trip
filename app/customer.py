class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.milk = self.product_cart["milk"]
        self.bread = self.product_cart["bread"]
        self.butter = self.product_cart["butter"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car_consumption = customer["car"]["fuel_consumption"]

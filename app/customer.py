class Customer:

    def __init__(self, customer: dict):
        self.customer = customer
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]

    def can_afford(self, some_money):
        return some_money <= self.money


    def get_location(self):
        return self.location

    def get_product_cart(self):
        return self.product_cart
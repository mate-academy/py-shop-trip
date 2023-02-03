

class Customers:
    def __init__(self, customer_dict: dict) -> None:
        self.name = customer_dict["name"]
        self.prod_cart = customer_dict["product_cart"]
        self.location = customer_dict["location"]
        self.money = customer_dict["money"]
        self.car = customer_dict["car"]

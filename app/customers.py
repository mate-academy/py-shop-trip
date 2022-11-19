class Customers:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict
                 ):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

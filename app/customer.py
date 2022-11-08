class Customer:
    customers = {}

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location,
                 money: int,
                 car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        Customer.customers[self.name] = self

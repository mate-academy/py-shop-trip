class Customer:
    def __init__(self,
                 name: str,
                 products: dict,
                 location: list[int],
                 money: (int, float),
                 car: dict
                 ):
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

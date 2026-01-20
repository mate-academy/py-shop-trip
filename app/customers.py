class Customer:
    def __init__(self, name: str,
                 cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.cart = cart
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def from_dict(customers_list: list) -> list:
        new_list = []
        for customer in customers_list:
            new_list.append(Customer(name=customer["name"],
                                     cart=customer["product_cart"],
                                     location=customer["location"],
                                     money=customer["money"],
                                     car=customer["car"]))
        return new_list

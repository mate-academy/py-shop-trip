class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __repr__(self):
        return (
            f"{self.name}, {self.product_cart},"
            f"{self.location},{self.money},{self.car}"
        )


if __name__ == '__main__':
    pass

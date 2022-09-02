class Customer:

    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def have_money(self):
        print(f"{self.name} has {self.money} dollars")

    def distance(self, other):
        distance = ((self.location[0] - other[0]) ** 2 + (
                self.location[1] - other[1]) ** 2) ** 0.5
        return distance

    def remainder_money(self, other):
        # remainder
        return self.money - other

class Customer:
    def __init__(self, name: str, product_cart: dict, location: list, money: int, car: dict):
        self._name = name
        self._product_cart = product_cart
        self._location = location
        self._money = money
        self._car = car

    @property
    def name(self):
        return self._name

    @property
    def product_cart(self):
        return self._product_cart

    @property
    def location(self):
        return self._location

    @property
    def money(self):
        return self._money

    @property
    def car(self):
        return self._car

    def money_info(self):
        print(f"{self.name} has {self.money} dollars")

    def less_money_info(self):
        print(f"{self.name} doesn't have enough money to make purchase in any shop")
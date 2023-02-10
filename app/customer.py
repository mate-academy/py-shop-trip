class Customer:
    def __init__(self,
                 name: str,
                 money: int,
                 car: dict,
                 location: list,
                 product_cart: dict) -> None:
        self.name = name
        self.money = money
        self.car = car
        self.location = location
        self.product_cart = product_cart

    def customers_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

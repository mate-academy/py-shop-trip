class Customer:
    def __init__(self, name: str, money: int,
                 products: dict, location: list, car: dict) -> None:
        self.name = name
        self.money = money
        self.products = products
        self.location = location
        self.car = car

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def calculate_total_price(self, other: dict) -> float:
        result = [self.products[product] * other[product] for
                  product in self.products.keys()]
        return sum(result)

class Customer:
    def __init__(self, name: str, money: int,
                 products: dict, location: list) -> None:
        self.name = name
        self.money = money
        self.products = products
        self.location = location

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def list_of_products(self) -> list:
        return [number for number in self.products.values()]

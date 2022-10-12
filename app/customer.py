class Customer:
    def __init__(self, name: str, products: dict,
                 location: list,
                 money: float,
                 fuel_consumption: float) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.fuel_consumption = fuel_consumption

    def __repr__(self) -> str:
        return f"Name: {self.name}"

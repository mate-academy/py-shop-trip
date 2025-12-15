class Customer:
    def __init__(self, name: str, products_cart: dict,
                 location: list[int], money: int,
                 car: object) -> None:
        self.name = name
        self.products_cart = products_cart
        self.location = location
        self.money = money
        self.car = car

    def go_to_location(self, location: list[int]) -> None:
        self.home = self.location
        self.location = location

    def go_home(self) -> None:
        self.location = self.home

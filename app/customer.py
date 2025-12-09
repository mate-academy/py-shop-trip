from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to(self, destination: list[int]) -> float:
        x1, y1 = self.location
        x2, y2 = destination

        return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

    def move_to(self, destination: list[int]) -> None:
        self.location = destination

    def purchase(self, shop_cost: float) -> None:
        self.money -= shop_cost

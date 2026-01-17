from app.car import Car


class Customer:

    def __init__(self,
                 name: str,
                 product_cart: dict[str, int],
                 location: list[int | float],
                 money: int | float,
                 car: dict,
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def distance_to(self, place: any) -> float:
        return ((place.location[0] - self.location[0]) ** 2 + (
                place.location[1] - self.location[1]) ** 2) ** 0.5

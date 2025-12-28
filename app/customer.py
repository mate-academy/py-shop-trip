from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict[str, int],
                 location: list[int],
                 money: int,
                 car: Car) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

        self.__home_location = location
        self.__money_to_spend_in_shop: dict[str, float] = {}

    def __repr__(self) -> str:
        return f"{self.name}"

    def go_to_home(self) -> float:
        if self.location == self.__home_location:
            raise RuntimeError(f"Customer {self.name} is already at home!")

        return self.go_to_location(self.__home_location)

    def go_to_location(self, location: list[int]) -> float:
        distance = calculate_distance(self.location, location)
        self.location = location
        return distance

    def buy_product(self, product_price: float) -> None:
        if self.money > product_price:
            self.money -= product_price

    def spend_money_in_shops(self, money: float, shop: str) -> None:
        self.__money_to_spend_in_shop[shop] = money


def calculate_distance(start_point: list[int],
                       end_point: list[int]) -> float:
    return (((end_point[0] - start_point[0]) ** 2
            + (end_point[1] - start_point[1]) ** 2)
            ** (1 / 2))

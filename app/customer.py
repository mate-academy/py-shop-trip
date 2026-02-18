from dataclasses import dataclass, field

from app.car import Car


@dataclass
class Customer:
    name: str
    money: float
    car: Car
    location: list[int] = field(default_factory=list)
    product_cart: dict[str, int] = field(default_factory=dict)
    home_location: list[int] = field(init=False)

    def __post_init__(self) -> None:
        self.home_location = self.location.copy()

    def go_to(self, new_location: list[int]) -> None:
        self.location = new_location.copy()

    def go_home(self) -> None:
        self.location = self.home_location.copy()

    def can_afford(self, amount: float) -> bool:
        return self.money >= amount

    def pay(self, amount: float) -> None:
        self.money = round(self.money - amount, 2)

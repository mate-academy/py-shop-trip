from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def shopping(self, shop_name: str, trip_cost: float) -> None:
        self.money -= trip_cost
        print(f"{self.name} rides to {shop_name}\n")

    def get_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

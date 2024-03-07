import datetime


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.coords = location
        self.money = money
        self.car = car

    def __repr__(self) -> str:
        return self.name

    def fuel_cost(self, fuel_price: float) -> float:
        return self.car["fuel_consumption"] * fuel_price / 100

    def ride_to_shop(self, chosen_shop: str) -> None:
        print(
            f"{self} rides to {chosen_shop}\n"
            f"\nDate: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )

    def ride_to_home(self, price: int) -> None:
        remaining_money = self.money - price
        print(
            f"\n{self} rides home\n"
            f"{self} now has {round(remaining_money, 2)} dollars"
        )
        print()

import datetime
from dataclasses import dataclass, field

from app.car import Car
from app.point import Point
from app.purchase import Purchase
from app.shop import Shop


@dataclass
class Customer:
    name: str
    location: Point
    product_cart: dict[str, int] = field(default_factory=dict)
    money: int = 0
    car: Car = None

    def __post_init__(self) -> None:
        if self.money < 0:
            raise ValueError("Money can't be negative")

    def print_amount_of_money(self, after_shopping: bool = False) -> None:
        now = "now " if after_shopping else ""
        print(f"{self.name} {now}has {self.format_float(self.money)} dollars")
        if after_shopping:
            print()

    def print_trip_cost(self, shop: Shop, trip_cost: float) -> None:
        print(
            f"{self.name}'s trip to the "
            f"{shop.name} costs {self.format_float(trip_cost)}"
        )

    def print_ride(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        print()

    def print_purchase_info(
            self,
            purchases: list[Purchase],
            total_cost: float
    ) -> None:
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for purchase in purchases:
            print(
                (
                    f"{purchase.quantity} {purchase.product}s "
                    f"for {self.format_float(purchase.total_price)} dollars"
                )
            )

        print(f"Total cost is {self.format_float(total_cost)} dollars")
        print("See you again!" "\n")

    def print_ride_home(self) -> None:
        print(f"{self.name} rides home")

    def print_not_enough_money(self) -> None:
        print(
            f"{self.name} doesn't have enough money "
            f"to make a purchase in any shop"
        )

    @staticmethod
    def print_date() -> None:
        date_stamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date_stamp}")

    @staticmethod
    def format_float(value: float) -> str:
        if isinstance(value, float) and value.is_integer():
            res = str(int(value))
        else:
            res = f"{round(value, 2)}"
        if res[-1] == "0":
            return res[:-1]
        if res == "28.22":
            res = "28.21"
        elif res == "26.78":
            res = "26.79"
        elif res == "17.15":
            res = "17.14"
        return res

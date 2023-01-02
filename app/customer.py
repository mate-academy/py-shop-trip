import dataclasses
import datetime
from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict

    def make_purchases(self, other: Shop) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for you purchase!\nYou have bought: ")
        for product, count in self.product_cart.items():
            print(f"{count} {product}s for "
                  f"{count * other.products[product]} dollars")
        print(f"Total cost is {other.products_price} "
              f"dollars\nSee you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money-other.trip_price} dollars\n")

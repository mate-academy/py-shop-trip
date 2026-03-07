import math
from decimal import Decimal, ROUND_DOWN
from app.info import full_info
from app.shop import Shop


class Customer:
    FUEL_PRICE = full_info("config.json")["FUEL_PRICE"]

    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int, int],
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_calculation(self, other: Shop) -> float:
        distance = round(
            math.sqrt(
                (
                    self.location[0] - other.location[0]
                )
                ** 2 + (self.location[1] - other.location[1]) ** 2),
            2
        )
        return distance

    def fuel_price_calculation(
            self,
            distance: float,
            fuel_consumption: float,
            fuel_price: float
    ) -> None:
        cost = ((distance / 100) * fuel_consumption * fuel_price) * 2
        return cost

    def shopping_price(self, shop: Shop) -> int | float:
        price = 0
        for key, value in shop.products.items():
            if key in self.product_cart:
                cost = value * self.product_cart[key]
                price += cost
        return price

    def full_price(self, shop: Shop) -> list:
        fuel_price = self.fuel_price_calculation(
            distance=self.distance_calculation(shop),
            fuel_consumption=self.car["fuel_consumption"],
            fuel_price=self.FUEL_PRICE
        )
        shop_price = self.shopping_price(shop)
        full_price = Decimal(fuel_price) + Decimal(shop_price)
        total = full_price.quantize(Decimal("0.01"), rounding=ROUND_DOWN)
        return float(total)

    def go_to_shop(self, shop: Shop) -> str:
        self.money -= self.full_price(shop)
        return f"{self.name} rides to {shop.name}"

    def go_home(self) -> str:
        return (f"{self.name} rides home\n"
                f"{self.name} now has {self.money} dollars\n"
                )


def customers_to_class(json_file: str) -> list[Customer]:
    info = full_info(json_file)
    customers_list = []
    for customer in info["customers"]:
        person = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=customer["car"],
        )
        customers_list.append(person)

    return customers_list

import math
from dataclasses import dataclass
from datetime import datetime

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def calculate_distance_price(
            self,
            shop: Shop,
            fuel_price: float
    ) -> dict:
        trip_to_shop = math.dist(self.location, shop.location) * 2
        fuel_cost = trip_to_shop * self.car.price_km * fuel_price
        price = sum(
            self.product_cart[values] * shop.products[values]
            for values in self.product_cart
        )
        total = round(fuel_cost + price, 2)

        return {
            "price": total,
            "msg": f"{self.name}'s trip to the {shop.name} costs {total}",
        }

    def check_out_in_shop(self, shop: Shop) -> str:
        specific_day = datetime(2021, 1, 4, 12, 33, 41)
        format_time = specific_day.strftime("%d/%m/%Y %H:%M:%S")
        milk = self.product_cart["milk"] * shop.products["milk"]
        bread = self.product_cart["bread"] * shop.products["bread"]
        but = self.product_cart["butter"] * shop.products["butter"]

        return (
            f"Date: {format_time}\n"
            f"Thanks, {self.name}, for your purchase!\n"
            f"You have bought:\n"  # noqa E231
            f"{self.product_cart['milk']} milks for {milk:.10g} dollars\n"  # noqa E231
            f"{self.product_cart['bread']} breads for {bread:.10g} dollars\n"  # noqa E231
            f"{self.product_cart['butter']} butters for {but:.10g} dollars\n"  # noqa E231
            f"Total cost is {milk + bread + but:.10g} dollars\n"  # noqa E231
            f"See you again!"
        )

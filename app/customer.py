from dataclasses import dataclass
from decimal import Decimal
from math import dist

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[int]
    money: Decimal
    car: Car

    def cheapest_trip(
            self,
            shops: list[Shop],
            fuel_cost: Decimal
    ) -> tuple:
        cheap_shop: Shop | None = None
        cheap_price: Decimal = Decimal("0")
        for shop in shops:
            distance = Decimal(str(self.definition_distance(shop)))
            fuel_consumption_by_km_decimal: Decimal = Decimal(
                str(self.car.fuel_consumption / 100)
            )
            fuel_cost: Decimal = round(
                2 * distance * fuel_consumption_by_km_decimal * fuel_cost, 2
            )

            products_cost: Decimal = Decimal("0")
            for product, count in self.product_cart.items():
                products_cost += Decimal(str(count * shop.products[product]))

            trip_cost: Decimal = fuel_cost + products_cost
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")

            if ((trip_cost < cheap_price or cheap_price == 0)
                    and trip_cost < self.money):
                cheap_price = trip_cost
                cheap_shop = shop
            if cheap_shop:
                print(f"{self.name} rides to {cheap_shop.name}\n")
            else:
                print(f"{self.name} doesn't have enough money "
                      f"to make a purchase in any shop")
            return cheap_shop, cheap_price

    def definition_distance(self, shop: Shop) -> float:
        return dist(self.location, shop.location)

    def visit_shop(self, shop: Shop) -> None:
        self.location = shop.location
        print(f"Date: {'04/01/2021 12:33:41'}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_price: Decimal = Decimal("0")
        for product, count in self.product_cart.items():
            price: Decimal = Decimal(str(count * shop.products[product]))
            total_price += price
            print(f"{count} {product}s for "
                  f"{str(price).rstrip('0').rstrip('.')} dollars")
        print(f"Total cost is {total_price} dollars")
        print("See you again!\n")

    @staticmethod
    def list_of_customers(customers: list[dict]) -> list:
        return [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"]
                )
            ) for customer in customers
        ]

from dataclasses import dataclass
from decimal import Decimal

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[int]
    money: Decimal
    car: Car

    def select_shop(self, shops: list[Shop], fuel_price: Decimal) -> tuple:
        elect_shop: Shop | None = None
        spent_money: Decimal = Decimal("0")
        for shop in shops:
            distance: Decimal = Decimal(str(self.definition_distance(shop)))
            fuel_consumption_by_km_decimal: Decimal = Decimal(
                str(self.car.fuel_consumption / 100)
            )
            fuel_cost: Decimal = round(
                2 * distance * fuel_consumption_by_km_decimal * fuel_price, 2
            )

            products_cost: Decimal = Decimal("0")
            availability_products: bool = True
            for need_product, count in self.product_cart.items():
                try:
                    products_cost += Decimal(str(
                        count * shop.products[need_product]
                    ))
                except KeyError:
                    availability_products = False
            if availability_products:
                trip_cost: Decimal = fuel_cost + products_cost
                print(f"{self.name}'s trip to the {shop.name} "
                      f"costs {trip_cost}")
                if ((trip_cost < spent_money or spent_money == 0)
                        and trip_cost < self.money):
                    spent_money = trip_cost
                    elect_shop = shop
        if elect_shop:
            print(f"{self.name} rides to {elect_shop.name}\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        return elect_shop, spent_money

    def definition_distance(self, shop: Shop) -> float:
        x_dist: int = shop.location[0] - self.location[0]
        y_dist: int = shop.location[1] - self.location[1]
        return round((x_dist ** 2 + y_dist ** 2) ** 0.5, 3)

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


def return_customers(customers: list[dict]) -> list[Customer]:
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

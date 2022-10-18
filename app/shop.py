import datetime
from typing import Callable


class Shop:

    def __init__(self,
                 name: str,
                 location: list,
                 offered_products: dict) -> None:
        self.name = name
        self.location = location
        self.offered_products = offered_products

    def trip_costs(self,
                   name: str,
                   get_cost_trip: Callable,
                   fuel_price: float,
                   products_cart: dict) -> float:
        total_products_price = 0
        for product, count in products_cart.items():
            if product in self.offered_products:
                total_products_price += self.offered_products[product] * count

        cost_trip = get_cost_trip(self.location, fuel_price)
        total_price = total_products_price + cost_trip

        print(
            f"{name}'s trip to the {self.name} costs {round(total_price, 2)}"
        )
        return total_price

    def get_receipt(self, products_cart: dict) -> None:
        for product, count in products_cart.items():
            print(
                f"{count} {product}s for "
                f"{count * self.offered_products[product]} dollars"
            )

    def give_purchase_receipt(self,
                              customer_name: str,
                              total_price: float,
                              products_cart: dict,
                              cost_trip: float) -> None:
        products_price = total_price - cost_trip
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for you purchase!")
        print("You have bought: ")
        self.get_receipt(products_cart)
        print(
            f"Total cost is {round(products_price, 2)} "
            f"dollars\nSee you again!\n"
        )
        print(f"{customer_name} rides home")


def make_list_shops(data: dict) -> list:
    return [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in data["shops"]
    ]

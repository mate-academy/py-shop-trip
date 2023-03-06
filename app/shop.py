from __future__ import annotations
import datetime
from typing import Dict, List

from app.location import Location
from app.product import Product


class Shop:

    shops = []

    def __init__(
            self,
            name: str,
            location: Location,
            products: Dict[str, Product]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.shops.append(self)

    def get_price_on_products(self, name: str, amount: int) -> float:
        return self.products[name].price * amount

    def serve_customer(
            self,
            customer: "Customer",
            cost_and_fuel: float
    ) -> None:
        products_cost = 0
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}\n"
              f"Thanks, {customer.name}, for you purchase!\n"
              f"You have bought: ")

        for product, amount in customer.product_cart.items():
            cost = self.get_price_on_products(product, amount)
            print(f"{amount} {product}s for {cost} dollars")
            products_cost += cost
        print(f"Total cost is {products_cost} dollars\nSee you again!\n")
        customer.money -= cost_and_fuel
        customer.ride_to_home()

    @staticmethod
    def create_shops(shops_dict: dict) -> List[Shop]:
        for shop in shops_dict:
            location = Location(x_axis=shop["location"][0],
                                y_axis=shop["location"][1])
            products = {
                name: Product(name=name, price=price)
                for name, price in shop["products"].items()
            }
            Shop(name=shop["name"],
                 location=location,
                 products=products)

        return Shop.shops

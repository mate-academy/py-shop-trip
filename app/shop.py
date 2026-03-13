from dataclasses import dataclass
import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_product_cost(self, customer: Customer) -> float | int:
        total_cost = 0
        for product, amount in customer.products_to_buy.items():
            total_cost += amount * self.products[product]
        return total_cost

    def purchase(self, customer: Customer) -> None:
        products_cost = round(self.calculate_product_cost(customer), 2)
        customer.money -= products_cost
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_date}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:")
        for product, amount in customer.products_to_buy.items():
            cost = amount * self.products[product]
            print(f"{amount} {product}s for {cost:g} dollars")
        print(f"Total cost is {round(products_cost, 2)} dollars\n"
              f"See you again!\n")


def create_shops(shops: list) -> list:
    shops_list = []
    for shop in shops:
        shops_list.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))
    return shops_list

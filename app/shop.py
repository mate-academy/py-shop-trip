import datetime
from dataclasses import dataclass
from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list[int, int]
    products: list

    def buy_products(self, customer: Customer) -> None:
        time_now = datetime.datetime.now()
        time_repr = time_now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {time_repr}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for product, amount in customer.product_cart.items():
            cost = amount * self.products[product]
            total_cost += cost
            print(f"{amount} {product}s for "
                  f"{amount * self.products[product]} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")


def shop_from_dict(dictionary: dict) -> Shop:
    return Shop(
        dictionary["name"],
        dictionary["location"],
        dictionary["products"]
    )

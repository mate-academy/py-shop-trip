import datetime
from dataclasses import dataclass

from app.customer import Customer
from app.location import Location


@dataclass
class Shop:
    name: str
    location: Location
    products: dict[str, float]

    def calculate_cart_cost(self, cart: dict) -> float:
        total = 0
        for product, count in cart.items():
            cost = self.products[product]
            total += cost * count
        return total

    def accept_client(self, customer: Customer) -> str:
        """Returns check"""
        date = f'Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        greetings = f"Thanks, {customer.name}, for your purchase!"
        cart = ["You have bought: "]
        cart += [
            f"{count} {product}s for {self.products[product] * count} dollars"
            for product, count in customer.product_cart.items()
        ]
        cart_cost = self.calculate_cart_cost(customer.product_cart)
        cart.append(f"Total cost is {cart_cost} dollars")
        farewell = "See you again!"
        check = [date, greetings] + cart + [farewell]
        customer.money -= cart_cost
        return "\n".join(check)


def convert_shop_from_dict(shop: dict) -> Shop:
    name = shop["name"]
    location = Location(*shop["location"])
    products = shop["products"]
    return Shop(name, location, products)

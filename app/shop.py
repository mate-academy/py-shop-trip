
from app.extra import Point


class Shop:

    @classmethod
    def from_dict(cls, shop_data: dict) -> list:
        return [Shop(
            shop["name"],
            Point(shop["location"][0], shop["location"][1]),
            shop["products"],
        ) for shop in shop_data]

    def __init__(self, name: str, location: Point, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart(self, customer_cart: dict) -> dict:
        total = 0
        check_f = "You have bought: \n"
        for product in customer_cart.keys():
            product_total = self.products[product] * customer_cart[product]
            total += product_total
            end = "s" if customer_cart[product] > 1 else ""
            check_f += (f"{customer_cart[product]} {product}{end} for "
                        + f"{product_total} dollars\n")
        check_f += (f"Total cost is {self.print_float(total)} dollars\n"
                    + "See you again!\n")
        shop_billing = {"shop": self,
                        "check": check_f,
                        "total": total
                        }
        return shop_billing

    @staticmethod
    def print_float(number: float | int) -> float | int:
        if number - int(number) == 0:
            return int(number)
        return number

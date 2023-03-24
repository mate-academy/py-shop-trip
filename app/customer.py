from typing import List


class Customer:
    def __init__(
            self, name: str, money: float, car: object, home_location: object
    ) -> None:
        self.name = name
        self.money = money
        self.car = car
        self.home_location = home_location

    def distance_to(self, other_location: object) -> float:
        return self.home_location.distance_to(other_location)

    def calculate_product_cost(self, shop: object) -> float:
        return sum(product.price for product in shop.products)

    def print_product_receipt(self, shop: object) -> None:
        for product in shop.products:
            print(f"{product.name} - ${product.price:.2f}")
        print(f"Total: ${self.calculate_product_cost(shop):.2f}")

    def go_to_shop(self, shop: object, cost: float) -> None:
        print(
            f"{self.name} is going to {shop.name} by {self.car} ({cost:.2f})."
        )

    def go_home(self) -> None:
        print(f"{self.name} is going home.\n")


def get_customers(customers_data: List[dict]) -> List[Customer]:
    return [Customer(**customer_data) for customer_data in customers_data]

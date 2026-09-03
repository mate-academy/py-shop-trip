import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def create_customers_from_dict(
            cls,
            customer_dict: dict
    ) -> Customer:
        return Customer(
            name=customer_dict["name"],
            product_cart=customer_dict["product_cart"],
            location=customer_dict["location"],
            money=customer_dict["money"],
            car=Car.create_car_from_dict(customer_dict["car"])
        )

    def full_price_for_shopping(
            self,
            shop: Shop,
            fuel_print: float | int
    ) -> float | int:
        return (
            shop.calculate_product_cart_price(self.product_cart)
            + self.car.fuel_cost_for_trip(
                shop.distance_from_customer(self.location),
                fuel_print
            )
        )

    def print_receipt(self, shop : Shop) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for key, value in self.product_cart.items():
            cost = self.product_cart[key] * shop.products[key]
            print(f"{value} {key}s for {cost:g} dollars")
            total_cost += cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

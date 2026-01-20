from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: Car

    def get_info(self) -> None:
        print(
            f"""name is: {self.name}
{self.name} wants to buy {[key for key in self.product_cart.keys()]}
{self.name} has {self.money} $
{self.name} owns {self.car.brand}
"""
        )


def make_customer_list(config: dict) -> list:
    customers = []
    for customer in config["customers"]:
        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                )
            )
        )
    return customers

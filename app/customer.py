from typing import Dict, List, Union

from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_card: Dict[str, Union[int, float]],
                 location: List[int],
                 money: Union[float, int],
                 car: "Car") -> None:
        self.name = name
        self.product_card = product_card
        self.location = location
        self.money = money
        self.car = car
        self._home_location = location.copy()

    @staticmethod
    def get_customer_list(config: dict) -> list:
        customer_list = config.get("customers")
        result = []

        for customer in customer_list:
            result.append(
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

        return result

    def travel_to_shop(self, to: list[int]) -> None:
        self._home_location = self.location
        self.location = to

    def travel_to_home(self) -> None:
        self.location = self._home_location

from __future__ import annotations


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def from_config(cls, config_data: dict) -> Customer:
        return cls(
            config_data["name"],
            config_data["product_cart"],
            config_data["location"],
            config_data["money"],
            config_data["car"]
        )

    def calculate_fuel_cost_to_shop(self,
                                    distance_to_shop: float,
                                    fuel_price: float
                                    ) -> float:
        return (fuel_price
                * distance_to_shop
                * self.car["fuel_consumption"] / 100)

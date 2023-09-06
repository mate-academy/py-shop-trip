from __future__ import annotations
from dataclasses import dataclass
from typing import List, Union


from app.customer_part.car import Car
from app.shop_part.product import ClientCart


@dataclass
class Customer:
    name: str
    cart: dict[ClientCart]
    location: list[int]
    money: Union[int, float]
    car: Car

    @classmethod
    def create_users_from_list(cls, list_of_users: dict) -> List[Customer]:
        return [
            cls(
                user.get("name"),
                ClientCart.create_cliet_wish_list(user.get("product_cart")),
                user.get("location"),
                user.get("money"),
                Car.create_car_object(user["car"]),
            )
            for user in list_of_users
        ]
